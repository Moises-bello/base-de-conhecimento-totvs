---
article_id: 360052970874
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 46e31432772b915b837c1ef5e5ce5f80f9d483511769b950d3968edd4150491f
fetched_at: '2026-06-28T22:39:44.412403+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Quebra parcela
  no Controle Câmbio
type: support-article
updated_at: '2022-06-01T21:06:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052970874-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Quebra-parcela-no-Controle-C%C3%A2mbio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar a quebra do valor da parcela na rotina de Controle de Câmbio?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Export Control – Todas versões.  
  
**Solução**O módulo SIGAEIC, não realiza a geração de um novo título quando modificado o valor da parcela, sendo assim, o procedimento é realizado conforme abaixo:  
1. Acesse o módulo SIGAEIC em Atualizações \ Financeiro \ Controle cambio (EICAP100);  
2. Posicione no processo de desembaraço e selecione Alterar;  
3. Posicione na parcela e selecione Outras Ações \ Alteração  
4. Selecione o campo Valor Moeda (WB\_FOBMOE) e modifique para o valor da parcela que deseja alterar, após selecione Salvar :  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088582653/mceclip0.png)  
5. Verifique que a parcela terá o valor atualizado:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088583073/mceclip1.png)  
6. Verifique que para o saldo restante da parcela será necessário a inclusão de uma nova parcela, sendo assim, selecione Outras Ações \ Inclusão.  
7. Informe os dados referente: Cod.Evento, Invoice, Tipo Reg, Vencimento e Valor Moeda, após selecione o Salvar:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087444394/mceclip3.png)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088585773/mceclip2.png)  
8. Verifique que será criado uma nova linha referente a parcela, após selecione o Salvar:   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087444494/mceclip4.png)  
9. No SIGAFIN, rotina do contas a pagar (FINA050), será mantido a primeira parcela porém com o valor atualizado e criado uma nova parcela referente a quebra do valor:   
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087444634/mceclip5.png)  
10. Na rotina de Controle Cambio (EICAP100), é possível verificar na linha da parcela o numero do título, através do campo Nro.Titulo:   
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088586313/mceclip6.png)
