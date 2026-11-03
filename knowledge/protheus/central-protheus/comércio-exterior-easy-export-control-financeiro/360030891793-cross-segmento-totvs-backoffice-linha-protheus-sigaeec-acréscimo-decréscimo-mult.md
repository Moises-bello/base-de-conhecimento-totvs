---
article_id: 360030891793
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: e4dbe73df7a89cccca48624a2d383fe2a16642190179b0c50fa55613aedc27fa
fetched_at: '2026-06-28T22:36:58.078612+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Acréscimo, decréscimo,
  multa, juros e desconto no câmbio de exportação
type: support-article
updated_at: '2022-06-10T20:58:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030891793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Acr%C3%A9scimo-decr%C3%A9scimo-multa-juros-e-desconto-no-c%C3%A2mbio-de-exporta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:05:00 min  
  
Dúvida**Como informar Acréscimo, decréscimo, multa, juros e desconto no câmbio de exportação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Para que seja aplicado verifique a configuração do parâmetro MV\_EEC0046, acréscimo, decréscimo, multa, juros e desconto no câmbio de exportação, verifique o documento: [DTRADE-2953 DT Acréscimo, decréscimo, multa, juros e desconto no câmbio de exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=504821428)  
1. Acesse Atualizações/ Financeiro / Câmbio, posicione sobre o processo de embarque embarcado anteriormente e clique no botão “Alterar”. O sistema irá exibir as parcelas, tanto a receber quanto a pagar (quando houver), com seus respectivos números de título financeiro gravados.  
2. Selecione uma parcela, podendo esta ser uma parcela de câmbio a receber ou a pagar, e que possua saldo do embarque não adiantado e clique no botão “Outras Ações/ Liquidar”.  
3. Verifique os campos “Desconto”(EEQ\_DESCON), “Multa”(EEQ\_MULTA), “Juros”(EEQ\_JUROS) estarão disponíveis para edição. Informe os valores nestes campos observando as seguintes restrições do sistema:  
Se o valor informado em qualquer destes três campos faça com que a somatória dos decréscimos e descontos se iguale ou exceda valor original da parcela acrescida dos acréscimos, multa e juros, o sistema não permite editar o último campo com o valor que originou a invalidação.  
O sistema não permite informar valores negativos nestes campos.  
4. Ao finalizar a informação nos campos clique no botão “Salvar”. Verifique no browser de parcelas que os valores da parcela liquidada foram atualizados (“Vl.Fech.Camb”, “Desconto”, “Multa” e “Juros”).  
5. Confira os dados e confirme. Neste momento o sistema irá enviar os dados para baixa do título no módulo financeiro.  
Verificando os valores no módulo SIGAFIN - Financeiro:  
6. No módulo financeiro (SIGAFIN), caso a parcela liquidada seja de um câmbio a receber, acesse Atualizações / Consultas / Contas a Receber / Posição de Títulos a Receber.  
7. Posicione sobre o título referente à parcela de câmbio liquidada e clique no botão consulta.  
8. O sistema exibirá as movimentações de descontos, juros e multas acerca da baixa efetuada no título do SIGAFIN conforme informado na liquidação do câmbio do SIGAEEC.  
9. Caso a parcela de câmbio liquidada tenha sido uma parcela de câmbio a pagar, acesse Atualizações / Consultas / Contas a Pagar / Posição de Títulos a Pagar.  
10. Posicione sobre o título referente à parcela de câmbio liquidada e clique no botão consulta.  
11. O sistema exibirá as movimentações de descontos, juros e multas acerca da baixa efetuada no título do SIGAFIN conforme informado na liquidação do câmbio do SIGAEEC.
