---
article_id: 360051864793
category: RH - Férias
content_hash: c432dcb9db0751dc23e96927bf1c226b305dd19876c78d6c2b633e1d34cacb6f
fetched_at: '2026-06-28T22:43:59.228530+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema exibe matrículas conforme Filial da matrícula
  posicionada no browse da rotina de cálculo de Férias ao imprimir o Recibo de Férias
type: support-article
updated_at: '2025-09-04T17:59:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051864793-RH-Linha-Protheus-GPE-Sistema-exibe-matr%C3%ADculas-conforme-Filial-da-matr%C3%ADcula-posicionada-no-browse-da-rotina-de-c%C3%A1lculo-de-F%C3%A9rias-ao-imprimir-o-Recibo-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31725736634007)Tempo aproximado para leitura: 00:01:00 min**  
**Dúvida**Sistema exibe matrículas conforme Filial da matrícula posicionada no *browse* da rotina de cálculo de Férias ao imprimir o Recibo de Férias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para a correção deste incidente trocamos a **Consulta Padrão do pergunte Matrícula De/Até** do grupo de perguntas utilizado no relatório de Recibo de Férias.  
  
Para realizar o ajuste manual, é necessário alterar a consulta padrão via Configurador (SIGACFG):  
  
**1 -** Acesse: **Configurador > Base de Dados > Dicionário > Base de Dados,** e no menu à esquerda, seleciona a Empresa clicando no ícone '![](https://centraldeatendimento.totvs.com/hc/article_attachments/31725762103191)' e depois escolha a opção **Perguntas:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31725762104599)  
  
  
**2 -** Na barra superior selecionar o ícone de **Pesquisa:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31725736646551)

**3 -** Procure por **GPR130** e clique em **Buscar:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31725736649751)**  
  
**4 -** Selecione o ícone de **editar:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31725736653719)  
  
  
  
**5 -** Localize as perguntas **Matrícula De?** e **Matrícula Até?**, e na coluna **Consulta Padrão (edit)** pressione duas vezes e selecione a opção **SRA02 - Funcionários** para ambas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31725736657175)

**6 -** Ao finalizar, confirme as alterações através do botão **Confirmar:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31725762117015)

**Saiba Mais:**[RH - Linha Protheus - GPE - Emissão de aviso e recibo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4810789551639-RH-Linha-Protheus-GPE-Emiss%C3%A3o-de-aviso-e-recibo-de-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Como alterar a data de pagamento das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063518933-RH-Linha-Protheus-GPE-Como-alterar-a-data-de-pagamento-das-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Impressão do recibo de férias apresenta nome diferente do cadastro Nome.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6334557879447-RH-Linha-Protheus-GPE-Impress%C3%A3o-do-recibo-de-f%C3%A9rias-apresenta-nome-diferente-do-cadastro-Nome)  
[RH - Linha Protheus - GPE - Aviso de férias apresenta menos de 30 dias para concessão das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000523122-RH-Linha-Protheus-GPE-Aviso-de-f%C3%A9rias-apresenta-menos-de-30-dias-para-concess%C3%A3o-das-f%C3%A9rias)
