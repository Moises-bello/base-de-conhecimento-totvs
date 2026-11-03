---
article_id: 360025818694
category: SIGAEST - PODER DE TERCEIROS
content_hash: 73dd249c528ff20dd855d404de3abda977cab0f40fefd1e1d7aa4223c4e88499
fetched_at: '2026-06-28T22:39:03.261029+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo para recebimento
  de Beneficiamento com MP de Terceiros
type: support-article
updated_at: '2024-06-12T01:28:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025818694-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-para-recebimento-de-Beneficiamento-com-MP-de-Terceiros
---

**Dúvida**Vou receber Matéria Prima (MP) de um terceiro para fazer um serviço ou montar um PA. Como controlar este fluxo do recebimento da MP até o retorno do Produto Acabado no *Protheus?*  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Nesta operação recebemos do cliente uma MP a qual iremos transformar em produto acabado. Porém como na devolução desta remessa temos que devolver o produto como MP (para dar baixa no poder de terceiros) iremos tratar o serviço executado como PA**.** No exemplo abaixo recebemos o produto **CHAPA** e transformamos em uma **fita** (**SV.CORTE**). Vamos aos passos:

**1) CADASTRAR OS PRODUTOS:**  
a) Produto: CHAPA         Descrição: Chapa                   Tipo: MP  
b) Produto: SV.CORTE   Descrição: Serviço de corte   Tipo: PA  
  
**2) CADASTRAR ESTRUTURA:**  
SV.CORTE  
  |\_ CHAPA  
  
**3) CADASTRAR OS TES (TIPOS DE ENTRADA E SAÍDA):**  
001 • Entrada: (CHAPA)      – Poder Terceiros = Remessa            - Estoque = SIM  
501 • Saída:   (CHAPA)       – Poder Terceiros = Devolução          - Estoque = NÃO  
502 • Saída:   (SV.CORTE)   – Poder Terceiros = Não Controla     - Estoque = SIM 

OBS: Os números dos TES são meramente ilustrativos.  
  
**4) RECEBENDO A MATÉRIA-PRIMA (MATA103)**  
Tipo da Nota = Normal (se receber de um Fornecedor) ou Beneficiamento (se  receber de um Cliente)  
Incluir o produto CHAPA na nota com a quantidade enviada pelo fornecedor/cliente e utilizar o TES 001.  
  
**5) ABERTURA DE OP PARA O PRODUTO "SV.CORTE"**  
  
**6) PRODUÇÃO E ENCERRAMENTO DA OP**  
OBS: Se a requisição da MP "CHAPA" for realizada manualmente via Movimentos Internos (MATA240/MATA241), dar um F12 e selecionar o parâmetro "Cons. Saldo de 3º N/ Poder?=SIM". Caso a requisição seja feita automaticamente (Apontamento de Produção - MATA250) não é necessário fazer nenhum outro procedimento.  
  
**7) ESTOQUE APÓS APONTAR A PRODUÇÃO**  
Após a produção será gerado estoque do produto SV.CORTE, consumindo o saldo em estoque do produto CHAPA.  
  
**8) DEVOLUÇÃO E FATURAMENTO DOS ITENS**  
Tipo da Nota = Normal (se recebeu a chapa de Cliente) ou Utiliza Fornecedor (se recebeu a chapa de Fornecedor)

1º Item: CHAPA - TES: 501 (Sem atualizar estoque pois o produto já foi consumido na produção)

2º Item: SV.CORTE  - TES: 502   
  
**OBS.1**: Uma maneira sugerida para fazer essa devolução é: 

Acessar à rotina MATA410 (Pedido de Vendas) -> clicar em "Outras Ações" -> "Retornar" -> Selecionar os filtros (Cliente ou Fornecedor) e data do documento da entrada (ou pelo número do documento da entrada). Desta forma o sistema puxará o item CHAPA, bastando ajustar o TES para 501 e em seguida adicionar manualmente o segundo item "SV.CORTE" com TES 502.

**OBS.2:** No processo NF de Beneficiamento, e de remessa e retorno para Terceiro, sempre se faz necessário o vinculo da NF Origem ao realizar o retorno do Documento, para ser realizada a Baixa do Poder de Terceiro.

**Informações Importantes:**

Para o cenário em que deseja [**não agregar o custo do produto (MP)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771732-MP-SIGAEST-N%C3%A3o-agregar-custo-na-produ%C3%A7%C3%A3o?source=search) recebido de terceiros, deve-se realizar o seguinte procedimento:  
  
*• Para o produto que não queremos que o custo seja agregado ao PA (No nosso caso a MP recebida de terceiros), o campo B1\_AGREGCU deverá ser preenchido com "1=Permite não agregar".*  
*• Para o tipo de movimentação utilizada na produção ou na requisição do produto, o campo F5\_AGREGCU deve estar como "2-Não agrega".*  
  
Dessa forma o custo da MP não será agregado.

**Saiba mais:**

*[MP - SIGAEST - Como efetuar o processo de Remessa para Beneficiamento de OP Em Terceiros?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063627613-MP-SIGAEST-Como-efetuar-o-processo-de-Remessa-para-Beneficiamento-de-OP-Em-Terceiros-)*

*[Clique aqui para acessar mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)*
