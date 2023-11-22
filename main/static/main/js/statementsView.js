const main = document.querySelector('main');
const statementContainer = document.querySelector('.statement-container');
const paginationContainer = document.querySelector('.pagination-container');

const getData = async (url) => {
    try {
        statementContainer.innerHTML = ''

        const response = await fetch(url);
        const data = await response.json();

        data.results.forEach(item => {
            const list = document.createElement('ul');
            list.classList.add('elem', 'w-full', 'h-[60px]', 'flex', 'justify-center', 'items-center', 'text-center', 'hover:bg-none', 'mt-[20px]', 'rounded-[19px]');

            const title = document.createElement('li');
            const payment = document.createElement('li');
            const status = document.createElement('li');
            const date = document.createElement('li');
            const fileLink = document.createElement('li');

            title.classList.add('flex', 'justify-center', 'items-center', 'w-[25%]', 'h-full', 'border-r-[1px]', 'border-[#3a3a3a]');
            payment.classList.add('flex', 'justify-center', 'items-center', 'w-[25%]', 'h-full', 'border-r-[1px]', 'border-[#3a3a3a]');
            status.classList.add('flex', 'justify-center', 'items-center', 'w-[25%]', 'h-full', 'border-r-[1px]', 'border-[#3a3a3a]');
            fileLink.classList.add('flex', 'justify-center', 'items-center', 'w-[25%]', 'h-full', 'cursor-pointer', 'border-r-[1px]', 'border-[#3a3a3a]')
            date.classList.add('flex', 'justify-center', 'items-center', 'w-[25%]', 'h-full');

            const titleSpan = document.createElement('span');
            const paymentSpan = document.createElement('span');
            const statusSpan = document.createElement('span');
            const dateSpan = document.createElement('span');
            const fileLinkAnchor = document.createElement('a');

            titleSpan.innerText = item.title;
            dateSpan.innerText = item.date;
            fileLinkAnchor.href = item.file;
            fileLinkAnchor.innerText = 'Download File';
            fileLinkAnchor.classList.add('w-full', 'h-full', 'cursor-pointer', 'flex', 'justify-center', 'items-center')

            if (item.payment) {
                paymentSpan.innerText = 'Оплачено';
                paymentSpan.classList.add('bg-[#69d92e]', 'px-[20px]', 'py-[7px]', 'rounded-[10px]', 'font-bold');
            } else {
                paymentSpan.innerText = 'Не оплачено';
                paymentSpan.classList.add('bg-[#d41c1c]', 'px-[20px]', 'py-[7px]', 'rounded-[10px]', 'font-bold');
            }

            if (item.status === 'Отправлено' || item.status === 'Принято в работу') {
                statusSpan.innerText = item.status;
                statusSpan.classList.add('bg-[#d3eb1e]', 'px-[20px]', 'py-[7px]', 'rounded-[10px]', 'font-bold');
            } else if (item.status === 'Готово') {
                statusSpan.innerText = item.status;
                statusSpan.classList.add('bg-[#69d92e]', 'px-[20px]', 'py-[7px]', 'rounded-[10px]', 'font-bold');
            } else {
                statusSpan.innerText = item.status;
                statusSpan.classList.add('bg-[#d41c1c]', 'px-[20px]', 'py-[7px]', 'rounded-[10px]', 'font-bold');
            }

            title.append(titleSpan);
            payment.append(paymentSpan);
            status.append(statusSpan);
            fileLink.append(fileLinkAnchor);
            date.append(dateSpan);

            list.append(title);
            list.append(payment);
            list.append(status);
            list.append(fileLink);
            list.append(date);

            statementContainer.append(list);
        });

        if (data.next || data.previous) {
            renderPaginationButtons(data.next, data.previous);
        }
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
    paginationContainer.classList.add('mt-10')

    if (prevLink) {
        const prevButton = createPaginationButton('Previous', prevLink);
        prevButton.classList.add('mr-5', 'bg-[#2e2e2e]', 'rounded-[10px]', 'py-[10px]', 'px-[20px]')
        paginationContainer.appendChild(prevButton);
    }

    if (nextLink) {
        const nextButton = createPaginationButton('Next', nextLink);
        nextButton.classList.add('mr-5', 'bg-[#2e2e2e]', 'rounded-[10px]', 'py-[10px]', 'px-[20px]')
        paginationContainer.appendChild(nextButton);
    }
};

getData('http://127.0.0.1:8000/api/v1/statement/');
