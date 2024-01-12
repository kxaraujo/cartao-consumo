// Parcelar Compra
function calcularParcelas() {
    const valorCompra = parseFloat(document.getElementById('valor_compra').value);
    const numParcelas = parseInt(document.getElementById('num_parcelas').value);

    if (!isNaN(valorCompra) && !isNaN(numParcelas) && numParcelas > 0) {
        const valorParcela = valorCompra / numParcelas;
        document.getElementById('valor_parcela').innerText = `Valor da Parcela: R$${valorParcela.toFixed(2)}`;
    } else {
        document.getElementById('valor_parcela').innerText = '';
    }
}
