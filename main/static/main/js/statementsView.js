const main = document.querySelector('main');
const statementContainer = document.querySelector('.statement-container');
const paginationContainer = document.querySelector('.pagination-container');

const clearStatementContainer = () => {
    statementContainer.innerHTML = '';
};

const createListElement = (item) => {
    const list = document.createElement('ul');
    list.classList.add('elem', 'w-full', 'h-[60px]', 'flex', 'justify-center', 'items-center', 'text-center', 'hover:bg-none', 'mt-[20px]', 'rounded-[19px]');

    const title = createListElementItem('title', item.title, '25%');
    const payment = createListElementItem('payment', item.payment ? 'Оплачено' : 'Не оплачено', '25%', item.payment ? 'bg-[#69d92e]' : 'bg-[#d41c1c]');
    const status = createListElementItem('status', getStatusText(item.status), '25%');
    const fileLink = createListElementFileLink(item.file);
    const date = createListElementItem('date', item.date, '25%');

    list.append(title, payment, status, fileLink, date);
    return list;
};

const createListElementItem = (key, text, width, additionalClass) => {
    const item = document.createElement('li');
    item.classList.add('flex', 'justify-center', 'items-center', `w-[${width}]`, 'h-full', 'border-r-[1px]', 'border-[#3a3a3a]', additionalClass);
    const span = document.createElement('span');
    span.innerText = text;
    item.append(span);
    return item;
};

const createListElementFileLink = (file) => {
    const item = document.createElement('li');
    item.classList.add('flex', 'justify-center', 'items-center', 'w-[25%]', 'h-full', 'cursor-pointer', 'border-r-[1px]', 'border-[#3a3a3a]');
    const fileLinkAnchor = document.createElement('a');
    fileLinkAnchor.href = file;
    fileLinkAnchor.innerText = 'Download File';
    fileLinkAnchor.classList.add('w-full', 'h-full', 'cursor-pointer', 'flex', 'justify-center', 'items-center');
    item.append(fileLinkAnchor);
    return item;
};

const getStatusText = (status) => {
    switch (status) {
        case 'Отправлено':
        case 'Принято в работу':
            return 'Отправлено';
        case 'Готово':
            return 'Готово';
        default:
            return status;
    }
};

const renderData = (data) => {
    clearStatementContainer();

    data.results.forEach(item => {
        const list = createListElement(item);
        statementContainer.append(list);
    });

    if (data.next || data.previous) {
        renderPaginationButtons(data.next, data.previous);
    }
};

const getData = async (url) => {
    try {
        const response = await fetch(url);
        const data = await response.json();
        renderData(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

const createPaginationButton = (label, link) => {
    const button = document.createElement('button');
    button.innerText = label;

    button.addEventListener('click', () => {
        getData(link);
    });

    return button;
};

const renderPaginationButtons = (nextLink, prevLink) => {
    paginationContainer.innerHTML = '';
    paginationContainer.classList.add('mt-10');

    if (prevLink) {
        const prevButton = createPaginationButton('Previous', prevLink);
        prevButton.classList.add('mr-5', 'bg-[#2e2e2e]', 'rounded-[10px]', 'py-[10px]', 'px-[20px]');
        paginationContainer.appendChild(prevButton);
    }

    if (nextLink) {
        const nextButton = createPaginationButton('Next', nextLink);
        nextButton.classList.add('mr-5', 'bg-[#2e2e2e]', 'rounded-[10px]', 'py-[10px]', 'px-[20px]');
        paginationContainer.appendChild(nextButton);
    }
};

getData('http://127.0.0.1:8000/api/v1/statement/');
