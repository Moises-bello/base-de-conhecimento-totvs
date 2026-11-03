---
content_hash: 0190251934e703a37e89cc2970208d3f0d9138461f702d81e91a674ce96487dd
fetched_at: '2026-06-29T00:10:31.103003+00:00'
page_id: '520661767'
product: rm
source: tdn-rm
title: Meio de pagamento do item de baixa no movimento. 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520661767
version: 2
---

# DEDUINTEGRACOES-5753 NF-e - Meio de Pagamento

## **01.****DADOS GERAIS**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de movimento |
| **Ticket:** |  |
| **Requisito/Story/Issue (informe o requisito relacionado)****:** |  |

## **02.****SITUAÇÃO/REQUISITO**

Cliente necessita que a tag tPag do XML da NF-e seja gerada como “15 - Tipo de Pagamento Boleto”, conforme Manual do Contribuinte. Porém, essa a tag em questão está sendo levada como “99 – Outros” na geração de movimentos pelo Educacional. Isto ocorre porque o TOTVS Gestão Educacional não envia os dados de pagamento para a geração do movimento. O preenchimento desta informação é baseado na Forma de Pagamento que está sendo gerada no movimento.

Se habilitarmos o parâmetro "Utiliza Edição de Meio De pagamento" nos parâmetros do Tipo de movimento, em 'Fin. - Condições de pagamento', afim de que o Educacional leve esta informação para o Movimento é apresentado mensagem de erro na geração do movimento.

## **03.****SOLUÇÃO**

Foi realizado uma evolução no TOTVS Gestão Educacional para que seja possível enviar os dados de pagamento na geração de movimento quando os lançamentos estiverem com o status ***baixado***. Para geração de movimentos de lançamentos ***não baixados***, foi criado um parâmetro para que seja informado o valor default da forma de pagamento a ser enviada na nota fiscal com a tag <TPag> baseada nesta informação.

**Parametrização**

No módulo Movimento, deverá utilizar o parâmetro “Utiliza Edição de Meio De pagamento”, nas configurações do tipo de movimento.

Assim, de acordo com a forma de pagamento informada no momento da baixa, o sistema preencherá a tag <tPag> na NF-e.

**Geração de Movimento de lançamentos baixados**

No processo de geração de movimento no educacional para lançamentos já baixados, serão enviados os dados de pagamento oriundos da baixa.

Para verificar o resultado, acessar o módulo Movimento, e no menu Vendas / Faturamento / Movimentação visualizar os dados contidos na página Integrações / Financeira. Confirme que o campo forma de pagamento contém a mesma forma de pagamento informado na baixa.

**Geração de Movimento de lançamentos baixados**

Para a geração de movimentos cujos lançamentos não estejam com status ***baixado,*** foi criado o parâmetro de Integração Fiscal “Forma de pagamento padrão para geração de movimento (lançamentos não baixados)”. O objetivo deste parâmetro é informar ao módulo Movimento o meio de pagamento que será enviado para a NFe para tais movimentos com lançamentos não baixados.

Para alterar esta configuração, basta acessar o módulo Educacional, menu Ambiente / Parâmetros / Educacional, e na opção Integração / Fiscal / Fiscal 2/2.

Ao gerar um movimento para um boleto cujo lançamento não esteja baixado, o sistema deverá carregar como forma de pagamento o padrão configurado acima.
