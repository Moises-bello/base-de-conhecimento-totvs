---
article_id: 360026405292
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: 0e7e9549365db697ecb198ea23a5fde2140c1724d8887b1f769887b49109ea49
fetched_at: '2026-06-28T22:36:58.143484+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Nota complementar
  no exportação
type: support-article
updated_at: '2023-10-26T19:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026405292-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Nota-complementar-no-exporta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como gerar uma nota complementar no Exportação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – *Easy Export Control* – A partir da versão 11.80  
  
**Solução**A rotina de NF Complementos possibilita ao exportador fazer uma nota complementar a nota principal do processo.   
Caso o exportador tenha alguma despesa, mudança na variação cambial fixada para o processo e despesas complementares que irão impactar na diferença entre a nota principal e o real valor gerado na nota fiscal do processo é necessário gerar a nota fiscal de complemento. O sistema permite gerar três tipos de Notas Fiscais de Complemento, são elas:   
  
**A- Nota Fiscal Complementar de Câmbio:** Para gerar uma Nota Fiscal complementar de Câmbio o processo realizado pelo exportador deve sofrer um acerto de variação cambial, onde é necessário que haja um embarque, com a data de embarque preenchida e com pelo menos uma a parcela de cambio contratada, para verificação da variação cambial entre a data considerada para o embarque e a data da liquidação do câmbio.   
  
**B- Nota Fiscal Complementar de Despesas:** Será necessário realizar a inclusão de uma Nota Fiscal Complementar de Despesas quando o processo tiver despesas internacionais e/ou quando o processo possuir um Incoterm que prevê despesas como frete, seguro e etc. Neste caso, o embarque deve ter data de embarque preenchida para que o sistema considere as despesas do mesmo.   
  
**C- Nota Fiscal Complementar de Embarque:** Será necessário realizar a Nota Fiscal Complementar de embarque, quando houver a necessidade de gerar uma Nota Fiscal Complementar de Câmbio e de Despesas para o mesmo processo e também a Nota Fiscal Complementar de preço. Neste caso não é necessário ter a data de embarque preenchida para que o sistema entenda que existe variação de preço no processo.  
  
Caso seja necessário, é possível configurar a série para a geração da nota complementar através do parâmetro **MV\_EECSERI**.  
É necessário habilitar os paramentos **MV\_EECFAT** com o conteúdo .T.  
  
**Nota fiscal complementar de preço**  
A rotina de NF de Complemento possibilita ao exportador fazer uma nota complementar a nota principal do processo. Sendo assim, toda despesa que não foi contemplada na nota fiscal do processo fica sujeito a ser contemplada na nota fiscal complementar.   
  
Pré-Requisitos:   
A- Possuir um Pedido de Exportação cadastrado;  
B-Possuir um Documento de Saída gerado no Faturamento;  
C- Possuir um Embarque cadastrado;  
D- Alterar o embarque e alterar o valor do produto vinculado ao mesmo e informar a data de embarque.   
  
**Exemplo – Como Gerar uma Nota Fiscal de Complemento de Preço:**   
1. No Easy Export Control (SIGAEEC), acesse Atualizações\ Financeiro\ N.F. Complementos.   
2. Na tela que será apresentada, é possível visualizar todos os processos que podem ser gerado a nota.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025981232)

3. Selecione Ações Relacionadas e após selecione Legenda. Veja os status para os processos cadastrados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025984071)

4. Selecione o processo cadastrado anteriormente e selecione Ações Relacionadas e após selecione NFC Embarque.   
  
5. Será apresentado a tela abaixo, selecione Ok.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025984091)

6. Ao clicar em Ok será exibida a mensagem abaixo informando a diferença de preço entre o pedido e o preço informado no embarque. selecione Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025981392)

7. O sistema irá processar a geração da nota fiscal complementar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025984171)

8. Após o processamento, o sistema irá apresentar a mensagem abaixo informando o número da nota gerado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025981532)

**Exemplo – Como visualizar o Pedido de Venda:**   
1. No Faturamento (SIGAFAT), acesse Atualizações\ Pedidos\ Pedidos de Venda.   
2. Com isso o sistema irá gerar um pedido de venda do tipo complemento de preço e automaticamente uma nota de complemento de preço no faturamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025984251)

**Exemplo – Como visualizar a Nota Fiscal de Complemento:**   
1. No Faturamento (SIGAFAT), acesse Atualizações\ Faturamento\ Documento de Saída.   
2. Será possível visualizar a nota de complemento de preço no faturamento. selecione Visualizar doc.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025981652)

3. Será possível visualizar a nota gerada com o valor complementar à nota principal do sistema. Observe o número da Nota Fiscal Original.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025981672)  
  
**Saiba mais**  
[Nota complementar de exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=516650895)
