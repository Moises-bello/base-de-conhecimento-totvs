---
article_id: 360024679951
category: Materiais - Compras (SIGACOM)
content_hash: dd70dc9f71c3ed8518330fecf53379a43fd14b1a392cb9c6d4122a6633301279
fetched_at: '2026-06-28T22:41:07.732675+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Lançar Despesas
  de Importação no Compras (MATA119) ?
type: support-article
updated_at: '2022-10-18T16:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024679951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Lan%C3%A7ar-Despesas-de-Importa%C3%A7%C3%A3o-no-Compras-MATA119
---

**Dúvida**Como Lançar Despesas de Importação no Compras (MATA119) ?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
  
**Solução**

Semelhante ao Conhecimento de Frete, esta rotina tem a finalidade de emitir uma nota fiscal de complemento onde serão discriminadas despesas de importação feita por uma importadora.   
  
A rotina facilita a digitação das despesas de importação, permitindo o valor total das despesas, pago sobre as notas de entrada associadas.

Esta rotina é utilizada apenas por usuários que não trabalham com o Ambiente SIGAEIC, visto que este ambiente possui rotinas mais detalhadas e abrangentes que esta (MATA119).

* **Para gerar a nota fiscal de despesas de importação:**

1. Na janela de Manutenção de Despesas de Importação, o sistema apresenta a tela de parametrizações da rotina.
2. Preencha os dados conforme orientação do help de campo.![MATA119.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005770341/MATA119.png)![mata119_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005662622/mata119_1.png)
3. Confira os dados e confirme.  
   O sistema apresentada uma nova tela de parâmetros.![MATA119_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005770361/MATA119_3.png)
4. Configure-os com atenção.
5. Confira os dados e clique no botão "Ok" .  
   Com base no critério especificado, o sistema exibe as notas de entrada para a escolha da qual deve-se referenciar a nota de despesas de importação.![MATA119_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005770381/MATA119_4.png)
6. Selecione as notas com um duplo clique sobre seu registro para que fique marcada com um "X" e Selecione, então, a opção "Gera Despesa". ![mata119_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005770421/mata119_5.png)
7. Caso alguma outra nota de despesa já tenha sido vinculado a mesma origem, o sistema emite um alerta em tela, porém permite nova inclusão, ou seja, novo vínculo. Basta clicar em OK.![mata119_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005662782/mata119_6.png)
8. A partir disto, o programa estrutura e já a montagem de uma nova nota com os valores adequados à 2a tela de digitação dos parâmetros da rotina. Caso haja mais de um produto na nota de entrada(origem), os valores serão calculados segundo a proporção da compra de cada produto.  
   É possível alterar alguns dados, se necessário. O campo quantidade é desabilitado.![mata119_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005770601/mata119_7.png)
9. Preencha os dados das "Pastas do Rodapé". O rodapé da tela apresenta seis pastas contendo informações referentes à Nota de Despesas de Importação. Algumas destas pastas apresentam campos que podem ser preenchidos de acordo com a necessidade do usuário.
10. A amarração entre a nota de entrada com a nota de despesas de importação é gravada dentro da tabela SF8 no sistema. ![MATA119_8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005662862/MATA119_8.png)
11. A tabela SF8 também grava as amarrações efetuadas pela rotina MATA116, conhecimento de frete, porém o campo F8\_TIPO é quem destingue por qual operação ou qual o tipo de vínculo que foi efetuado com a nota de origem. Ele grava D = Despesa de Importação (MATA119) e ele grava F quando for conhecimento de frete (MATA116).![MAT119_9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005662902/MAT119_9.png)

**Estorno das Despesas de Importação:**Nesta rotina, também é possível estornar (desmarcar) as notas fiscais que entraram no rateio de uma determinada Nota Despesas de Importação (permitindo que estas possam ser novamente marcadas na geração de outra nota fiscal).

***Excluindo Notas de Despesas de Importação:***

* **Para excluir a Nota Fiscal de Despesas de Importação:**

1. Na rotina de "Desp. Importação", preencha os parâmetros conforme descrito na rotina de Geração da Nota de Despesas de Importação. Porém, informe o parâmetro "Quanto a Nota?" como "Excluir NF de Desp. Importação".
2. Confirme a parametrização.  
   O sistema apresenta a tela com as notas de despesas de importação geradas.
3. Posicione o cursor sobre a nota desejada e clique no botão "Excluir".  
   O sistema apresenta nota na tela para checagem dos dados.
4. Confira-os e confirme.

***Obs::***

Por padrão o sistema carregará na rotina de despesa de importação os mesmos produtos que estão na nota de origem a qual o sistema está sendo vinculado e o valor da despesa será rateado entre os produtos, pois é uma despesa referente aos produtos importados, mesmo porque o valor da despesa precisa ser incorporado aos produtos da NF.  
Não é possível efetuar alteração/inclusão de produto.

***Saiba Mais***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao Gerar Nota de Despesas de importação(MATA119) está trazendo Itens que não constam na Nota de Origem selecionada.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424836917783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-Gerar-Nota-de-Despesas-de-importa%C3%A7%C3%A3o-MATA119-est%C3%A1-trazendo-Itens-que-n%C3%A3o-constam-na-Nota-de-Origem-selecionada-?source=search)

[PÁGINA CENTRALIZADORA DE COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
