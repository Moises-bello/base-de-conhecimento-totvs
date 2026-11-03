---
article_id: 6777494398231
category: Financeiro - Carta de Cobrança
content_hash: f6b2be12e3f3dcef4bceb76e93ae612bf0241004c3de424e08e07517cd4491d0
fetched_at: '2026-06-28T22:37:28.989349+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA811 - Como realizar
  o envio da carta de cobrança
type: support-article
updated_at: '2026-01-16T19:37:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6777494398231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA811-Como-realizar-o-envio-da-carta-de-cobran%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18226128950423) Tempo aproximado para leitura: **00:07:00 min**  
  
**Dúvida**  
Como realizar o envio da carta de cobrança?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA811 - Todas as versões  
  
**Solução**

Para o envio das cartas, deve ser respondida cada etapa do *wizard*, conforme explicação a seguir.

 - Tela inicial do *wizard*.  
![Step_1.JPG](https://tdn.totvs.com/download/attachments/196805118/Step_1.JPG?version=2&modificationDate=1439835191000&api=v2)  
  
 - Definição dos parâmetros para busca e filtragem das informações.   
  
![](https://tdn.totvs.com/download/attachments/492706741/image2021-6-23_14-41-49.png?version=1&modificationDate=1624470109717&api=v2)

1. **Cliente e loja de** (intervalo inicial de cliente e loja);
2. **Cliente e loja até** (intervalo final de cliente e loja);
3. **Vencimento de** (intervalo de vencimento inicial dos títulos);
4. Vencimento até (intervalo de vencimento final dos títulos);
5. **Valor de** (intervalo de valor inicial dos títulos);
6. **Valor até** (intervalo de valor final dos títulos);
7. **Seleciona filiais** (caso seja definido com "**Sim**", a tela padrão de seleção de filiais será exibida para que as filiais possam ser selecionadas);
8. **Situação de cobrança** (será apresentada a mesma consulta já utilizada no requisito "**Processos** **SERASA**", permitindo que uma ou mais situações de cobrança sejam selecionadas. Este campo é validado para não ser deixado em branco ao avançar no processo);
9. **Títulos a vencer** (caso esteja como sim, o filtro vai considerar os títulos que ainda estão por vencer);
10. **Data de referência** para cálculo de juros e multa dos títulos;
11. **Considera valor** (caso seja definido com "**1-Valor Total**", sistema irá filtrar os registros com conteúdo no campo **E1\_VALOR** entre os valores informados nos itens 5 e 6 dessa janela. Caso seja definido com "**2-Saldo**", o sistema irá filtrar os registros com conteúdo no campo **E1\_SALDO** entre os valores informados nos itens 5 e 6 dessa janela );
12. **Considera cliente bloqueado?** Essa pergunta irá validar o campo **A1\_MSBLQL** dos clientes. Se preenchido com **SIM**, irá considerar todos os clientes independentemente do status do campo de bloqueio. Se **NÃO**, irá considerar apenas clientes ativos.

 - Seleção do layout da carta (apenas 1 layout poderá ser selecionado).  
  
![Step_3.JPG](https://tdn.totvs.com/download/attachments/196805118/Step_3.JPG?version=2&modificationDate=1439835215000&api=v2)  
  
 - Seleção do(s) cliente(s).  
  
  
![](https://tdn.totvs.com/download/attachments/492706741/image2022-5-19_8-41-7.png?version=1&modificationDate=1652960467757&api=v2)

**Importante**

Nesta tela do *wizard* existe um botão para realização de filtros na lista de clientes ("Filtrar"), porém somente os campos a seguir estão habilitados para realização/execução de filtros: **A1\_FILIAL** (Filial do cadastro do cliente), **A1\_COD** (Código do cliente), **A1\_LOJA** (Loja do cliente), **A1\_NOME** (Razão social do cliente), **A1\_END** (Endereço do cliente) e, **A1\_EMAIL** (E-mail do cliente)

 - Seleção do(s) título(s).

![Step_5.JPG](https://tdn.totvs.com/download/attachments/196805118/Step_5.JPG?version=2&modificationDate=1439835245000&api=v2)

É importante ressaltar que a seleção de títulos deve considerar o bloqueio de situação de cobrança configurado (conforme já citado anteriormente).

 - Envio ou impressão das cartas.  
  
![Step_6.JPG](https://tdn.totvs.com/download/attachments/196805118/Step_6.JPG?version=2&modificationDate=1439835269000&api=v2)  
  
 - Consulta de log dos envios e conclusão do processo.  
  
![Step_7.JPG](https://tdn.totvs.com/download/attachments/196805118/Step_7.JPG?version=1&modificationDate=1439835294000&api=v2)  
  
- Consulta do log  
  
![](https://tdn.totvs.com/download/attachments/492706741/image2019-5-22_13-36-8.png?version=1&modificationDate=1558542968870&api=v2)  
  
 - Modelo do e-mail enviado ao cliente.  
  
![image2019-1-29_18-12-0.png](https://tdn.totvs.com/download/attachments/196805118/image2019-1-29_18-12-0.png?version=1&modificationDate=1548792720600&api=v2)

Obs: Estes campos são somente enviados pela rotina FINA811, os mesmos não são enviados pela FINA713, somente as informações de e-mail

**Saiba Mais**  
[Carta de Cobrança - Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)
