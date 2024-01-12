// Confirmar Pagamento Parcelado
function confirmarPagamentoParcelado() {
    const confirmacao = confirm("Deseja confirmar o pagamento parcelado?");
    
    if (confirmacao) {
        document.getElementById('form-parcela').submit();
    } else {
        alert("Pagamento cancelado.");
    }
}
