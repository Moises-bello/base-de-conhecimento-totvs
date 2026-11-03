---
content_hash: ed4453ee917bbc8fdd73e0cd305e81b0af14229c154366f690ead4e1c66364fc
fetched_at: '2026-06-29T00:10:01.381798+00:00'
page_id: '452718711'
product: rm
source: tdn-rm
title: Liberação de Flags de FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718711
version: 2
---

As flags são dispositivos utilizados para detectar, se houve, alguma alteração na ficha cadastral do funcionário. Aqui, você poderá liberar (limpar) as flags.

**Exemplo**

Houve mudança no número da carteira de trabalho do funcionário. Após gerar o arquivo para recolhimento do FGTS, será necessário fazer a liberação de flag para limpar a informação da ficha cadastral, para que não sejam enviados os mesmos registros de alteração no próximo recolhimento de FGTS.  
 Para a liberação, defina o "Código de quebra" Em seguida, clique em "Seleção de Funcionários" para acessar a janela de seleção. Selecione e clique em OK.

**Opções de liberação**

Selecione qual(is) item(ns) deseja que os flags sejam liberados. Por default todos os itens virão selecionados, mas se desejar que somente sejam liberados os flags da alteração do nome do funcionário, por exemplo, deixe marcado somente este item.  
    
 **Executar**

O sistema exibirá o número de funcionários que foram processados e um resumo de erros/avisos.  
    
 **Atenção**  
 Caso seja necessário enviar informações que tenham a flag marcada, ao entrar no módulo poderá ser selecionado apenas as opções para liberação da flag.  
    
 **Exemplo**  
 Precisa ser liberada a flag do Número do PIS e não pode liberar a flag do Endereço de Correspondência, basta desmarcar o parâmetro do Endereço de Correspondência que a flag do mesmo continua marcada internamente e será informada a alteração no arquivo do SEFIP. Este procedimento se faz necessário, por exemplo para admitidos no mês. E poderá ser feito para outros campos, por exemplo, quer informar a mudança de dados somente da Carteira de Trabalho, desmarca o parâmetro da Carteira de Trabalho e deixa todos os outros marcados que somente a flag da Carteira de Trabalho não será liberada. O mesmo serve se for para um funcionário apenas, que neste caso deve fazer o filtro na seleção do funcionário que a flag continuará marcada.
