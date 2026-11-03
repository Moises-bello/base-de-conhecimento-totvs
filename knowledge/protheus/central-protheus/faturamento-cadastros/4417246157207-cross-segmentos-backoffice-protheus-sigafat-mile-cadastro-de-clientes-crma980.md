---
article_id: 4417246157207
category: Faturamento - Cadastros
content_hash: 2e6ef17e7021dcb3a772d8a5463fd1f7e2230d641322190a46f8ad57701cc116
fetched_at: '2026-06-28T22:38:36.808249+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - MILE Cadastro de Clientes
  - CRMA980
type: support-article
updated_at: '2024-12-13T19:45:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417246157207-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-MILE-Cadastro-de-Clientes-CRMA980
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28514228032663) Tempo aproximado para leitura: **00**:**01:00 min** **Dúvida**

Como realizar a importação do Cadastro de Clientes através do MILE?   
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - todas releases;

**Solução**  
Com a descontinuação do fonte MATA030 o cadastro do MILE é chamado através do Cadastro de Clientes - CRMA980, segue a configuração para a importação através do MILE.

Importante: Para realizar o procedimento é necessário, realizar o login com o usuário Administrador ou um usuário que tenha permissão de acesso ao "SIGACFG".

1- Acessar o Configurador(SIGACFG) Ir em Ambiente >> Aceleradores >> Mile >> Layouts;

2- Clicar em Incluir "Importação".

Realizar o preenchimento dos dados de acordo com o Print abaixo.

Aba Geral

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28514235959319)

Aba Formação do Arquivo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28514235960855)

Aba Dados do Canal;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28514228043287)

Aba Campos

Preencher os campos, obrigatórios do cadastro do Clientes.

3- Abrir um Bloco de Notas e realizar a inclusão dos campos definidos na Aba campos de acordo com a sequencia e o separados definido "Ponto e Virgula ou PIPE".

000031|01|CADASTRO PELO MILE|MILE CRMA980|F|AV BRAS LEME 1000|SP|SAO PAULO|0000000001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28514235963927)

4- Acessar a rotina de Cadastro de Clientes - CRMA980, ir em outras ações Outros >> Importar, selecionar o arquivo .TXT gravado e realizar a Importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28514235966487)

5- Tela de Processamento para informar se foi concluído com sucesso ou apresentou algum incidente na importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28514235968151)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28514235969559)

**Saiba mais**:  
[Configuração Mile para o Módulo Faturamento](https://tdn.totvs.com/x/-jQrI)

[Mile Importação e Exportação do Layout](https://tdn.totvs.com/x/KrJEGQ)
