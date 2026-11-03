---
content_hash: 45964c101e7d3e9f0eb53596796c196d613bce6ef50bb33d47fb1f33f110bc77
fetched_at: '2026-06-29T00:10:46.946589+00:00'
page_id: '556394443'
product: rm
source: tdn-rm
title: Enviar relatório no corpo do e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556394443
version: 67
---

## **ÍNDICE**

1. **Visão Geral**
2. **Geração e Exportação do relatório**
3. **Identificando o XML do Processo**
4. **Inserindo as atividades na Fórmula Visual**  
   1. **Atividade "Preparar Execução do Processo"**
   2. **Atividade "Executar Processo"**
   3. **Atividade "Executar Consulta SQL"**
   4. **Atividade "Enviar E-mail"**
5. **Alterações para clientes Oracle**
   1. **Atividade "Executar Consulta SQL"**
   2. **Atividade "Executar Código"**
   3. **Atividade "Enviar E-mail"**

**01. VISÃO GERAL**

Neste documento será apresentado uma Fórmula Visual que envia um relatório do Reports diretamente no corpo do e-mail em formato HTML.

**02. GERAÇÃO E EXPORTAÇÃO DO RELATÓRIO**

* Exporte o relatório que será enviado na Fórmula Visual com o formato HTML:

 

**03. IDENTIFICANDO O XML DO PROCESSO**

* Acesse o Gerenciamento de Jobs e copie o XML do processo.

**04. INSERINDO AS ATIVIDADES NA FÓRMULA VISUAL**

### **Atividade "Preparar Execução do Processo"**

* Insira a atividade "Preparar Execução do Processo"
  + Nome do Processo: Gerar Relatório
  + XML dos Parâmetros: Cole o XML gerado anteriormente

### **Atividade "Executar Processo"**

* Insira a atividade "Executar Processo"
  + Atividade de Preparar Parâmetros: selecione a atividade criada no passo anterior
  + Nome do Processo: Gerar Relatório

### **Atividade "Executar Consulta SQL"**

* Insira a atividade "Executar Consulta SQL"
  + Crie uma nova consulta SQL com o conteúdo abaixo:

SELECT IDREL, IDJOBLOG,  
           CONVERT(VARCHAR(MAX), CONVERT(VARBINARY(MAX), RELATORIO)) AS RELATORIO  
FROM GRELBATCH  
WHERE IDJOBLOG = (SELECT Max(IDJOBLOG)  
                                   FROM GRELBATCH)

### **Atividade "Enviar E-mail"**

* Insira a atividade "Enviar E-mail"
  + Anexar Arquivo: faça a ligação com a consulta SQL, conforme print abaixo
  + Assunto: Informe um assunto
  + Destinatários: informe um ou mais destinatários
  + Remetente: escolha um remetente
  + Nome do arquivo anexo: Informe um nome para o anexo
  + Texto do E-mail: faça a ligação com a consulta SQL, conforme print abaixo
  + Texto HTML: True

Em caso de dúvidas na atividade Enviar E-mail, consulte a documentação 

**05. ALTERAÇÕES PARA CLIENTES ORACLE**

Para clientes com bases de dados Oracle, será necessário as alterações nas atividades abaixo:

### **Atividade "Executar Consulta SQL"**

* Insira a atividade "Executar Consulta SQL"
  + Crie uma nova consulta SQL com o conteúdo abaixo:

SELECT IDREL,  
             IDJOBLOG,  
             RELATORIO  
FROM GRELBATCH  
WHERE IDJOBLOG = (SELECT Max(IDJOBLOG)  
                                  FROM GRELBATCH)

### **Atividade "Executar Código"**

* Insira a atividade "Executar Código"
  + ExecuteCode:

var bytes = this.rmsConsSQLActivity1.DataSet.Tables["Resultado"].Rows[0]["RELATORIO"] as byte[];  
this.rmsSendEmailActivity1.Body = Encoding.UTF8.GetString(bytes, 0, bytes.Length);

### **Atividade "Enviar E-mail"**

* Insira a atividade "Enviar E-mail"
  + Anexar Arquivo: faça a ligação com a consulta SQL, conforme print abaixo
  + Assunto: Informe um assunto
  + Destinatários: informe um ou mais destinatários
  + Nome do arquivo anexo: Informe um nome para o anexo
  + Remetente: escolha um remetente
  + Texto do E-mail: ""
  + Texto HTML: True

Em caso de dúvidas na atividade Enviar E-mail, consulte a documentação 

## Artigos relacionados

Os artigos relacionados aparecem aqui baseados nos rótulos que você selecionar. Clique para editar a macro e adicionar ou alterar os rótulos.

false5LRMfalsemodifiedtruepagelabel = "kb-how-to-article" and type = "page" and space = "LRM"kb-how-to-article

true

|  |  |
| --- | --- |
| Ocorrências relacionadas |  |
