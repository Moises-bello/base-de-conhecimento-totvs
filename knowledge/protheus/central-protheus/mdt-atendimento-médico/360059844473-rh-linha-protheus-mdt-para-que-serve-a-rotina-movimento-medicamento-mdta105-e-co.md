---
article_id: 360059844473
category: MDT - Atendimento Médico
content_hash: 6573f31f9f6ec21298512558a9616265c987514713429ada626f0d7d6d2c7a2f
fetched_at: '2026-06-28T22:44:21.427642+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Para que serve a rotina Movimento Medicamento (MDTA105)
  e como incluir
type: support-article
updated_at: '2025-07-29T16:59:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059844473-RH-Linha-Protheus-MDT-Para-que-serve-a-rotina-Movimento-Medicamento-MDTA105-e-como-incluir
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25285998370327)**Tempo aproximado para leitura:**00:02:00** min

**Dúvida**Para que serve a rotina Movimento Medicamento (MDTA105) e como incluir?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Esta rotina permite registrar a **movimentação de medicamentos** no estoque da farmácia do ambulatório.

Para saber como cadastrar um Medicamento consulte a documentação abaixo.  
[MP - MDT - Para que serve a rotina Medicamentos (MDTA010) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059843533)  
  
O Código que identifica a movimentação campo que será realizada no estoque da farmácia **"Cod. Movto" (TM3\_INDMOV)** . Podendo ser:

**1 - Entrada Inventário:** este movimento irá gravar a quantidade informada, como sendo a quantidade de inventário e também a quantidade atual no estoque. Será desconsiderado tudo o que existia antes em estoque.  
**2 - Entrada Compra:** irá somar a quantidade informada no saldo atual em estoque.  
**3 - Entrada Devolução:** irá somar a quantidade informada no saldo atual em estoque.  
**4 - Entrada Ajuste:** irá somar a quantidade informada no saldo atual em estoque.  
**5 - Saída Utilização:** este movimento é gerado automaticamente pelo programa de atendimento médico, quando o médico registra um medicamentos para um paciente. Ele subtrai do saldo a quantidade informada. Este movimento não pode ser excluído através deste programa.  
**6 - Saída Validade:** irá subtrair a quantidade informada do saldo em estoque.  
**7 - Saída Ajuste:** irá subtrair a quantidade informada do saldo em estoque.

O usuário indica se deseja controlar ou não o estoque do medicamentos.  
  
Para os medicamentos assinalados como controle de estoque, a cada registro de medicamentos para o paciente, feito pelo médico, o sistema irá atualizar o saldo, gerando uma saída do medicamentos. Observando sempre que a unidade de medida dos medicamentos deverá ser a mesma informada pelo médico no momento do atendimento.  
  
Para incluir um movimento de medicamentos acesse o Módulo 35 (SIGAMDT), no seguinte caminho: Atualizações - Medicamentos - Movimento Medicamentos.  
  
**1**. Na janela de Movto Medicamentos, selecione a opção "Incluir".  
**2**. Preencha os campos conforme orientação do help de campo. Observe porém o preenchimento do seguinte campo:  
**3**. Confira os dados e confirme a inclusão.  
  
![SUlEvXPHPM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098367754)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20%20)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
