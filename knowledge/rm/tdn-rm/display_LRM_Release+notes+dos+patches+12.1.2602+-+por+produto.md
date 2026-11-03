---
content_hash: 2dccdbf62d171308311d6632be76a7301655c5e8796f7df834ff3d13bfdb5cfd
fetched_at: '2026-06-29T00:05:50.387808+00:00'
page_id: '1043708019'
product: rm
source: tdn-rm
title: Release notes dos patches 12.1.2602 - por produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Release+notes+dos+patches+12.1.2602+-+por+produto
version: 88
---

|  |
| --- |
| Esses são todos os patches gerados, porém nem todos estão disponíveis para todos os clientes. |

---

  
  

1square

---

  
  

# IA RM

## 12.1.2602.110

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-89]** Mudanca no ECD para nova versão

Arquivos: RM.IA.Backoffice.Service.dll; RM.IA.OCR.Lib.Service.dll; RM.IA.Backoffice.IService.dll

## 12.1.2602.113

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-89]** Mudanca no ECD para nova versão

Arquivo: RM.IA.Backoffice.Service.dll

## 12.1.2602.127

### Rotina: BASE ACELERADORA

* **[Ticket: RMARQIA-226]** Otimização do processo de cópia de dados fiscais para possibilitar o Cadastro de caminhos de arquivos fiscais e contábeis

Arquivos: RM.IA.Backoffice.Service.dll; RM.IA.OCR.Lib.Service.dll

## 12.1.2602.129

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-234]** Validação na importação de dados XML de notas no que tange ao cadastro de transportadoras e ao código auto-incrementado

Arquivo: RM.IA.Backoffice.Service.dll

* **[Ticket: RMARQIA-234]** Validação na importação de dados XML de notas no que tange ao cadastro de transportadoras

Arquivo: RM.IA.Backoffice.Service.dll

## 12.1.2602.130

### Rotina: BASE ACELERADORA

* **[Ticket: RMARQIA-227]** - Adicionada mensagem para acompanhamento do processo de Cópia de dados arquivos fiscais, contábeis e aceleradores;- Adicionada validação do tamanho do campo do Nome da transpotadora;- Recuperar o CNPJ da coligada destino;

Arquivos: RM.IA.Backoffice.IService.dll; RM.Glb.Processos.Server.dll; RM.IA.Backoffice.Service.dll

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-235]** Otimização da exibição do nome do fornecedor no log da Cópia de dados arquivos fiscais, contábeis e aceleradores;

Arquivo: RM.IA.Backoffice.Service.dll

* **[Ticket: RMARQIA-319]** Melhorar a mensagem de log de erros ao final do processo de cópia de dados de arquivos fiscais e contábeis

Arquivo: RM.IA.Backoffice.Service.dll

## 12.1.2602.131

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-318]** Otimização da inserção de filiais de tal maneira que o código seja gerado sequencialmente sem janelas

Arquivo: RM.IA.Backoffice.Service.dll

* **[Ticket: RMARQIA-319]** Otimização do cadastro de fornecedores no processo de cópia de dados fiscais e contábeis: os dados de inscrição estadual, email e complementeo do endereço eram copiados da Filial.

Arquivos: RM.IA.Backoffice.Service.dll; RM.IA.Backoffice.IService.dll

* **[Ticket: RMARQIA-320]** Sanitizar os campos de endereço do cliente fornecedor Rua e Bairro no processo de cópia de dados fiscais e contábeis

Arquivo: RM.IA.Backoffice.Service.dll

* **[Ticket: RMARQIA-340]** Otimização no expurgo de registros da Filial no processo de cópia de dados fiscais e contábeis

Arquivo: RM.IA.Backoffice.Service.dll

## 12.1.2602.132

### Rotina: BASE ACELERADORA

* **[Ticket: RMARQIA-322]** Otimização da cópia do endereço (NUMERO e COMPLEMENTO) da Filial no processo de Cópia de dados fiscais e contábeis

Arquivo: RM.IA.Backoffice.Service.dll

* **[Ticket: RMARQIA-322]** Otimização da cópia do endereço da Filial no processo de Cópia de dados fiscais e contábeis

Arquivo: RM.IA.Backoffice.Service.dll

## 12.1.2602.142

### Rotina: GESTÃO DE PROJETOS

* **[Ticket: RMARQIA-416]** Atualização dos recursos avançados do Classification

Arquivo: Eng/dta-vision-rm-front

## 12.1.2602.143

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-335]** Descida para versão 2602 embedado o XSLT

Arquivo: RM.IA.OCR.Lib.Service.dll

## 12.1.2602.151

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-496]** Removacao de informações inrelevantes sobre a nota

Arquivo: RM.IA.Backoffice.Service.dll

## 12.1.2602.166

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-496]** Atualização para passar as notas sem error

Arquivo: RM.IA.OCR.Lib.Service.dll

## 12.1.2602.167

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-496]** Atualização do ECD usando a data que vem do sped

Arquivo: RM.IA.Backoffice.Service.dll

## 12.1.2602.173

### Rotina: INTEGRAÇÃO COM GIT

* **[Ticket: RMARQIA-45]** Criação de estrutura básica para montagem de ambiente de desenvolvimento

Arquivo: Eng/dta-vision-rm-front

# Outros

## 12.1.2602.110

### Rotina: ALTA

* **[Ticket: DSAUGHASSIST-21621]** Inclusão do Número da declaração de óbito na alta

Arquivo: RM.Lib.Params.Wizard.xml

### Rotina: REGISTRO E CONTROLE

* **[Ticket: DSAUGHASSIST-21814]** Correção Ids repetidos

Arquivo: RM.Lib.Params.Wizard.xml

## 12.1.2602.125

### Rotina: OAUTH

* **[Ticket: DFRWFOUNDATION-29246]** Bibliotecas utilizadas para login com OIDC e contingência TOTP

Arquivos: Microsoft.IdentityModel.Protocols.dll; Otp.NET.dll; Microsoft.IdentityModel.Protocols.OpenIdConnect.dll

# TOTVS Worknow

## 12.1.2602.100

### Rotina: Plataforma A

* **[Ticket: WN-37567]** Ajuste na integraÃ§Ã£o de Coordenadores e Professores.

Arquivo: Wnw/worknow

* **[Ticket: WN-37853]** Ajuste para nÃ£o criar o campo PAMASTER com valor fixo.

Arquivo: Wnw/worknow

* **[Ticket: WN-37988]** Ajuste para integraÃ§Ã£o correta de professores.

Arquivo: Wnw/worknow

### Rotina: Portal e-commerce

* **[Ticket: WN-37858]** Ajuste em Consulta SQL para validaÃ§Ã£o da Data de Vencimento FlexÃ­vel Base SQL e Oracle

Arquivo: Wnw/worknow

### Rotina: Prova Facil

* **[Ticket: WN-35434]** Ajuste em atividades , criaÃ§Ã£o de atividades complementares

Arquivo: Wnw/worknow

### Rotina: Canvas

* **[Ticket: WN-36894]** Ajuste para integraÃ§Ã£o correta de notas do tipo Conceito.

Arquivo: Wnw/worknow

* **[Ticket: WN-37416]** Ajuste no integrador Canvas para correta execuÃ§Ã£o em base de dados Oracle.

Arquivo: Wnw/worknow

### Rotina: EAD Plataforma

* **[Ticket: WN-36444]** Ajuste na integraÃ§Ã£o de notas para cursos de GraduaÃ§Ã£o.

Arquivo: Wnw/worknow

### Rotina: Sem Rotina Específica

* Erro ao abrir parÃ¢metros do Workchat no em bases Oracle no ambiente da Totvs.

Arquivo: Wnw/worknow

### Rotina: BlackBoard

* **[Ticket: WN-36894]** Melhoria na chamada da API Blackboard para nÃ£o ocorrer Rate Limit 429.

Arquivo: Wnw/worknow

### Rotina: Eskolare

* **[Ticket: WN-37859]** Melhoria para utilizaÃ§Ã£o de resgate unitÃ¡rio na parte financeira.

Arquivo: Wnw/worknow

## 12.1.2602.101

### Rotina: Portal

* **[Ticket: WN-243]** Portal Geral

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-37947]** Melhoria no integrador Moodle para funcionar corretamente em base de dados Oracle.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-38152]** Melhoria no integrador para execuÃ§Ã£o correta no mÃ³dulo GestÃ£o de Estoque, Compras e Faturamento.

Arquivo: Wnw/worknow

## 12.1.2602.102

### Rotina: Ecommerce

* **[Ticket: WN-38405]** Ajuste no processo de remoÃ§Ã£o de itens duplicados.

Arquivo: Wnw/worknow

## 12.1.2602.103

### Rotina: WorkChat

* **[Ticket: WN-38401]** Melhoria na passagem de arquivo para a FÃ³rmula Visual tambÃ©m no formato Bytes.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-35434]** Ajute em execuÃ§Ã£o fv aba custom

Arquivo: Wnw/worknow

## 12.1.2602.104

### Rotina: Canvas

* **[Ticket: WN-37356]** InclusÃ£o de um novo parÃ¢metro para NÃ£o enviar data de inicio e fim na integraÃ§Ã£o de SeÃ§Ãµes.

Arquivo: Wnw/worknow

## 12.1.2602.105

### Rotina: Geral

* **[Ticket: WN-38506]** Ajuste em funÃ§Ã£o oracle Remove\_Caracteres\_Especiais

Arquivo: Wnw/worknow

## 12.1.2602.107

### Rotina: WorkChat

* **[Ticket: WN-38062]** MigraÃ§Ã£o da integraÃ§Ã£o para Webhook.

Arquivo: Wnw/worknow

## 12.1.2602.108

### Rotina: Canvas

* **[Ticket: WN-38485]** Ajuste no processo de integraÃ§Ã£o de Alunos, para inclusÃ£o e remoÃ§Ã£o correta em Subturmas.

Arquivo: Wnw/worknow

## 12.1.2602.109

### Rotina: D2L

* **[Ticket: WN-38186]** Ajuste para nÃ£o ocorrer remoÃ§Ã£o indevida de alunos.

Arquivo: Wnw/worknow

### Rotina: Plataforma A

* **[Ticket: WN-38286]** Melhoria no integrador para validar a seleÃ§Ã£o de data inicio e fim de inclusÃ£o do professor.

Arquivo: Wnw/worknow

### Rotina: WorkIA

* **[Ticket: WN-]** Melhoria na gravaÃ§Ã£o dos logs, inclusÃ£o de novas informaÃ§Ãµes para monitoramento.

Arquivo: Wnw/worknow

## 12.1.2602.110

### Rotina: Sem Rotina Específica

* **[Ticket: WN-38175]** [Rotina:] Desfazendo aba de campos customizados do Moodle.

Arquivo: Wnw/worknow

* **[Ticket: WN-232]** [Rotina:] Ajustando nÃºmero de telefone na Conversa Livre e outras melhorias.

Arquivo: Wnw/worknow

### Rotina: Plataforma A

* **[Ticket: WN-38697]** Ajuste no processo de exclusÃ£o de vÃ­nculo de professor em base de dados Oracle.

Arquivo: Wnw/worknow

### Rotina: BlackBoard

* **[Ticket: WN-38699]** Ajuste para realizar a ativaÃ§Ã£o de professores no processo de integraÃ§Ã£o.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-232]** Melhorias na utilizaÃ§Ã£o de multi-assistentes utilizando inteligÃªncia artificial.

Arquivo: Wnw/worknow

## 12.1.2602.111

### Rotina: Ãbaris

* **[Ticket: WN-36993]** InclusÃ£o das atividades complementares no histÃ³rico escolar digital.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-38793]** Melhorias de estabilidade e compatibilidade de dados na integraÃ§Ã£o de professores.

Arquivo: Wnw/worknow

### Rotina: Teams

* **[Ticket: WN-38657]** Melhoria no processo de arquivamento de equipes.

Arquivo: Wnw/worknow

### Rotina: BlackBoard

* **[Ticket: WN-38741]** Melhoria nos Logs nos processos de integraÃ§Ã£o e inclusÃ£o de validaÃ§Ã£o do tempo de vida do Token.

Arquivo: Wnw/worknow

## 12.1.2602.112

### Rotina: BlackBoard

* **[Ticket: WN-38837]** Melhoria no processo de ValidaÃ§Ã£o do Token e nos Logs de execuÃ§Ã£o de Processo.

Arquivo: Wnw/worknow

### Rotina: Sem Rotina Específica

* **[Ticket: WN-36687]** [Rotina:] Ajustes nos fontes do ecommerce serviÃ§o.

Arquivo: Wnw/worknow

## 12.1.2602.113

### Rotina: Moodle

* **[Ticket: WN-38698]** Ajuste no integrador para execuÃ§Ã£o correta em base de dados Oracle.

Arquivo: Wnw/worknow

### Rotina: Ecommerce

* **[Ticket: WN-36687]** Ajuste no preenchimento da data de competÃªncia das parcelas no processo de matrÃ­cula.

Arquivo: Wnw/worknow

### Rotina: Portal

* **[Ticket: WN-423]** Melhoria portal aluno

Arquivo: Wnw/worknow

### Rotina: BlackBoard

* **[Ticket: WN-38741]** Ajuste na validaÃ§Ã£o do Token.

Arquivo: Wnw/worknow

### Rotina: Plataforma A

* **[Ticket: WN-38173]** Ajuste no processo de suspensÃ£o de Alunos.

Arquivo: Wnw/worknow

## 12.1.2602.114

### Rotina: Blackboard

* **[Ticket: WN-38838]** Melhoria no processo de integraÃ§Ã£o de Alunos.

Arquivo: Wnw/worknow

### Rotina: Isaac

* **[Ticket: WN-38960]** Melhoria no proceso de limpeza da tabela de logs.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-39225 ]** Ajuste na funÃ§Ã£o Remove Caracteres Especiais nas consultas SQL para base de dados Oracle.

Arquivo: Wnw/worknow

* **[Ticket: WN-39197]** Ajuste no processo de integraÃ§Ã£o de professores para validaÃ§Ã£o correta das datas.

Arquivo: Wnw/worknow

* **[Ticket: WN-37630]** MudanÃ§a na interface de cursos, para aceitar o tamanho de upload em Megabytes.

Arquivo: Wnw/worknow

### Rotina: BlackBoard

* **[Ticket: WN-38984]** Melhoria na integraÃ§Ã£o de cursos

Arquivo: Wnw/worknow

## 12.1.2602.115

### Rotina: Portal

* **[Ticket: WN-38934 ]** Melhoria nos menus de portal

Arquivo: Wnw/worknow

### Rotina: Sem Rotina Específica

* Moodle - InclusÃ£o do campo complementar STURMADISCCOMPL.CODTURMADISC

Arquivo: Wnw/worknow

## 12.1.2602.116

### Rotina: Isaac

* **[Ticket: WN-38635]** Envio do valor original com o desconto permanente jÃ¡ aplicado.

Arquivo: Wnw/worknow

## 12.1.2602.117

### Rotina: Portal

* **[Ticket: WN-38934]** Melhoria mensagens de erro portal disciplinas

Arquivo: Wnw/worknow

### Rotina: Ãbaris

* **[Ticket: WN-39424]** InclusÃ£o da situaÃ§Ã£o de matricula no histÃ³rico digital.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-39413]** Ajuste para nÃ£o duplicar o ID do Curso ao selecionar a opÃ§Ã£o de concatenaÃ§Ã£o Turma Disciplina Compl.

Arquivo: Wnw/worknow

## 12.1.2602.119

### Rotina: Ãbaris

* **[Ticket: WN-38269]** Ajuste na validaÃ§Ã£o de licenÃ§a no envio de contrato para o Ãbaris.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-39510]** Ajuste no processo de integraÃ§Ã£o de aluno para integraÃ§Ã£o correta com Base de dados Oracle.

Arquivo: Wnw/worknow

## 12.1.2602.121

### Rotina: Blackboard

* **[Ticket: WN-38984]** CriaÃ§Ã£o de controle de identificador interno

Arquivo: Wnw/worknow

## 12.1.2602.122

### Rotina: Eskolare

* **[Ticket: WN-37859]** Melhoria na integraÃ§Ã£o de resgates e transaÃ§Ãµes financeiras.

Arquivo: Wnw/worknow

## 12.1.2602.123

### Rotina: Ãbaris

* **[Ticket: WN-39582]** InclusÃ£o da habilitaÃ§Ã£o na consulta de dados gerais.

Arquivo: Wnw/worknow

## 12.1.2602.124

### Rotina: Canvas

* **[Ticket: WN-39605]** Ajuste no processo de integraÃ§Ã£o de Subcontas, para montagem correta da consulta SQL.

Arquivo: Wnw/worknow

## 12.1.2602.125

### Rotina: Plataforma A

* **[Ticket: WN-39516]** Ajuste no processo de exclusÃ£o de turma/disciplina no Manager, evitando o travamento da fila quando o registro nÃ£o existir mais.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-39746]** Ajuste no processo de manutenÃ§Ã£o de Alunos e Professores, para nÃ£o ocorrer exclusÃµes indevidas.

Arquivo: Wnw/worknow

* **[Ticket: WN-39881]** Ajuste na consulta SQL para integraÃ§Ã£o correta de Grupos.

Arquivo: Wnw/worknow

* **[Ticket: WN-39570]** Ajuste na montagem da consulta SQL para execuÃ§Ã£o de Cohort.

Arquivo: Wnw/worknow

* **[Ticket: WN-39786]** Ajuste na busca de Alunos no Moodle para funcionar corretamente com as opÃ§Ãµes IdNumber e UserName.

Arquivo: Wnw/worknow

### Rotina: Ecommerce

* **[Ticket: WN- 39460]** Ajuste na rotina de pagamento com gateway TPC, e correÃ§Ã£o na listagem de boletos do Ecommerce (base Oracle)

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste em rotina de inclusÃ£o/remoÃ§Ã£o unitaria de usuarios

Arquivo: Wnw/worknow

### Rotina: D2L

* **[Ticket: WN-39797]** D2L - Ajuste em rotina de coordenadores , erro de filtro e controle de senha office 365

Arquivo: Wnw/worknow

### Rotina: Isaac

* **[Ticket: WN-38634]** ImplentaÃ§Ã£o da opÃ§Ã£o de pagamento como Garantidora.

Arquivo: Wnw/worknow

## 12.1.2602.127

### Rotina: Sem Rotina Específica

* [40102] Blackboard - Ajuste de grid, ajuste de codigo e descriÃ§Ã£o do campo modalidade e inclusÃ£o de opÃ§Ã£o Nivel/Categoria;

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-39940]** Ajuste na montagem da consulta SQL no processo de integraÃ§Ã£o de Professores.

Arquivo: Wnw/worknow

### Rotina: WorkIA

* **[Ticket: WN-39821]** Melhorias na integraÃ§Ã£o via chatbot com a Rubeus IA.

Arquivo: Wnw/worknow

## 12.1.2602.129

### Rotina: Moodle

* **[Ticket: WN-39940]** Ajuste na montagem de consulta para integraÃ§Ã£o correta de professores quando utilizado agrupamento por Subturma.

Arquivo: Wnw/worknow

* **[Ticket: WN-39910]** Ajuste na criaÃ§Ã£o da PK no processo de integraÃ§Ã£o de Grupos, quando Ã© baseada em Subturmas.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-36169]** Melhoria nas consistÃªncias da interface de envio de mensagens.

Arquivo: Wnw/worknow

### Rotina: Isaac

* **[Ticket: WN-38073]** Envio do perÃ­odo acadÃªmico em ciclos letivos semestrais ou anual.

Arquivo: Wnw/worknow

## 12.1.2602.130

### Rotina: Moodle

* **[Ticket: WN-39820]** Ajuste no processo de integraÃ§Ã£o de Alunos, para nÃ£o integrar o mesmo aluno mais de uma vez.

Arquivo: Wnw/worknow

### Rotina: Canvas

* **[Ticket: WN-40010]** Ajuste no processo de integraÃ§Ã£o unitÃ¡ria de Coordenadores.

Arquivo: Wnw/worknow

* **[Ticket: WN-37608]** Ajuste na integraÃ§Ã£o e atualizaÃ§Ã£o de Cursos quando o campo SQL de SubstituiÃ§Ã£o de Dados estÃ¡ sendo utilizado.

Arquivo: Wnw/worknow

### Rotina: GETNET

* **[Ticket: WN-21415]** Melhorias na conciliaÃ§Ã£o de cartÃ£o de crÃ©dito via GETNET.

Arquivo: Wnw/worknow

## 12.1.2602.131

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste controle id rotinas alunos, professores ,vinculos master e notas

Arquivo: Wnw/worknow

* **[Ticket: WN-38984]** Ajuste vinculo Professor

Arquivo: Wnw/worknow

* **[Ticket: WN-38984]** Ajuste matricula aluno

Arquivo: Wnw/worknow

### Rotina: MS Teams

* **[Ticket: WN-39579]** Ajuste na integraÃ§Ã£o de alunos, para ocorrer corretamente quando a Equipe estÃ¡ configurada por Turmas.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste rotina remoÃ§Ã£o vinculo aluno e professores

Arquivo: Wnw/worknow

### Rotina: WorkIA

* **[Ticket: WN-40375]** Melhoria no cadastro de contatos e eventos no Rubeus IA.

Arquivo: Wnw/worknow

## 12.1.2602.132

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste vinculo professor

Arquivo: Wnw/worknow

* **[Ticket: WN-38984]** Ajuste rotina matricula alunos - sql oracle

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste em rotina para recuperar clientid

Arquivo: Wnw/worknow

* **[Ticket: WN-38984]** Ajuste rotina matricula aluno, progresso de execuÃ§Ã£o, desempenho de notas

Arquivo: Wnw/worknow

## 12.1.2602.133

### Rotina: Canvas

* **[Ticket: WN-40161]** Ajuste no processo de integraÃ§Ã£o para Base de Dados Oracle.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** AtualizaÃ§Ã£o na classe de notas displayGrade Score para decimal

Arquivo: Wnw/worknow

## 12.1.2602.135

### Rotina: Moodle

* **[Ticket: WN-40504]** Ajuste para criaÃ§Ã£o correta das tabelas de controle em Base de Dados Oracle.

Arquivo: Wnw/worknow

### Rotina: E-commerce

* **[Ticket: WN-40699]** Ajuste no retorno de dados dos Produtos (Base Oracle)

Arquivo: Wnw/worknow

### Rotina: MS Teams

* **[Ticket: WN-39897]** Ajuste para execuÃ§Ãµes de FÃ³rmulas Visuais atravÃ©s do integrador.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-40481]** ImplementaÃ§Ã£o do Contexto Centralizador.

Arquivo: Wnw/worknow

## 12.1.2602.136

### Rotina: Isacc

* **[Ticket: WN-29737]** Melhoria no texto do log de erro durante a baixa de lanÃ§amentos.

Arquivo: Wnw/worknow

### Rotina: Isaac

* **[Ticket: WN-38920]** Melhoria para desconsiderar a taxa extra.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-21477]** Ajuste no processamento de turmas gerenciais e mistas para garantir que alunos de disciplinas vinculadas nÃ£o sejam suspensos incorretamente.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** CriaÃ§Ã£o rotina termos e inclusaÃµ vinculo de Alunos a hierarquia

Arquivo: Wnw/worknow

### Rotina: Plataforma A

* **[Ticket: WN-257]** Ajuste em funÃ§Ã£o GetGrades e parametro de atualiza Notas

Arquivo: Wnw/worknow

## 12.1.2602.137

### Rotina: Ãbaris

* **[Ticket: WN-39424]** InclusÃ£o da opÃ§Ã£o Outra Forma IntegralizaÃ§Ã£o no envio de informaÃ§Ãµes.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** CorreÃ§Ã£o consulta remove professor sem vinculo

Arquivo: Wnw/worknow

* **[Ticket: WN-38984]** Atualiza de notas e vinculo de master

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-39733]** Adicionada regra de suspensÃ£o combinada de alunos (Curso/HabilitaÃ§Ã£o OU Disciplina).

Arquivo: Wnw/worknow

* **[Ticket: WN-40831]** Ajuste no atualizador para criaÃ§Ã£o correta das tabelas em base de dados Oracle.

Arquivo: Wnw/worknow

### Rotina: WorkIA

* **[Ticket: WN-40728]** Melhorias na integraÃ§Ã£o com a Rubeus IA.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-40801]** InclusÃ£o do telefone da requisiÃ§Ã£o nos parÃ¢metros da integraÃ§Ã£o.

Arquivo: Wnw/worknow

### Rotina: BlackBoard

* **[Ticket: WN-39607]** Otimizado o mecanismo de registro de data e hora nas atualizaÃ§Ãµes da integraÃ§Ã£o.

Arquivo: Wnw/worknow

## 12.1.2602.141

### Rotina: Plataforma A

* **[Ticket: WN-40796]** Ajuste no processo de integraÃ§Ã£o de Notas par receber mais de um tipo de gradeCategoryType.

Arquivo: Wnw/worknow

### Rotina: Canvas

* **[Ticket: WN-36894]** Ajuste no processo de integraÃ§Ã£o de notas quando utilizado o nÃ­vel Subturma.

Arquivo: Wnw/worknow

## 12.1.2602.142

### Rotina: Geral

* **[Ticket: WN-39606]** Melhoria no log de integraÃ§Ã£o para informar corretamente a data da Ãºltima execuÃ§Ã£o do processo.

Arquivo: Wnw/worknow

## 12.1.2602.143

### Rotina: Isaac

* **[Ticket: WN-38754]** Melhoria para consumo de status de matricula do aluno.

Arquivo: Wnw/worknow

* **[Ticket: WN-41157]** Melhoria para permitir o cancelamento de parcelas vencidas.

Arquivo: Wnw/worknow

## 12.1.2602.145

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste em rotinas vinculo matricula, notas e matricula

Arquivo: Wnw/worknow

### Rotina: E-Commerce

* **[Ticket: WN-39745]** Ajuste no preenchimento da CompetÃªncia das parcelas conforme plano de pagamento.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-38062]** ImplementaÃ§Ã£o da resposta dos botÃµes da mensagem via webhook.

Arquivo: Wnw/worknow

### Rotina: Plataforma A

* **[Ticket: WN-37568]** InclusÃ£o de um novo papel de Professor, Mediador PedagÃ³gico.

Arquivo: Wnw/worknow

### Rotina: Geral

* **[Ticket: WN-39612]** Melhoria no processo de validaÃ§Ã£o do Codpessoa nas integraÃ§Ãµes.

Arquivo: Wnw/worknow

## 12.1.2602.148

### Rotina: WorkChat

* **[Ticket: WN-41601]** Melhoria no tratamento de checkpoints da Rubeus IA.

Arquivo: Wnw/worknow

## 12.1.2602.149

### Rotina: Geral

* **[Ticket: WN-38093]** Ajuste em execuÃ§Ã£o de fv , envio de user via contexto. InclusÃ£o de rotina de substituiÃ§Ã£o de dados por sql em Plataforma A

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-41502]** Melhoria na importaÃ§Ã£o de contatos.

Arquivo: Wnw/worknow

### Rotina: Isaac

* **[Ticket: WN-41379]** ImplementaÃ§Ã£o do cancelamento de parcela avulsa no lanÃ§amento financeiro.

Arquivo: Wnw/worknow

## 12.1.2602.150

### Rotina: WorkChat

* **[Ticket: WN-41601]** ParÃ¢metro para processamento de checkpoints de forma sÃ­ncrona.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste rotina vinculo aluno e professor

Arquivo: Wnw/worknow

## 12.1.2602.151

### Rotina: Geral

* **[Ticket: WN-38093]** InclusÃ£o codsistema na passagem de execuÃ§Ã£o de formula visual

Arquivo: Wnw/worknow

### Rotina: Isaac

* **[Ticket: WN-41379]** Melhorias no cancelamento de parcela avulsa no lanÃ§amento financeiro.

Arquivo: Wnw/worknow

### Rotina: Ãbaris

* **[Ticket: WN-41372]** Melhorias na geraÃ§Ã£o do diploma e histÃ³rico digital.

Arquivo: Wnw/worknow

## 12.1.2602.152

### Rotina: Canvas

* **[Ticket: WN-41396]** Adicionada uma nova Flag no processo de integraÃ§Ã£o de SeÃ§Ã£o para ValidaÃ§Ã£o de HabilitaÃ§Ã£o.

Arquivo: Wnw/worknow

* **[Ticket: WN-41441]** Adicionada uma flag para permitir definir se a data de vÃ­nculo de alunos serÃ¡ enviada.

Arquivo: Wnw/worknow

* **[Ticket: WN-36894]** Ajuste para integraÃ§Ã£o correta de notas tipo Conceito.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-41601]** Melhoria no tratamento de checkpoints com a RubeusIA.

Arquivo: Wnw/worknow

## 12.1.2602.153

### Rotina: Plataforma A

* **[Ticket: WN-41781]** Ajuste para correta atualizaÃ§Ã£o da SituaÃ§Ãµes da EnturmaÃ§Ã£o.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste rotina inativa e ativa alunos e remoÃ§Ã£o de alunos curso

Arquivo: Wnw/worknow

## 12.1.2602.168

### Rotina: Isaac

* **[Ticket: WN-42340]** Permitir cancelar parcelas parcialmente baixadas.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-42429]** Ajuste na integraÃ§Ã£o de cursos para concatenaÃ§Ã£o do Nome Breve e IdCurso.

Arquivo: Wnw/worknow

## 12.1.2602.170

### Rotina: PortalSSO

* **[Ticket: WN-21474]** Portal SSO refatorado.

Arquivo: Wnw/worknow

### Rotina: Ãbaris

* **[Ticket: WN-42466]** InclusÃ£o do nÃºmero DOU no json de envio.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-25425]** Melhoria na geraÃ§Ã£o da URL de auto login de atendentes.

Arquivo: Wnw/worknow

* **[Ticket: WN-42031]** Melhoria ao salvar templates em bases oracle.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-389840]** AtualizaÃ§Ã£o em rotina de remoÃ§Ã£o de professores

Arquivo: Wnw/worknow

### Rotina: MS Teaams

* **[Ticket: WN-42539]** Ajuste nas consultas SQL para tratar corretamente quando o Ãºltimo nÃ­vel for Turma.

Arquivo: Wnw/worknow

### Rotina: PortalDadosPessoais

* **[Ticket: WN-41258]** CriaÃ§Ã£o do campo customizado de saÃ­da desacompanhada.

Arquivo: Wnw/worknow

## 12.1.2602.171

### Rotina: Geral

* **[Ticket: WN-39713]** Melhoria nas mensagens de incidentes nos processos.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste consulta aluno e professor e inclusÃ£o de log caso consultas de vinculo, matricula e criaÃ§Ã£o de alunos e professores ocorra

Arquivo: Wnw/worknow

### Rotina: D2L

* **[Ticket: WN-39730]** Ajuste rotina que atualiza refresh token

Arquivo: Wnw/worknow

* **[Ticket: WN-39730]** Tempo de seguranÃ§a para refresh token aumentado para 50 minutos

Arquivo: Wnw/worknow

### Rotina: Portal Ecommerce

* **[Ticket: WN-33066]** Pagamento de mÃºltiplos boletos no portal do aluno.

Arquivo: Wnw/worknow

## 12.1.2602.172

### Rotina: Canvas

* **[Ticket: WN-42116]** Ajuste para exibir mais de um mil registros na tela de Aluno.

Arquivo: Wnw/worknow

## 12.1.2602.173

### Rotina: Ãbaris

* **[Ticket: WN-42466]** Melhoria na geraÃ§Ã£o de informaÃ§Ãµes no json.

Arquivo: Wnw/worknow

* **[Ticket: WN-42466]** InclusÃ£o de informaÃ§Ãµes adicionais na geraÃ§Ã£o do json.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-42723]** Melhoria no log e geraÃ§Ã£o de relatÃ³rios via integraÃ§Ã£o.

Arquivo: Wnw/worknow

### Rotina: D2L

* **[Ticket: WN-42683]** Ajuste no processo de integraÃ§Ã£o de notas.

Arquivo: Wnw/worknow

### Rotina: Sem Rotina Específica

* Adicionado previous\_response\_id OpenIA

Arquivo: Wnw/worknow

## 12.1.2602.174

### Rotina: Ãbaris

* **[Ticket: WN-42466]** Melhorias na geraÃ§Ã£o do json enviado para o Ãbaris.

Arquivo: Wnw/worknow

### Rotina: WorkChat

* **[Ticket: WN-43193]** CriaÃ§Ã£o das colunas AÃ§Ã£o e Id. AÃ§Ã£o na resposta da FÃ³rmula Visual.

Arquivo: Wnw/worknow

### Rotina: Plataforma A

* **[Ticket: WN-43247]** Ajuste na consulta SQL para validar NULL corretamente.

Arquivo: Wnw/worknow

### Rotina: MS Teams

* **[Ticket: WN-42908]** Ajuste no processo de atualizaÃ§Ã£o de senha no AD.

Arquivo: Wnw/worknow

## 12.1.2602.175

### Rotina: Plataforma A

* **[Ticket: WN-32421]** Ajuste na integraÃ§Ã£o para enviar as datas da Grade Curricular corretamente ou nulas.

Arquivo: Wnw/worknow

### Rotina: Ãbaris

* **[Ticket: WN-42466]** InclusÃ£o do id de dados do registro do diploma digital.

Arquivo: Wnw/worknow

* **[Ticket: WN-42466]** Melhorias na geraÃ§Ã£o de informaÃ§Ãµes do json para o Ãbaris.

Arquivo: Wnw/worknow

### Rotina: Moodle

* **[Ticket: WN-29384]** Nova opÃ§Ã£o para manter a data original da turma disciplina na criaÃ§Ã£o e atualizaÃ§Ã£o de cursos, ignorando os parÃ¢metros de dias antes e depois.

Arquivo: Wnw/worknow

* **[Ticket: WN-43241]** Ajuste no processo de integraÃ§Ã£o de professores ao utilizar o parÃ¢metro complementar Email do Moodle.

Arquivo: Wnw/worknow

### Rotina: Blackboard

* **[Ticket: WN-38984]** Ajuste rotina inativaÃ§Ã£o e ativaÃ§Ã£o de aluno. Vinculo de professor e criaÃ§Ã£o de termos

Arquivo: Wnw/worknow

### Rotina: Sharepoint

* **[Ticket: WN-42096]** Corrigido vÃ­nculo de anexos em movimentos para validar o mÃ³dulo de origem.

Arquivo: Wnw/worknow

### Rotina: Canvas

* **[Ticket: WN-43083]** Ajuste no processo de remoÃ§Ã£o de alunos.

Arquivo: Wnw/worknow

# TOTVS Automação de Ponto

## 12.1.2602.100

### Rotina: PORTARIA 671 - AEJ

* **[Ticket: 26480626 / DRHJORNRM-9304]** Adequação na geração do AEJ para manter a compatibilidade com o sql server 2014/2016.

Arquivo: RM.Pto.Relatorio.Data.dll

## 12.1.2602.101

### Rotina: ESPELHO

* **[Ticket: 26415410 / DRHJORNRM-9259]** Validações na leitura de listas de horários.

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: PARAMETRIZADOR

* **[Ticket: DRHJORNRM-9147]** Parâmetro Limite de dias para compensação do saldo banco de horas - Não permitir inserir valor negativo

Arquivo: RM.Pto.Parametros.Form.dll

## 12.1.2602.104

### Rotina: APROVAÇÃO DE BATIDAS

* **[Ticket: DRHJORNRM-9385]** Adequação do filtro de subordinados referente a parametrização do sistema para uso de gestão por hierarquia ou chefe supervisor. A validação da parametrização está atribuida ao RM Gestão de Recursos Humanos.

Arquivo: RM.Pto.Contexto.Server.dll

## 12.1.2602.109

### Rotina: IMPORTAÇÃO DE BATIDAS

* **[Ticket: DRHJORNRM-9148]** Melhoria no algoritmo de magnetismo (alocação automática de batidas por aproximação de batida realizada x horário planejado) para funcionários com mais de um vínculo de trabalho utilizando cálculo de proximidade absoluta incluindo batidas realizadas próximas a trocas de turno ou em jornadas noturnas (que cruzam a meia-noite)

Arquivo: RM.Pto.ImportacaoExportacao.Data.dll

## 12.1.2602.110

### Rotina: ESPELHO

* **[Ticket: DRHJORNRM-9417]** Exibição do rodapé ao entrar no modulo de automação de ponto

Arquivo: RM.Pto.dll

### Rotina: UTILIZAR CARTÃO DE PONTO

* **[Ticket: DRHJORNRM-9418]** Adequar o produto para que valide a data de admissão x campos Utiliza Cartão de Ponto e Deixar de Utilizar Cartão de Ponto

Arquivo: RM.Pto.Funcionario.Data.dll

## 12.1.2602.111

### Rotina: CARTÃO DE PONTO

* **[Ticket: DRHJORNRM-8439]** Adequação do sistema para compatibilidade com CNPJ alfanumérico

Arquivos: RM.Pto.ImportacaoExportacao.Data.dll; RM.Pto.Integracao.Intf.dll; RM.Pto.Integracao.Server.dll; RM.Pto.Utils.Intf.dll; RM.Pto.Relatorio.Data.dll

### Rotina: MEU PONTO - VER RESUMO

* **[Ticket: DRHMEURH-20899]** Ajuste para a correta exibição de horário contiguo no Meu RH

Arquivos: RM.Pto.Rest.Intf.dll; RM.Pto.Rest.Server.dll

## 12.1.2602.113

### Rotina: PORTAL - GESTÃO POR ESCALA

* **[Ticket: DRHJORNRM-9206]** Implementação de log na alteração por escala de horário.

Arquivos: Portal Corpore.Net

## 12.1.2602.119

### Rotina: RELÓGIO / BATIDA POR GEOLOCALIZAÇÃO

* **[Ticket: 26533997 / DRHMEURH-21322]** Ajuste para retornar timezone corretamente na batida de ponto | Meu RH

Arquivos: FrameHTML/RM.Pto.WebAPI.dll

## 12.1.2602.125

### Rotina: MEU PONTO - ESPELHO DO PONTO

* **[Ticket: DRHMEURH-20785]** Ajuste no retorno de dias ocasionais do Meu RH para considerar corretamente os dados.

Arquivos: FrameHTML/RM.Pto.WebAPI.dll

## 12.1.2602.130

### Rotina: HORA REDUZIDA

* **[Ticket: DRHJORNRM-9273]** Na definição do tipo de ocorrência a propriedade do enumerado do tipo de ocorrência permanece mesmo.

Arquivo: RM.Pto.Calculo.Service.dll

## 12.1.2602.133

### Rotina: EXCEÇÕES

* **[Ticket: 26826068 / DRHJORNRM-9478]** Feito o refactoring melhorando a complexidade ciclomática e favorecendo a manutenção. Foi removido um trecho da alteração realizada na issue 8202, corrigido os TUS e analisado os dois cenários citados.

Arquivo: RM.Pto.Relatorio.Data.dll

## 12.1.2602.134

### Rotina: CADASTRO

* **[Ticket: 26882260 / DRHJORNRM-9564]** Na leitura do horário a jornada atual associa-se ao próximo índice apenas se o parâmetro "Considera Data Fim Da Jornada Como Data Referencia" estiver marcado e houver múltiplas jornadas preenchidas para o mesmo horário.

Arquivo: RM.Pto.Horario.Data.dll

## 12.1.2602.135

### Rotina: RECÁLCULO (CALCULAR)

* **[Ticket: 26976872 / DRHJORNRM-9580]** Na compensação por período, tratado para que comparações com tipos string em banco de dados usem aspas simples (').

Arquivo: RM.Pto.BancoDeHoras.Data.dll

## 12.1.2602.142

### Rotina: ESPELHO

* **[Ticket: DRHJORNRM-9463]** Ajustes solution ponto

Arquivo: RM.Pto.Batida.Form.dll

## 12.1.2602.145

### Rotina: PORTARIA 671 - AEJ

* **[Ticket: 27284934 / DRHJORNRM-9666]** Melhoria no processamento dos dados para geração do relatório AEJ.

Arquivo: RM.Pto.Relatorio.Data.dll

## 12.1.2602.151

### Rotina: PORTARIA 671 - AEJ

* **[Ticket: 28165001 / DRHJORNRM-9768]** Adequação no relatório AEJ para imprimir de 1 a 8 caracteres referente a versão do sistema sem impactos em regras de negócio.

Arquivo: RM.Pto.Relatorio.Data.dll

## 12.1.2602.152

### Rotina: COMPENSAÇÃO DE DIA PONTE

* **[Ticket: 26707862 / DRHJORNRM-9611]** Ajuste referente ao cálculo da hora inicio da jornada de trabalho para compensação do dia ponte sem impactos nas regras de negócio

Arquivo: RM.Pto.Horario.Data.dll

### Rotina: ESPELHO

* **[Ticket: 26842862 / DRHJORNRM-9690]** Correção a consulta de feriados da seção do funcionário sem impactos nas regras de negócio

Arquivo: RM.Pto.Funcionario.Data.dll

## 12.1.2602.154

### Rotina: EDITAR BATIDAS

* **[Ticket: 27685693 / DRHJORNRM-9645]** Na inserção de batida duplicada em Oracle, os valores comparados são de acordo com a linha inserida.

Arquivo: RM.Pto.Batida.Data.dll

### Rotina: UTILIZAR CARTÃO DE PONTO

* **[Ticket: 27891747 / DRHJORNRM-9729]** Adequação para permitir utilizar ponto ao definir a opção: Considerar a data de admissão.

Arquivo: RM.Pto.Funcionario.Data.dll

## 12.1.2602.163

### Rotina: MEU PONTO - ESPELHO DO PONTO

* **[Ticket: 28519032 / DRHMEURH-22250]** Ajuste na visualização dos pontos de atenção no espelho de ponto do Meu RH.

Arquivo: RM.Pto.Rest.Server.dll

## 12.1.2602.165

### Rotina: EDITAR BATIDAS

* **[Ticket: 28658893 / DRHJORNRM-9855]** Na edição individual de marcações é validado se a data de inserção da batida sendo editada é a mesma de alguma existente em banco, caso sim, a batida existente está sendo editada, caso não se trata de uma nova batida. Ajuste impacta apenas bases Oracle.

Arquivo: RM.Pto.Batida.Data.dll

## 12.1.2602.170

### Rotina: HORÁRIOS POR INTERVALO

* **[Ticket: DRHJORNRM-9848]** Adequação para aumentar o campo descrição do horário do funcionário em conformidade com leiaute do eSocial versão S-1.3

Arquivos: RM.Pto.Horario.Data.dll; RM.Pto.Horario.Intf.dll; RM.Pto.Horario.Form.dll

## 12.1.2602.175

### Rotina: TIPOS DE OCORRÊNCIA

* **[Ticket: 28834300 / DRHJORNRM-9928]** Adequação no totalizador do saldo de banco de horas que estava triplicando o valor do saldo no espelho de ponto quando existe lançamento de ocorrência customizada.

Arquivo: RM.Pto.Ocorrencia.Data.dll

# TOTVS Avaliação e Pesquisa

## 12.1.2602.100

### Rotina: PROCESSOS DE IMPORTAÇÃO - IMPORTAR GABARITOS

* **[Ticket: 26330486 / DEDUCAPCOM-10111]** Alterações para entrar com notas de provas por candidatos.

Arquivos: RM.Tst.Provas.Data.dll; RM.Tst.Processos.Form.dll; RM.Tst.Processos.Server.dll

## 12.1.2602.124

### Rotina: Sem Rotina Específica

* **[Ticket: DEDUCAPCOM-10380]** Adicionando mensagem de aviso quando o usuario do portal da pesquisa publica tentar efetuar uma pesquisa sem informar algum campo de busca

Arquivo: Edu/portalbiblioteca

### Rotina: RM EXECUTOR (WEB SERVICE)

* **[Ticket: DEDUSAGA-10280]** Melhoria no processo de execução de avaliações e pesquisa

Arquivo: RM.TstExec.WebService.dll

## 12.1.2602.125

### Rotina: Sem Rotina Específica

* **[Ticket: DEDUCAPCOM-10380]** Ajuste na consulta ao portal da Biblioteca

Arquivo: Edu/portalbiblioteca

# TOTVS Banco de Dados

## 12.1.2602.100

### Rotina: CADASTRO DE DENTES

* **[Ticket: DSAUGHPACDIG-1337]** Marcação: SA.2026.02\_01 - Adicionar coluna STATUS na tabela SZMAPAFACIAL

Arquivo: Cvn.12.1.2602.sql

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11075]** Marcação: CN.2026.02\_01 - Adicionadas as colunas HORASSEMANAISMEDIADOR, ATUACAOMEDASSINCRONOS, ATUACAOMEDSINCRONOS, ATUACAOMEDSINCRONOSMEDIADOS, ATUACAOMEDPRESENCIAIS, ATUACAOMEDPESQUISAEXTENSAO, ATUACAOMEDGRUPOESTUDOS, ATUACAOMEDPLANJAATIVIDADES, ATUACAOMEDAVALAPRENDIZAGEM, ATUACAOMEDCOLEGIADOS e ATUACAOMEDAUTOAVALINSTIT na tabela SPROFESSORTURMA para utilização no módulo Educacional.Adicionadas as colunas HORASSEMANAISMEDIADOR, ATUACAOMEDASSINCRONOS, ATUACAOMEDSINCRONOS, ATUACAOMEDSINCRONOSMEDIADOS, ATUACAOMEDPRESENCIAIS, ATUACAOMEDPESQUISAEXTENSAO, ATUACAOMEDGRUPOESTUDOS, ATUACAOMEDPLANJAATIVIDADES, ATUACAOMEDAVALAPRENDIZAGEM, ATUACAOMEDCOLEGIADOS e ATUACAOMEDAUTOAVALINSTIT na tabela SPROFESSORMEC para utilização no módulo Educacional.Adicionadas as colunas CODSENTENCA91ES e CODSENTENCA92ES na tabela SINSTITUICAOMEC para utilização no módulo Educacional.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DEDUBOPE-11073]** Marcação: CN.2026.01\_05 - Ajustes na tabela de professor do MEC para ajustes do Arquivo 31 do Censo Superior

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DEDUBOPE-11073]** Marcação: CN.2026.01\_07 - Ajustes na tabela SPROFESSORTURMA para inclusão de campos relativos ao Layout 32 do Censo Superior

Arquivo: Cvn.12.1.2602.sql

### Rotina: ENVIO DE DADOS PARA A FEEDZ

* **[Ticket: DRHROTRM-14773]** Marcação: LB.2026.02\_01 - Criação da tabela PINTEGRACAOPARAMSECAO para armazenar tokens e seções na integração com a Feedz.

Arquivo: Cvn.12.1.2602.sql

### Rotina: INCLUSÃO

* **[Ticket: 26229349 / DOCELETRONICOS-456]** Reabertura de solicitação de script de marcação LI.2026.01\_13.

Arquivos: Cvn.12.1.2602.sql; Cvn.12.1.2510.sql; Cvn.12.1.2502.sql; Cvn.12.1.2506.sql

* **[Ticket: 26229349 / DOCELETRONICOS-456]** Marcação: LI.2026.01\_13 - Aumento do tamanho das colunas de chave de acesso para tabelas relacionadas a documentos eletrônicos

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: 26229349 / DOCELETRONICOS-456]** Marcação: NU.2026.02\_02 - Aumento do tamanho das colunas de chave de acesso para tabelas relacionadas a documentos eletrônicos

Arquivo: Cvn.12.1.2602.sql

### Rotina: PROFESSORES

* **[Ticket: DEDUBOPE-11390]** Marcação: CN.2026.02\_04 - Adicionadas as colunas PROFESSORAPTO e PROFESSORAUTORIZADO na tabela SDISCAUTORIZADA.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.101

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4706]** Marcação: CP.2026.02\_02 - Alteração do nome da coluna que identifica o número de Batch, de BATHCID para BATCHID

Arquivo: Cvn.12.1.2602.sql

### Rotina: BALANCETE (RM CTB)

* **[Ticket: 26011194 / CONTROLADORIA01-14466]** Marcação: SD.2026.01\_01 - Adicionado um índice na tabela CGERENCIA para auxiliar na performance dos relatórios Balancete, Razão e Retrospectiva que são do tipo Gerencial.

Arquivo: Cvn.12.1.2602.sql

### Rotina: FECHAMENTO DO CONDOMÍNIO

* **[Ticket: 26296488 / TINREV001-25766]** Marcação: SG.2026.02\_01 - Adicionado a coluna TIPOVALOR para a tabela XCONDDESPESAFIN para controle de despesas financeira no modulo de condomínio

Arquivo: Cvn.12.1.2602.sql

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-214]** Marcação: LI.2026.02\_02 - Adicionada as colunas sobre Alíquota Adicional na tabela de Tributos (DTRIBUTO).

Arquivo: Cvn.12.1.2602.sql

### Rotina: PERT

* **[Ticket: TOPORCAPLAN001-29136]** Marcação: SO.2026.02\_02 - Alterações na precisão de campos de quantidade das tabelas MTRFBASE, MTRFPLAN , MTRFMEDIDO , MTRFREAL

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.102

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: TOPORCAPLAN001-29591]** Marcação: SO.2026.02\_01 - Criação de campos "Indicativo de Prestação de Serviços" e "Tipo de Projeto" na tabela de Contratos

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.104

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: DEDUCAPCOM-8936]** Marcação: CN.2026.02\_03 - Script para adequar a chave primária da tabela SCATEGORIANOTIFICACAO validando corretamente a quantidade de colunas necessárias para a chave da tabela.

Arquivo: Cvn.12.1.2602.sql

### Rotina: TGM

* **[Ticket: DFRWTOOLS-4758]** Marcação: CP.2026.02\_04 - Adiciona a tabela GNOTIFYSERVERWHITELIST para controle dos executores da integração SmartLink Data Sharing

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.107

### Rotina: CADASTROS - PROCESSOS - CÓPIAS (RM LI)

* **[Ticket: DMOTORFISCALRM-153]** Marcação: LI.2026.02\_06 - Inserir dados da base aceleradora - Vigência Alíquota !

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DMOTORFISCALRM-153]** Marcação: LI.2026.02\_05 - Inserir dados da base aceleradora - Regras Tributárias!

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DMOTORFISCALRM-153]** Marcação: LI.2026.02\_04 - Inserir dados da base aceleradora - Classificação Fiscal de Bens e Serviços !

Arquivo: Cvn.12.1.2602.sql

### Rotina: MANUTENÇÃO RM ATUALIZADOR

* **[Ticket: DGPAADBH-4271]** Para banco de dados Sql Server irá avisar se possui índices ou estatísticas na colunas para usuário remove-las antes.

Arquivo: RM.Upg.Server.dll

## 12.1.2602.108

### Rotina: NFS-E - ENVIO

* **[Ticket: DMOTORFISCALRM-366]** Marcação: LI.2026.02\_07 - Adicionada coluna - PERCENTUALREDUCAO - na tabela - DVIGENCIAALIQUOTA - para utilização do Módulo Fiscal.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.111

### Rotina: BAIXAS REALIZADAS - CONSULTA|EXCLUSÃO

* **[Ticket: DRMGR-4567]** Marcação: FS.2026.02\_01 - Adicionado o índice da tabela FLANBAIXA para as colunas (STATUS, CODCOLIGADA, DATABAIXA, IDLAN, IDBAIXA), para tratar performance da consulta de informações de pagamento dos tributos de IBS e CBS

Arquivo: Cvn.12.1.2602.sql

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 26501300 / DRMMATERIAIS-8926]** Marcação: NU.2026.03\_02 - Inclusão de referência de menu profiler em GMENU

Arquivo: Cvn.12.1.2602.sql

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-8971]** Marcação: NU.2026.02\_05 - Criação do Identificador do tipo de operação da NFS-e

Arquivo: Cvn.12.1.2602.sql

### Rotina: NF-E - ENVIO

* **[Ticket: DRMMATERIAIS-8889]** Marcação: NU.2026.02\_06 - Criação do campo relacionando ao evento de prorrogação de remessa para item de movimento

Arquivo: Cvn.12.1.2602.sql

### Rotina: NFS-E - ENVIO

* **[Ticket: DRMMATERIAIS-9053]** Marcação: NU.2026.03\_01 - Tributação do Movimento/Item – Criar campos para tratamento do Percentual de Redução para Compras Governamentais

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.112

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 25449607 / TOPORCAPLAN001-29790]** Marcação: SO.2026.03\_02 - Inclusão do campo VALORCONTRATOINICIAL na tabela MCNT

Arquivo: Cvn.12.1.2602.sql

### Rotina: PARÂMETROS

* **[Ticket: TINREV001-25878]** Marcação: SG.2026.02\_02 - adicionado a coluna ORIGEM na tabela XALGCONFISSAODIVIDAPARAMFIN para utilização do modulo de shopping representando a origem do parametro financeiro

Arquivo: Cvn.12.1.2602.sql

### Rotina: PROTOCOLO TEV

* **[Ticket: 26028078 / DSAUGHNEXUS-572]** Marcação: SA.2026.02\_07 - Criação da tabela SZCADSCOREFORMULA para armazenar as fórmulas com a expressão matemática a ser aplicado sobre uma pontuação de score.Inserção da fórmula para cálculo do score de SAPS III (na tabela SZCADSCOREFORMULA ).Alteração do registro do cadastro do score de SAPS III para disponibilização da funcionalidade (SZCADSCORE).Alteração na tabela SZSCOREPACIENTERESPOSTA para armazenar o vínculo da resposta do score (pontuação) com a fórmula aplicada (IDFORMULA), resultado da fórmula aplicada (TOTALFORMULA) e descrição (DESCRICAOTOTALFORMULA).

Arquivo: Cvn.12.1.2602.sql

### Rotina: SMART VIEW (TREPORTS)

* **[Ticket: TOPEXECONTROL01-30433]** Marcação: SO.2026.03\_01 - Adicionado o tipo de recurso "SUPRIMENTO" a tabela RRELTIP para integração do Smart View

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.113

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: TINPAD001-21772]** Marcação: SG.2026.03\_02 - Aumentar a precisão dos campos de valores resíduo XVENDAPARCELARESIDUO, XVENDAPARCELA e XVENDAPARCELAREAJUSTE

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.114

### Rotina: USO GERAL

* **[Ticket: 26402230 / DSAUGHFATF-25207]** Marcação: SA.2026.03\_01 - Adicionada a coluna NGUIAANTERIOR na tabela SZANSATENDAUTORIZCAB para salvar a guia anterior caso o numero de guia operadora seja atualizado.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: 26402230 / DSAUGHFATF-25207]** Aguardando o envio da 2510 para aprovar na 2506.

Arquivo: Cvn.12.1.2506.sql

## 12.1.2602.115

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: TINPAD001-21772]** Marcação: SG.2026.03\_05 - Implementação do valor base importado de sistemas como base para o reajuste da XVENDAPARCELABASE.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.116

### Rotina: USO GERAL

* **[Ticket: 26402230 / DSAUGHFATF-25207]** Marcação: SA.2026.03\_07 - Inserido em todas as condições contratuais antigas o valor default "T" para o novo IDPARAM = '187'

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.117

### Rotina: Sem Rotina Específica

* **[Ticket: DRHSSTPT-1780]** Marcação: VI.2026.03\_01 - Adicionada nova coluna 'INFOPATPREC' na tabela 'VPROCTRABDADOSCOMPL' para adequação à Nota Técnica 06-2026 do eSocial.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: 26711554 / DSAUCLINICA-14371]** Marcação: SA.2026.03\_14 - Atualização da visão RMV\_ANTIBIOTICO para exibir corretamente a indicação dos antibióticos.

Arquivo: Cvn.12.1.2602.sql

### Rotina: APURAÇÃO DE PLANTÕES REALIZADOS

* **[Ticket: DSAUGHFATF-25549]** Marcação: SA.2026.03\_11 - Adicionado o campo PLANTAOCINDERELA na tabela SZPLANTAODETALHES para utilização na tela de Registro de Plantões

Arquivo: Cvn.12.1.2602.sql

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-216]** Marcação: LI.2026.03\_02 - Alterando o tipo das colunas LIMITEISENTOPERIODO, RECISENTAMAJORACAO, RECISENTAMAJORACAO2, RECISENTAMAJORACAO3, RECISENTAMAJORACAO4, RECMAJORADA, RECMAJORADA2, RECMAJORADA3, RECMAJORADA4 na tabela DPERIODO. para RMDVALOR4

Arquivo: Cvn.12.1.2602.sql

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21946]** Marcação: SA.2026.03\_18 - Adicionada a coluna ORIGEMREGISTRO na tabela SZORCAMENCLI e CLASSIFICACAOITEM na SZORCAMENCLIITEM para uso no Orçamento para Clientes do RM Saúde.

Arquivo: Cvn.12.1.2602.sql

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-22766]** Marcação: SA.2026.02\_04 - Criação de coluna "FLUXOPRESCMEDSOROCOMPOPCIONAL" na tabela "SZUNIDATEND" para utilização no prontuário eletrônico.

Arquivo: Cvn.12.1.2602.sql

### Rotina: ROLETA DE VENDAS

* **[Ticket: 26758843 / DTCGI\_INTSYNC-2730]** Marcação: SG.2026.03\_04 - Criada a tabela XPIGIROROLETAORDENACAO para armazenar a ordem de giro da roleta de leads do Portal de Imóveis, possibilitando o controle da sequência de distribuição dos leads entre os corretores vinculados às equipes

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.119

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-216]** Marcação: LI.2026.03\_03 - Alterando o tipo das colunas LIMITEISENTOPERIODO, RECISENTAMAJORACAO, RECISENTAMAJORACAO2, RECISENTAMAJORACAO3, RECISENTAMAJORACAO4, RECMAJORADA, RECMAJORADA2, RECMAJORADA3, RECMAJORADA4 na tabela DPERIODO. para RMDVALOR4

Arquivo: Cvn.12.1.2602.sql

### Rotina: PARAMETRIZADOR - ESOCIAL

* **[Ticket: 24821471 / DRHROTRM-15563]** Marcação: LB.2026.03\_01 - Criação do campo DTMUDANCA na tabela PFUNCOBSERVACAO para uso no evento S-2206 do eSocial

Arquivo: Cvn.12.1.2602.sql

### Rotina: PLANO TERAPÊUTICO

* **[Ticket: 26210533 / DSAUPEPCONV-22636]** Marcação: SA.2026.03\_16 - Alteração das colunas PROBLEMA, RESULTADO, OBSERVACAO, INTERVENCOES

Arquivo: Cvn.12.1.2602.sql

### Rotina: REGISTRO ONLINE

* **[Ticket: DRMGR-4729]** Marcação: FS.2026.03\_01 - Funcionalidade: - Criação de campo para definir a quantidade de dias úteis a serem considerados no cálculo da data de liquidação de pagamentos de boleto híbrido via código de barras.Banco de dados:- Criação da coluna QTDDIASUTEISLIQUIDACAO na tabela FCONVENIO;

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.121

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11590]** Marcação: CN.2026.03\_04 - Removendo constraint de not null nos campos de DOCENTEREGENTE, DOCENTECONTEUDISTA, DOCENTECOORDENADOR no cadastro de Professores da Turma

Arquivo: Cvn.12.1.2602.sql

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-25548]** Marcação: SA.2026.03\_12 - Adicionar a coluna CODIGOMSG na tabela SZSUSMSGAIH para gerenciamento dos tipos das críticas na AIH

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.124

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DRMMATERIAIS-9292]** Marcação: NU.2026.03\_04 - Criação da tabela TMOVDEFENSIVOAGRO e inclusão de campos na TMOV relacionados as informações do agronegócio.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DRMMATERIAIS-9295]** Marcação: NU.2026.03\_05 - Criação dos campos de percentual e valor de redução do ISS na TTRBMOV

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DRMMATERIAIS-9293]** Marcação: NU.2026.03\_03 - Criação do campo HABILITADADOSAGRO na TTMVEXT relacionado a exibição da aba dados agro negócio no movimento

Arquivo: Cvn.12.1.2602.sql

### Rotina: EFETIVAR

* **[Ticket: 26577282 / TINREV001-25938]** Marcação: SG.2026.03\_06 - Adicionado as colunas IDCAMPODESCONTO,IDCAMPOACRESCIMO na tabela XALGCONFISSAODIVIDAPARAMFIN para a utilização da confissão de dívida do modulo de shopping

Arquivo: Cvn.12.1.2602.sql

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25685]** Marcação: SA.2026.03\_21 - Criação da tabela SZSUSAIHMOTIVOREJEICAO para cadastro de motivos de rejeição da AIH

Arquivo: Cvn.12.1.2602.sql

### Rotina: OAUTH

* **[Ticket: DFRWFOUNDATION-29246]** Marcação: CP.2026.01\_04 - Criação do campo OIDC\_ENABLED no cadastro de usuário

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DFRWFOUNDATION-29246]** Marcação: CP.2026.02\_05 - Criar tabela GOIDCREDIRECTURLS

Arquivo: Cvn.12.1.2602.sql

### Rotina: PARÂMETROS

* **[Ticket: 26742785 / DEDUPACMEN-8513]** Marcação: CN.2026.03\_03 - Cria tabela SPARAMSERVUTILBOLONLINE para parametrização de serviços que permitem registrar boleto online, substituindo o parâmetro SERVUTILBOLONLINE da tabela SPARAM, em seguida, popula tabela SPARAMSERVUTILBOLONLINE e exclui os registros originais de SPARAM

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: TINREV001-25933]** Marcação: SG.2026.03\_01 - Adicionado as colunas IDLANCONFESSADO, IDCAMPO e VALOR na tabela XALGCONFISSAODIVIDABAIXA para utilização do modulo de confissão de dívida

Arquivo: Cvn.12.1.2602.sql

### Rotina: RECURSO DE GLOSAS

* **[Ticket: 26402611 / DSAUGHFATF-25288]** Marcação: SA.2026.03\_20 - Criação da tabela SZATENDITENSLOTEGUIA para armazenamento do espelho unificado dos itens de lote de guias TISS, contemplando todos os tipos de lançamento (procedimentos, honorários, materiais, medicamentos, taxas e diárias).

Arquivo: Cvn.12.1.2602.sql

### Rotina: REGISTRO DE ATENDIMENTO

* **[Ticket: 26886635 / DSAUPEPCONV-23239]** Marcação: SA.2026.03\_15 - Definir coluna OBSERVACAO das tabelas SZPEPSOLICITAINT, SZPEPSOLICITAINTLOG e SZSOLPROCEDIMENTO.

Arquivo: Cvn.12.1.2602.sql

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23270]** Marcação: SA.2026.03\_19 - Adicionada a coluna IMPRIMEEXAMENAPRESCRICAO na tabela SZUNIDATEND para utilização no módulo de prescrição médica no prontuário eletrônico.

Arquivo: Cvn.12.1.2602.sql

### Rotina: TABELA DE PREÇO

* **[Ticket: DEDUPACMEN-8371]** Marcação: CN.2026.03\_02 - Criação da chave estrangeira entre as tabelas SHABFILIALALUNOTABELAPRECOS e SHABILITACAOALUNO

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.125

### Rotina: ANAMNESE

* **[Ticket: DSAUPEPCONV-22801]** Marcação: SA.2026.02\_06 - Criar tabela SZOBRIGCLINICALOG responsável por conter os logs de violação de regras de obrigatoriedades clínicas do prontuário eletrônico.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUPEPCONV-22800]** Marcação: SA.2026.02\_02 - Criação da tabela SZOBRIGCLINICA para parametrização de obrigações clínicas do prontuário eletrônico.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUPEPCONV-22800]** Marcação: SA.2026.02\_03 - Criação das tabelas SZOBRIGCLINICATIPOACAO, SZOBRIGCLINICACLASSEPROF, SZOBRIGCLINICATIPOATEND e SZOBRIGCLINICAUNIDATEND para criação de obrigatoriedades clínicas no prontuário eletrônico.

Arquivo: Cvn.12.1.2602.sql

### Rotina: BASE ACELERADORA

* **[Ticket: RMARQIA-226]** Reabertura de solicitação de script de marcação CP.2026.03\_06.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: RMARQIA-226]** Marcação: CP.2026.03\_06 - Criação de tabela para armazenar tipos de caminho de Arquivo Sped

Arquivo: Cvn.12.1.2602.sql

### Rotina: OAUTH

* **[Ticket: DFRWFOUNDATION-29246]** Marcação: CP.2026.03\_07 - Criar campo OIDC\_LOGIN na GPARAMS

Arquivo: Cvn.12.1.2602.sql

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: 26546954 / TINPAD001-21898]** Marcação: SG.2026.03\_10 - Adicionar o log da tabela XLOGREAJUSTEVENDAGRUPOLOG da XREAJUSTEVENDAGRUPO

Arquivo: Cvn.12.1.2602.sql

### Rotina: REGISTRO ONLINE

* **[Ticket: DRMGR-3755]** Marcação: FS.2026.03\_02 - Funcionalidade: - Criação de Índice para melhorar o desempenho em consultas da tabela de transações de boleto híbridoBanco de dados:- Criação do Índice referente a coluna CODCOLIGADA;IDBOLETO na tabela FINTEGRACAOCARTAO;

Arquivo: Cvn.12.1.2602.sql

### Rotina: SCORES - OUTROS

* **[Ticket: DSAUPEPCONV-23307]** Marcação: SA.2026.03\_22 - Adicionada a coluna TIPOCOMPONENTE na tabela SZCADSCOREITEM para determinar se as opções de respostas será de seleção única ou múltipla.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.126

### Rotina: Sem Rotina Específica

* **[Ticket: 26904682 / DSAUCLINICA-14465]** Marcação: SA.2026.03\_26 - Atualização da visão RMV\_PROCINVASIVO para permitir a importação de procedimentos invasivos quando estes não forem realizados por convênio SUS.

Arquivo: Cvn.12.1.2602.sql

### Rotina: ANALISE DE ANTIMICROBIANOS - VISÃO

* **[Ticket: 27062599 / DSAUCLINICA-14473]** Marcação: SA.2026.03\_27 - Atualização da visão RMV\_INTERALTA para permitir a importação da internação com as informações relacionada ao leito que o paciente está internado.

Arquivo: Cvn.12.1.2602.sql

### Rotina: ANÁLISE DE LOG - HOMOLOGAÇÃO

* **[Ticket: 27142838 / DEDUPACMEN-8652]** Reabertura de solicitação de script de marcação CN.2026.03\_03.

Arquivos: Cvn.12.1.2506.sql; Cvn.12.1.2510.sql; Cvn.12.1.2602.sql

* **[Ticket: 27142838 / DEDUPACMEN-8652]** Marcação: CN.2026.04\_01 - Restruturação da criação da tabela SPARAMSERVUTILBOLONLINE para parametrização de serviços que permitem registrar boleto online, substituindo o parâmetro SERVUTILBOLONLINE da tabela SPARAM, em seguida, popula tabela SPARAMSERVUTILBOLONLINE e exclui os registros originais de SPARAM

Arquivo: Cvn.12.1.2602.sql

### Rotina: FECHAR EXERCÍCIO CONTÁBIL (RM CTB)

* **[Ticket: 27006177 / CONTROLADORIA01-14599]** Marcação: SD.2026.03\_01 - Removida a constraint dos campos CONCILIACAODEBITO e CONCILIACAOCREDITO da tabela CPARTIDAHIST.

Arquivo: Cvn.12.1.2602.sql

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23118]** Marcação: SA.2026.03\_29 - Nova coluna que será criada na tabela SZPEDEXAMEITEM para representar as observações de exames provenientes do PEP.

Arquivo: Cvn.12.1.2602.sql

### Rotina: USO EXTERNO DE API / WEBSERVICE

* **[Ticket: DEDUTECH-411]** Marcação: SG.2026.03\_03 - Criação da tabela XRDMARKETINGSMARTLINKCONFIG para a integração RD Station Marketing x Totvs Gestão de Imóveis

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.129

### Rotina: CONCILIAÇÃO BANCÁRIA - IMPORTAÇÃO OFX

* **[Ticket: 26887362 / DRMGR-4745]** Marcação: FS.2026.04\_01 - Funcionalidade: - Aumentar o tamanho do campo número do documento da tabela de conciliação bancária para 255 devido ao tamanho retornando no arquivo ofxBanco de dados:- Aumentar tamanho da coluna NUMERODOCUMENTO na tabela FRECONCIL;

Arquivo: Cvn.12.1.2602.sql

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: DSAUGHFATF-25694]** Marcação: SA.2026.03\_25 - Alterado a tabela SZSUSAIHPROD para incluir as colunas IDMOTIVOREJEICAO e OBSERVACAOREJEICAO.

Arquivo: Cvn.12.1.2602.sql

### Rotina: PAINEL DE DISPENSAÇÃO - VISÃO

* **[Ticket: DSAUCLINICA-14487]** Marcação: SA.2026.04\_02 - Criado índice na tabela SZMOVITMAPRAZ contemplando as colunas CODCOLIGADA e IDAPRAZAMENTO, com o objetivo de melhorar a performance das consultas que utilizam esses campos como critério de busca.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.130

### Rotina: CARGOS

* **[Ticket: 24548396 / DRHSSTPT-1196]** Marcação: VI.2026.04\_01 - Adição da coluna RQE (Registro de Qualificação de Especialista) à tabela VPROFISSIONALSAUDE para atendimento à RESOLUÇÃO CFM Nº 2.217/2018

Arquivo: Cvn.12.1.2602.sql

### Rotina: LIBERAÇÃO / INTEGRAÇÃO COM SUPRIMENTOS/FATURAMENTO

* **[Ticket: 27025045 / TOPORCAPLAN001-30038]** Marcação: SO.2026.04\_01 - Alteração de precisão da coluna VALORCONTRATADO na tabela MCNT

Arquivo: Cvn.12.1.2602.sql

### Rotina: MANUTENÇÃO SCRIPTS

* **[Ticket: DGPAADBH-4487]** Adicionando alerta para índices ou estatísticas na coluna MCNT.VALORCONTRATADO

Arquivo: RM.Upg.Server.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: DSAUGHFATF-25777]** Marcação: SA.2026.03\_28 - Permitir Atendimento Externo (BPA/APAC) simultâneo à Internação (AIH)

Arquivo: Cvn.12.1.2602.sql

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21810]** Marcação: SA.2026.03\_13 - Ajuste de tamanho do campo GUICHE da tabela SZPARAMESTACAO para utilização no Painel de Chamadas do RM Saúde.

Arquivo: Cvn.12.1.2602.sql

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22146]** Marcação: SG.2026.04\_02 - ALTERAR A PRIMARY KEY DA TABELA xdistratoparc

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.131

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22088]** Marcação: SA.2026.04\_03 - Adicionada a coluna TIPOAPLIC na tabela SZPERIODOESP para caracterizar se o período é complementar ao período padrão ou se é excludente

Arquivo: Cvn.12.1.2602.sql

### Rotina: ANÁLISE DE LOG - HOMOLOGAÇÃO

* **[Ticket: 27298512 / TOPORCAPLAN001-30108]** Reabertura de solicitação de script de marcação SO.2026.04\_01.

Arquivos: Cvn.12.1.2510.sql; Cvn.12.1.2602.sql

* **[Ticket: 27298512 / TOPORCAPLAN001-30108]** Marcação: SO.2026.04\_02 - Alteração de precisão da coluna VALORCONTRATADO na tabela MCNT

Arquivo: Cvn.12.1.2602.sql

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DRMMATERIAIS-9292]** Marcação: NU.2026.04\_02 - Alterando tipo da coluna de decimal para int

Arquivo: Cvn.12.1.2602.sql

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1387]** Marcação: LI.2026.04\_01 - Criar campo coluna: CNAE na tabela DTRBMUNICIPIOPRD. Possibilitar informar o código CNAE do item para o município.

Arquivo: Cvn.12.1.2602.sql

### Rotina: MANUTENÇÃO SCRIPTS

* **[Ticket: DGPAADBH-4487]** Adicionando alerta para índices ou estatísticas na coluna TMOV.NUMGUIATRANSITO

Arquivo: RM.Upg.Server.dll

### Rotina: TIPO DE MOVIMENTO

* **[Ticket: DRMMATERIAIS-9352]** Marcação: NU.2026.04\_03 - Inclusão das colunas FINALIDADEEMISSAONFE, TIPONFDEBITO e TIPONFCREDITO na TTMVEXT

Arquivo: Cvn.12.1.2602.sql

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22146]** Marcação: SG.2026.04\_04 - Novas colunas na tabela de distrato xdistratoparc para gerenciar os valores das parcelas

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.132

### Rotina: ERRO DURANTE A CONVERSÃO

* **[Ticket: 27265610 / DGPAADBH-4501]** Em Oracle, quando não usa o table\_space padrão estava fixo o RM\_INDICES na criação de tabela controle de migração.

Arquivo: RM.Upg.Server.dll

### Rotina: ROLETA DE VENDAS

* **[Ticket: DTCGI\_INTSYNC-2895]** Marcação: SG.2026.04\_05 - Script para excluir ForeinKeys (FKXPIFILALEADHIST\_XPIROLETA e FKXPIFILALEADHIST\_XPIEQUIPE) em tabela (XPIFILALEADHIST) de histórico da roleta de leads

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DTCGI\_INTSYNC-2931]** Marcação: SG.2026.04\_03 - Adicionado coluna de ULTIMOGIRO nas tabelas XPIEQUIPECORRETOR e XPIROLETAEQUIPE para representar ponteiros de posição de ultima eqiupe e corretor a receber o lead no processo de giro da roleta de leads

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.133

### Rotina: Sem Rotina Específica

* **[Ticket: 27293034 / TINPAD001-22227]** Marcação: SG.2026.04\_08 - dois campos novos para a apuração de competência xcompvendaparcela com o valores do TCGI

Arquivo: Cvn.12.1.2602.sql

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3707]** Marcação: LI.2026.04\_02 - Adicionado o campo NUMEROCEBAS na tabela DPARAMSECFFILIAL. Campo referente ao Certificado de Entidade Beneficente de Assistência Social - CEBAS.

Arquivo: Cvn.12.1.2602.sql

### Rotina: SCORES - OUTROS

* **[Ticket: DSAUPEPCONV-23307]** Marcação: SA.2026.03\_24 - Atualização SZCADSCOREITEM do SCORE SAPS III para indicar os campos que serão de multiseleção.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.134

### Rotina: Sem Rotina Específica

* **[Ticket: 27293034 / TINPAD001-22227]** Marcação: SG.2026.04\_09 - Um campo novo para a apuração de competência xcompvendaparcela com o valores do TCGI

Arquivo: Cvn.12.1.2602.sql

### Rotina: CONTRATO DE LOCAÇÃO

* **[Ticket: TINREV001-25467]** Marcação: SG.2026.03\_07 - Tabela XALGCONTRATOLOCMOV para armazenar os movimentos gerados pelas baixas de lançamentos de aluguel.

Arquivo: Cvn.12.1.2602.sql

### Rotina: FOLHA DE PRODUÇÃO DE PRESTADORES

* **[Ticket: DSAUGHFATF-25896]** Marcação: SA.2026.04\_05 - Adicionado a coluna OBSERVACAO na tabela SZFOLHAPAGTOPREST.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.136

### Rotina: TIPO DE MOVIMENTO

* **[Ticket: DRMMATERIAIS-9680]** Marcação: NU.2026.04\_07 - Criação da coluna CODTMVNOTADEBITOMULTAJUROS na tabela TTMVEXT

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.137

### Rotina: CONTRATOS

* **[Ticket: DEDUPACMEN-8635]** Marcação: CN.2026.03\_05 - Adiciona a coluna OBRIGAASSINATURATAEMATRICULA na tabela SHABILITACAOFILIALPL para permitir a assinatura do contrato TAE na parametrização por curso.

Arquivo: Cvn.12.1.2602.sql

### Rotina: MAPA DE DISPENSAÇÃO

* **[Ticket: 27392539 / DSAUCLINICA-14594]** Marcação: SA.2026.04\_07 - Criação de índice na tabela SZATENDMATMED, com o objetivo de melhorar a performance da consulta utilizada na busca de lotes de produtos na rotina de devolução, localizada na movimentação de estoque.

Arquivo: Cvn.12.1.2602.sql

### Rotina: MOTIVO DE RESERVA DE LEITO - CADASTRO

* **[Ticket: DSAUGHFATF-25845]** Marcação: SA.2026.04\_08 - Criação de tabelas SZTIPOEVOLUCAO e SZTIPOEVOLUCAOCONSPROF para cadastro de Tipo de Evolução para o Catálogo Multiprofissional.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.139

### Rotina: CAMPOS COMPLEMENTARES

* **[Ticket: DRMMATERIAIS-9725]** Marcação: NU.2026.04\_09 - Ajuste da descrição dos campos VALORLIQUIDO e VALORBRUTOITEM , pertencente a TITMMOV na tabela GDIC

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.141

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25417]** Marcação: SG.2026.04\_11 - Tabela para cadastrar os valores de integração da negociação

Arquivo: Cvn.12.1.2602.sql

### Rotina: SCORES - CÁLCULO DO SCORE

* **[Ticket: DSAUPEPCONV-23436]** Marcação: SA.2026.04\_19 - Criação da coluna PRIORIDADEPADRAOSOLICEXAMES na tabela SZUNIDATEND para definir a programação que será default na solicitação de exames.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.142

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27399604 / DEDUBOPE-11727]** Marcação: CN.2026.04\_06 - Adequação da tabela SAUTORIZACAOFILIAL para usar coligada global para todos os registros.

Arquivo: Cvn.12.1.2602.sql

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25853]** Marcação: SA.2026.04\_18 - Adicionada a coluna CODEVOLUCAO na tabela SZORIGEMSUSLANC para determinar a origem do lançamento durante a evolução clínica

Arquivo: Cvn.12.1.2602.sql

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3959]** Marcação: LI.2026.04\_03 - Criação da tabela DDEDUCOES conforme legislação referente ao registro Y730 - IDENTIFICAÇÃO DOS DONATÁRIOS/DESTINATÁRIOS DE DEDUÇÕES DO IRPJ/CSLL

Arquivo: Cvn.12.1.2602.sql

### Rotina: SCORES - CÁLCULO DO SCORE

* **[Ticket: DSAUPEPCONV-23436]** Marcação: SA.2026.04\_12 - Ajuste da equação do score SAPS III

Arquivo: Cvn.12.1.2602.sql

### Rotina: UTILITÁRIOS - DUPLICAÇÕES (RM LI)

* **[Ticket: DMOTORFISCALRM-593]** Marcação: LI.2026.04\_04 - Correção no produto definido para a Cópia de Classificação Fiscal de Bens e Serviços da base aceleradora.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.143

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27399604 / DEDUBOPE-11727]** Reabertura de solicitação de script de marcação CN.2026.04\_06.

Arquivos: Cvn.12.1.2510.sql; Cvn.12.1.2506.sql; Cvn.12.1.2602.sql

## 12.1.2602.144

### Rotina: CRÉDITO/DÉBITO - BAIXA DE LANÇAMENTO VIA CARTÃO

* **[Ticket: FINANCEIRO01-27560]** Marcação: FS.2026.04\_02 - Criação da tabela FCYBERTARGETORIGIN

Arquivo: Cvn.12.1.2602.sql

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3959]** Marcação: LI.2026.05\_02 - Criação da tabela DDESTINATARIOSDEDUCOESECF referente à nova tela de Destinatários das Deduções

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DMONTRIBRM-3959]** Marcação: LI.2026.05\_01 - Apagar Tabela DDEDUCOES para reconfigurar as constraints e tamanho de campos

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.145

### Rotina: AGENDAMENTO

* **[Ticket: 27276123 / DSAUGHASSIST-22446]** Marcação: SA.2026.04\_09 - Inclusão da tabela SZPERIODO na GAutoInc para que o controle de novos ID's seja controlado por ela.Essa alteração se faz necessário porque atualmente está sendo feito através de um Select MAX(ID), que está ocasionando uma não conformidade quando a funcionalidade é executada simultaneamente em dois ou mais terminais ao mesmo tempo

Arquivo: Cvn.12.1.2602.sql

### Rotina: APURAÇÃO DE COMPETÊNCIA

* **[Ticket: TINPAD001-22282]** Marcação: SG.2026.05\_02 - Novos campos para apuração de competência como valor do seguro, outros e tipo de contabilização

Arquivo: Cvn.12.1.2602.sql

### Rotina: CONFIGURAÇÃO

* **[Ticket: TINREV001-24202]** Marcação: SG.2026.04\_14 - Campos para desconto de juros e multa na tabela de confissão (XALGCONFISSAODIVIDA):TAXADESCJUROS - Taxa de desconto nos juros;VALORDESCJUROS - Valor de desconto nos juros;TAXADESCMULTA -Taxa de desconto na multa;VALORDESCMULTA - Valor de desconto na multa.

Arquivo: Cvn.12.1.2602.sql

### Rotina: INCLUSÃO

* **[Ticket: DMONTRIBRM-3953]** Marcação: NU.2026.04\_10 - Adicionada FK da FCFO na tabela TTRBMOV, para fazer o vínculo do beneficiário da COSIRF no lançamento fiscal

Arquivo: Cvn.12.1.2602.sql

### Rotina: UTILITÁRIOS - DUPLICAÇÕES (RM LI)

* **[Ticket: DMOTORFISCALRM-576]** Marcação: NU.2026.05\_01 - Adicionando registro da unidade de medida na GCOPIACOLIGADA.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.146

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25776]** Marcação: SA.2026.03\_30 - Adicionado a coluna CODREGISTROASSOCIADO na tabela SZSUSMSGAIH para indicar qual o código do registro associado a mensagem da AIH.

Arquivo: Cvn.12.1.2602.sql

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23305]** Marcação: SA.2026.05\_12 - Criação da coluna PRIORIDADEPADRAOSOLPRESCRICAO na tabela SZUNIDATEND para definir a programação que será default na solicitação de exames em prescrição medica

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.148

### Rotina: APURAÇÃO DE COMPETÊNCIA

* **[Ticket: TINPAD001-22282]** Marcação: SG.2026.05\_03 - Novo campo para controlar o tipo de fechamento de apuração competência na tabela XCOMP

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: TINPAD001-22282]** Marcação: SG.2026.05\_04 - Novo campo na Apuração de competência da venda para colocar o motivo do não processamento na xcompvenda

Arquivo: Cvn.12.1.2602.sql

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-26016]** Marcação: SA.2026.05\_16 - Adicionada a coluna LANCAMENTOAUTOMATICO na tabela SZSUSPROCREALIZADOS para identificar se a diária lançada é originária do processo de lançamento de diária SUS

Arquivo: Cvn.12.1.2602.sql

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: DSAUGHFATF-26017]** Marcação: SA.2026.05\_15 - Adicionada a coluna CODDIARIAUTISIGTAP na tabela SZLEITO para o lançamento automático de diárias de UTI.

Arquivo: Cvn.12.1.2602.sql

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 27601591 / DEDUPACMEN-8818]** Marcação: CN.2026.05\_01 - Adicionada a coluna ENVIADADOSDESTMOVIMENTO na tabela SALUNO para controle do envio dos dados do destinatário na geração de movimento.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.149

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 27336205 / DRMGR-4970]** Marcação: FS.2026.05\_01 - Adicionar as colunas IDTRBLAN e CST na tabela de histórico FLANBAIXATRBHST, refletindo espelho da tabela de origem. O campo IDTRBLAN devera fazer parte da chave da tabela.

Arquivo: Cvn.12.1.2602.sql

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1554]** Marcação: LI.2026.05\_03 - Criar colunas referentes a autorização da NFS-e na tabela TMOVFISCAL.Campos: Número do Movimento, Data de Emissão do Movimento e Data de Competência

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.150

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1665]** Marcação: LI.2026.05\_06 - Criar colunas CODIGOSERVICOEMITENTE e CODIGOSERVICOFEDERALEMITENTE na tabela DTRBMUNICIPIOPRD, para receber os respectivos códigos na perspectiva do emitente.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.151

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-22171]** Marcação: SG.2026.04\_07 - Adicionar coluna ID\_MOTVENDA na tabela XVENDA para possibilitar a escolha do motivo da venda no cadastro da venda.

Arquivo: Cvn.12.1.2602.sql

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25955]** Marcação: SG.2026.04\_06 - Criação das tabelas XALGNEGOCIACAOBOLETO, destinadas ao gerenciamento da negociação de dívidas de boletos vencidos.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: TINREV001-25955]** Marcação: SG.2026.05\_01 - Adicionado a tabela XALGNEGOCIACAOBOLETOBAIXA para armazenar as baixas dos lançamentos gerado pela negociação de boletos do modulo de shopping

Arquivo: Cvn.12.1.2602.sql

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADA/SAÍDA (RM LI)

* **[Ticket: DMOTORFISCALRM-599]** Marcação: LI.2026.05\_07 - Adição de colunas de Finalidade da Nota Fiscal - FINALIDADEDEBITOCREDITONF, e o Tipo da Nota Fiscal (Crédito ou Débito) - TIPODEBITOCREDITONF na tabela de Lançamento Fiscal - DLAF

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.152

### Rotina: Sem Rotina Específica

* **[Ticket: DRMMATERIAIS-9353]** Marcação: NU.2026.04\_11 - Script para criação Tabela de Movimentos Gerado a partir de Baixas do Financeiro para Geração de Nota.

Arquivo: Cvn.12.1.2602.sql

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11811]** Marcação: CN.2026.05\_02 - Adicionadas novas colunas e realizados ajustes de dados nas tabelas de integração com o MEC para conformidade com o Censo Escolar:Tabela SINSTITUICAOMEC: Adicionadas colunas relativas à infraestrutura e recursos (Esfera Administrativa, Internet, Rede Local, Língua de Ensino, Laboratório de Robótica, Assistente Social e Materiais Didáticos). O script também realiza o UPDATE dessas colunas consolidando informações de campos legados.Tabela STURMAMEC: Adicionadas colunas de classificação da turma (Tipo de Turma, Eixo do Curso e Forma de Organização), com atualização automática baseada nos indicadores de atendimento anteriores.Tabela SPROFESSORMEC: Adicionadas colunas para registro de cursos de formação específica (Alfabetização e Ensino Integral).Tabela SGESTORMEC: Adicionadas colunas para registro de cursos de formação específica (Alfabetização e Ensino Integral).

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DEDUBOPE-11811]** Marcação: CN.2026.05\_03 - Adicionada a coluna CARGAHORARIA na tabela STURMAMEC para utilização no módulo educacional

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.153

### Rotina: MEDICAMENTO

* **[Ticket: DSAUPEPCONV-23403]** Marcação: SA.2026.05\_14 - Adicionada a coluna JUSTIFICACIENCIARESSALVA na tabela SZUNIDATEND para utilização no módulo de prescrição médica no prontuário eletrônico.Adicionado a coluna JUSTIFICATIVACIENCIARESSALVA na tabela SZANALISEFARMPRESCITEM para gravar a justificar para a ciência de itens liberados com ressalva.

Arquivo: Cvn.12.1.2602.sql

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-4099]** Marcação: NU.2026.05\_06 - Adicionado o tipo de recurso "DANFSE" a tabela RRELTIP para geração da DANFSE via Smart View, que está sendo criada na Reforma Tributária

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.155

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10172]** Marcação: CN.2026.04\_09 - Script para habilitar o Assistente de IA TOTVS na Central de Comunicação no PGE (Portal Gestão Educacional). O procedimento ativa os parâmetros do sistema e concede permissão de acesso aos perfis de usuários que já possuem autorização para o envio de mensagens.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DEDUCAPCOM-10172]** Marcação: CN.2026.03\_01 - Criação da tabela SCCOMMENSAGEMIALOG para armazenar o log de uso do assistente de IA da Central de Comunicação

Arquivo: Cvn.12.1.2602.sql

### Rotina: ONCOLOGIA - QUIMIOTERAPIA

* **[Ticket: 26512006 / DSAUPEPCONV-23696]** Marcação: SA.2026.02\_05 - Criação do parâmetro de unidade para indicar qual fórmula de superfície corporal utilizada pela unidade.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.156

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11811]** Marcação: CN.2026.05\_04 - O script adiciona cinco novas colunas na tabela SMECEDUPROFISSIONAL para classificar cursos profissionalizantes por eixo tecnológico, carga horária e tipo de curso. Em seguida, recarrega a tabela com dados completos de 13 eixos (como Ambiente e Saúde, Gestão, Informática, Militar, etc.), incluindo cursos técnicos e de qualificação profissional. Também ajusta a coluna NOME da tabela SMECDISCIPLINA para 200 caracteres, recarrega as tabelas de disciplinas, etapas e séries

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.157

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4994]** Marcação: CP.2026.03\_01 - Criação de índices nos filtros mais utilizados para as tabelas GDATASHARE, GDATASHARERECORDS, GSMARTLINKLOG e GDATASHARESUMMARY

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DFRWTOOLS-4994]** Marcação: CP.2026.05\_10 - Criação de índices para melhorar a performance e agilizar as consultas de preparação do SYNC

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.158

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8556]** Marcação: CN.2026.04\_07 - Criação das tabelas estruturais para o controle de movimentação financeira das disciplinas e das matrículas.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.162

### Rotina: MANUTENÇÃO AUTO SCRIPT

* **[Ticket: DGPAADBH-4212]** Marcação: ZB.2026.05\_06 - Inserir na tabela de dicionário de dados (GDIC) a descrição para a tabela de Atualizações de versões (GUPGATUALIZACAO)

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.163

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11815]** Marcação: CN.2026.06\_01 - Adicionada a coluna CHINTEGRALIZADA na tabela SMATRICPLMEC para utilização no módulo Educacional.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.166

### Rotina: S-1010 - RUBRICAS

* **[Ticket: 26023454 / DRHROTRM-16904]** Marcação: LB.2026.04\_01 - Criação dos campos CODEVENTODEPARARECIBOFERIAS, CODEVENTODEPARAPROVENTOFERIAS, CODEVENTODEPARADESCONTOFERIAS, CODINCCP, CODINCIRRF e CODINCFGTS na tabela PEVENTO para uso nos eventos do eSocial

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.167

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14445]** Marcação: SA.2026.03\_23 - Adicionada as colunas VOLUMEFATURAMENTO e QUANTIDADECONTROLE na tabela SZMOVIESTOQUEITEM, será utilizada para auxiliar no cálculo da unidade de controle nas movimentações de estoque.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14445]** Marcação: SA.2026.04\_20 - Adicionada a coluna VOLUMEFATURAMENTO na tabela SZITENSCIRURGIA, será utilizada para o cálculo da unidade de controle dos itens exibidos no Painel de Cirurgia.

Arquivo: Cvn.12.1.2602.sql

### Rotina: S-1010 - RUBRICAS

* **[Ticket: 26023454 / DRHROTRM-16904]** Marcação: LB.2026.04\_03 - Criação dos campos FORCARINCINSS e INCINSSFORCADA na tabela PEVENTO para uso nos eventos do eSocial

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.168

### Rotina: LANÇAMENTOS - EXECUTA RECÁLCULO

* **[Ticket: DRHCALCRM-12398]** Marcação: LB.2026.04\_02 - Criação de campos no envelope e no recibo de férias para gravação do evento de De Para do eSocial.

Arquivo: Cvn.12.1.2602.sql

### Rotina: NFS-E - CADASTRO

* **[Ticket: DOCELETRONICOS-1912]** Marcação: LI.2026.06\_01 - Copia o conteúdo das colunas: CODIGOSERVICO, CODIGOSERVICOFEDERAL respectivamente para as colunas: CODIGOSERVICOEMITENTE, CODIGOSERVICOFEDERALEMITENTE da tabela: DTRBMUNICIPIOPRD. (valores dos campos código de serviço municipal e código de serviço federal da perspectiva de incidência para a de emissão).Marca o flag, Códigos de trib. pelo mun. emitente quando filial possuir NFS-e autorizada e utiliza layout diferente de nacional.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.170

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4994]** Marcação: CP.2026.04\_03 - Criar campo IS\_DUPLICATED\_EMAIL na tabela GUSUARIO\_SYNC

Arquivo: Cvn.12.1.2602.sql

### Rotina: ANEXOS - ATIVIDADES AGENDADAS

* **[Ticket: DEDUCAPCOM-10714]** Marcação: CN.2026.02\_05 - Script para criação da estrutura para armazenar no TOTVS Educacional os dados de notificações enviados para o Meu eduCONNECT.

Arquivo: Cvn.12.1.2602.sql

### Rotina: FATURAMENTO TISS

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.04\_04 - Adicionar a coluna OBSERVACAOGUIA na tabela SZCONTROLEGLOSAITEM para utilizar no módulo de importação de Retorno de Demonstrativo

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.02\_10 - Inclusão de novos registros no menu Cadastros/Uso Geral/TISS/Mensagens de negativa de Elegibilidade, para atender a versão 4.03.00 da TISS

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.04\_11 - Criação da tabela SZANSCOBERTURAESPECIAL contendo os códigos da tabela de domínio TISS 75 - Terminologia de Cobertura Especial, incluído na versão 4.03.00 da TISS, referente ao campo “Cobertura Especial” da Guia de Autorização no Gestão Hospitalar.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.02\_09 - Atualização das tabelas de domínio para a nova versão 4.03.00 da TISS

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.05\_13 - Criação de Tabela SZANSLOGCOMUNICACAO para controle de Log para envios de comunicação de Internação e Alta TISS e Criação da tabela SZANSCOMUNICACAO para controle de comunicação e retorno de Internação e Alta TISS

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.03\_06 - Criação da tabela SZANSCENTROCONSUMOCORRELA utilizada no menu Cadastros/Uso Geral/TISS/Correlação Centro de Consumo

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.05\_06 - Adicionado campo de identificação para WebService utilizado durante gravação de log para TISS, campo TIPODOCGERACAO na tabela SZANSLOGAUTORIZ

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.02\_11 - Criação do Centro de Consumo (SZANSCENTROCONSUMO), referente à Terminologia de Centro de Consumo (tabela 82), da versão 4.03.00 da TISS

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DSAUCLINICA-14791]** Marcação: SA.2026.04\_15 - Criação do campo COBERTURAEXCLUSIVAHOSPITALAR na tabela SZPLANOSCONVENIO para identificar “Plano com cobertura exclusivamente Hospitalar”.

Arquivo: Cvn.12.1.2602.sql

### Rotina: HORÁRIOS POR INTERVALO

* **[Ticket: DRHJORNRM-9848]** Marcação: CR.2026.06\_01 - Atualização do tamanho do campo "Descrição" na tabela de horários.

Arquivo: Cvn.12.1.2602.sql

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1657]** Marcação: LI.2026.05\_08 - Atualização do valor do campo SANITIZACAODOCE da tabela TPARFILIAL.

Arquivo: Cvn.12.1.2602.sql

* **[Ticket: DOCELETRONICOS-1657]** Marcação: LI.2026.05\_05 - Adiciona a coluna SANITIZACAODOCE na tabela TPARFILIAL, para armazenar o texto de sanitização do XML do DOC-e.

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.171

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11975]** Marcação: CN.2026.06\_04 - Adicionada a coluna ENVIARCHCENSO na tabela SINSTITUICAOMEC para utilização no módulo Educacional

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.173

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 28429021 / TOPORCAPLAN001-30640]** Marcação: SO.2026.06\_01 - Adicionada a coluna VALORREALINHADO nas tabelas MITMCNT E MITMCNTISM

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.174

### Rotina: RELAT. - RELATÓRIO CONFERÊNCIA INSS PATRONAL

* **[Ticket: 28907131 / DRHROTRM-19122]** Marcação: LB.2026.06\_02 - Criação do campo INDSUSPENSAO na tabela PPROCSUSPENSAOINC para uso no relatório

Arquivo: Cvn.12.1.2602.sql

## 12.1.2602.175

### Rotina: LANÇAMENTOS - EXECUTA RECÁLCULO

* **[Ticket: DRHCALCRM-12440]** Marcação: LB.2026.06\_01 - Criação da coluna PERCGARANTIARESC na tabela PFEMPRT para percentual de garantia do empréstimo credito do trabalhador, na Rescisão.

Arquivo: Cvn.12.1.2602.sql

# TOTVS Business Connect

## 12.1.2602.106

### Rotina: Sem Rotina Específica

* **[Ticket: 26586913 / DFRWTOOLS-4830]** Ajustes nos Logs para evitar grande volume em bases sem integração DataSharing.

Arquivos: RM.Con.SmartLink.Service.dll; RM.Lib.Server.dll; RM.Con.SmartLink.Server.dll

## 12.1.2602.109

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4721]** Ajuste no ForceReload para abortar o envio do BatchID em caso de queda de conexão e deixar preparado para novo envio, aguardando nova sinalização.

Arquivo: RM.Con.SmartLink.Infra.dll

## 12.1.2602.111

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4637]** Melhorias na tela de diagnóstico da integração com o SmartLink

Arquivo: RM.Con.Menu.dll

### Rotina: TGM

* **[Ticket: DFRWTOOLS-4758]** Removendo ordenação na consulta da FR para entrega imediata no reader

Arquivo: RM.Con.SmartLink.Service.dll

## 12.1.2602.125

### Rotina: GLOBAIS

* **[Ticket: DFRWTOOLS-4809]** Validação de ambiente portabilidade requisitos para execução do smartlink

Arquivo: RM.Con.SmartLink.Server.dll

### Rotina: OAUTH

* **[Ticket: DFRWFOUNDATION-29246]** Descendo alterações de redirecionamento de URLS do login OIDC

Arquivos: RM.Lib.Server.dll; RM.Con.SmartLink.Server.dll

## 12.1.2602.129

### Rotina: TGM

* **[Ticket: DFRWTOOLS-4864]** Novo Serviço de limpeza de logs do SmartLink

Arquivos: RM.Con.SmartLink.Server.dll; RM.Con.SmartLink.Service.dll; RM.Lib.Server.dll; RM.Lib.Communication.dll

## 12.1.2602.130

### Rotina: Sem Rotina Específica

* **[Ticket: 27124733 / DFRWTOOLS-4923]** Ajustes no Credential Helper para evitar a invalidação das Credenciais e melhoria na identificação dos Logs

Arquivos: RM.Con.SmartLink.Server.dll; RM.Con.TotvsApp.Server.dll; RM.Con.SmartLink.Service.dll; RM.Lib.SmartLink.dll; RM.Con.TotvsApp.Service.dll

## 12.1.2602.158

### Rotina: COMPATIBILIZAÇÃO - UPGRADE DE RELEASE/VERSÃO (BSO)

* **[Ticket: 27239833 / DFRWBI-15599]** Réplica Adição de ponto de plugin no fluxo de edicação de Relatórios e importação de conceitos, Metadados e Relatórios

Arquivos: RM.Rpt.Customizacao.Intf.dll; RM.Rpt.Lib.Server.dll; RM.Con.Conector.Server.dll; RM.Con.Conector.Intf.dll; RM.Glb.Metadata.Intf.dll; RM.Glb.Metadata.Server.dll

## 12.1.2602.167

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4994]** Réplica para versão de mercado de todas as Melhorias no DataSharing

Arquivos: RM.Con.TotvsApp.IService.dll; RM.Lib.SmartLink.dll; RM.Con.Conector.Server.dll; RM.Con.TotvsApp.Intf.dll; RM.Lib.Server.dll; RM.Con.TotvsApp.Server.dll; RM.Glb.SmartX.SmartLink.Diagnostics.dll; RM.Con.SmartLink.Infra.dll; RM.Con.TotvsApp.Service.dll; RM.Lib.dll; RM.Con.SmartLink.Service.dll; RM.Con.SmartLink.Server.dll

## 12.1.2602.168

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4994]** Ajuste na montagem do hash de contexto do Credential Helper

Arquivo: RM.Con.TotvsApp.Intf.dll

## 12.1.2602.170

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4797]** Ajuste no Sync para registrar a WallTableName

Arquivos: RM.Con.SmartLink.Service.dll; RM.Con.SmartLink.Server.dll; RM.Con.TotvsApp.IService.dll

* **[Ticket: DFRWTOOLS-4797]** Ajuste no Sync para resolver conflito entre tabelas com mesmo nome do Delta e FR

Arquivo: RM.Con.SmartLink.Server.dll

* **[Ticket: DFRWTOOLS-4994]** Ajustes no Log removendo informações desnecessárias

Arquivo: RM.Con.SmartLink.Service.dll

* **[Ticket: DFRWTOOLS-4994]** Limpando o cache de TenantId ao limpar credenciais

Arquivos: RM.Con.TotvsApp.Intf.dll; RM.Lib.SmartLink.dll; RM.Con.SmartLink.Service.dll

## 12.1.2602.172

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-5151]** Alteração no mecanismo de verificação do serviço de correção da integração Smartink

Arquivos: RM.Con.SmartLink.Service.dll; RM.Con.SmartLink.Server.dll; RM.Con.SmartLink.Infra.dll

## 12.1.2602.175

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-5188]** Corrigido filtro do Sync para o ForceReload e Carga Inicial

Arquivo: RM.Con.SmartLink.Service.dll

# TOTVS Construção e Projetos

## 12.1.2602.100

### Rotina: ADITIVO

* **[Ticket: 26499352 / TOPORCAPLAN001-29663]** Melhoria de desempenho ao abrir a tela de aditivo do contrato.

Arquivo: RM.Prj.Contrato.Server.dll

* **[Ticket: TOPORCAPLAN001-29570]** Ajustes no cálculo de aditivos, para ajustar o valor total.

Arquivo: RM.Prj.Contrato.Server.dll

### Rotina: APP MINHAS INSPEÇÕES

* **[Ticket: 26352160 / TOPORCAPLAN001-29622]** Filtros de busca em Inspeções do Portal Minhas Inspeções

Arquivo: Prj/minhasinspecoes

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: TOPORCAPLAN001-29653]** Ajuste na consistência da quantidade orçada de pedido de material e de contratos ao criar o pedido de material.

Arquivos: RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.PedidoMaterial.Server.dll; RM.Prj.PedidoMaterial.Intf.dll; RM.Prj.Contrato.Server.dll

### Rotina: PROTHEUS EAI 2.0

* **[Ticket: 26093775 / TOPEXECONTROL01-30423]** Envio pedido de faturamento direto para o Protheus não está sendo possível

Arquivo: RM.Prj.PedidoMaterial.Server.dll

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-29525]** Ajustes na criação e aplicação de Revisão de Reprogramação.

Arquivo: RM.Prj.Projeto.Data.dll

## 12.1.2602.101

### Rotina: MONITOR DE OBRAS

* **[Ticket: 25274168 / TOPEXECONTROL01-30103]** Ajuste nas mensagens do Portal.

Arquivo: Prj/portal-pedidos-monitor

### Rotina: PERT

* **[Ticket: TOPORCAPLAN001-29136]** Exportar Pert para Cronograma - Aumentar campo cronograma

Arquivos: RM.Prj.Classes.Intf.dll; RM.Prj.Cronograma.Server.dll

## 12.1.2602.102

### Rotina: PERT

* **[Ticket: TOPORCAPLAN001-29136]** Exportar Pert para Cronograma - Aumentar campo cronograma

Arquivos: RM.Prj.Classes.Intf.dll; RM.Prj.Cronograma.Server.dll

## 12.1.2602.103

### Rotina: PLANILHA EXECUTIVA

* **[Ticket: 26450114 / TOPEXECONTROL01-30547]** Ajuste ao exportar dados da planilha executiva para o cronograma realizado quando a grandeza parametrizada for diferente de valor.

Arquivo: RM.Prj.Planilhas.Server.dll

## 12.1.2602.104

### Rotina: APROPRIAÇÃO

* **[Ticket: 25480019 / TOPEXECONTROL01-30111]** Importar apropriação do backoffice retornando registros duplicados em cada execução

Arquivos: RM.Prj.Integracao.Intf.dll; RM.Prj.Integracao.Server.dll; RM.Prj.TotvsMessage.Adapter.dll

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: TOPORCAPLAN001-29591]** Disponibilização no cadastro de Contratos dos campos "Indicativo de Prestação de Serviços" e "Tipo de Projeto"

Arquivos: RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.Data.dll; RM.Prj.Utils.Server.dll; RM.Prj.Utils.Intf.dll; RM.Prj.Contrato.Intf.dll

## 12.1.2602.106

### Rotina: ADITIVO

* **[Ticket: 26499352 / TOPORCAPLAN001-29663]** Ajuste na alteração de itens de aditivo quando chamados via webservice.

Arquivos: RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.IServer.dll; RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Intf.dll

## 12.1.2602.110

### Rotina: EQUIPE

* **[Ticket: 26031059 / TOPEXECONTROL01-30323]** Ao adicionar Membros de Mobilidade como terceiro através de Processos/Inclusão de Membro(s)o a inclusão ocorrerá normalmente

Arquivo: RM.Prj.EquipeProjeto.Data.dll

## 12.1.2602.111

### Rotina: APROPRIAÇÃO

* **[Ticket: 26523153 / TOPEXECONTROL01-30607]** Ajuste no processo de importar apropriações do backoffice quando não erá usada toda a planilha e existiam trasferências em tarefas fora do intervalo selecionado.

Arquivo: RM.Prj.Apropriacao.Server.dll

### Rotina: PEDIDOS EXTRAS

* **[Ticket: 25285700 / TOPEXECONTROL01-30028]** Criação do campo Observação no Pedido e Pedido Extra no portal-pedidos-monitor.

Arquivo: Prj/portal-pedidos-monitor

* **[Ticket: 25285700 / TOPEXECONTROL01-30028]** Ajuste campo de observação no Pedido e Pedio Extra

Arquivo: Prj/portal-pedidos-monitor

### Rotina: PLANILHA

* **[Ticket: 26672215 / TOPORCAPLAN001-29762]** incluir uma nova tarefa - Planilha de atividade

Arquivo: RM.Prj.Planilhas.Form.dll

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-29730]** Ajustes do Sincronismo na 2602.

Arquivos: RM.Prj.Projeto.Intf.dll; RM.Prj.Projeto.Form.dll; RM.Prj.Composicao.Data.dll; RM.Prj.Projeto.Data.dll; RM.Prj.Insumo.Data.dll; RM.Prj.Insumo.Intf.dll; RM.Prj.Composicao.Intf.dll; RM.Prj.Insumo.Form.dll; RM.Prj.Composicao.Form.dll

## 12.1.2602.112

### Rotina: SMART VIEW (TREPORTS)

* **[Ticket: TOPEXECONTROL01-30433]** Relatórios Suprimentos - Smart View dentro do TCOP

Arquivo: RM.Prj.Relatorios.Form.dll

## 12.1.2602.113

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 25449607 / TOPORCAPLAN001-29790]** Inclusão do campo de Contratado Atual e ajuste do campo Contratado Inicial em contratos.

Arquivos: RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.IServer.dll; RM.Prj.PedidoMaterial.Data.dll; RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.PedidoMaterial.Server.dll

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-29730]** Ajuste na carga de tarefas no processo de sincronismo de RR.

Arquivo: RM.Prj.Projeto.Form.dll

* **[Ticket: TOPORCAPLAN001-29730]** Ajustes do Sincronismo de RR ao salvar controle de revisão.

Arquivo: RM.Prj.Projeto.Data.dll

## 12.1.2602.114

### Rotina: CRONOGRAMA

* **[Ticket: 26588863 / TOPORCAPLAN001-29801]** Ajuste no cálculo de gandezas do cronograma quando utilizado vigência de preços.

Arquivo: RM.Prj.Cronograma.Server.dll

### Rotina: DIÁRIO DE OBRA (RDO)

* **[Ticket: 26600191 / TOPORCAPLAN001-29735]** Cadastro de Grupos de Usuário no Diário de Obra

Arquivos: RM.Prj.Rest.Server.dll; Prj/minhasinspecoes; RM.Prj.Menu.dll

### Rotina: PLANILHA

* **[Ticket: 26672215 / TOPORCAPLAN001-29762]** Ajuste ao incluir uma tarefa na planilha de atividades e deslocar o código das próximas tarefas

Arquivos: RM.Prj.Planilhas.Data.dll; RM.Prj.Tarefa.Intf.dll; RM.Prj.Planilhas.Form.dll; RM.Prj.Tarefa.Data.dll

### Rotina: PORTAL DE MEDIÇÃO DE CONTRATOS PARA FORNECEDORES

* **[Ticket: 26526123 / TOPORCAPLAN001-29720]** Ajuste ao cancelar a liberação de um período com estorno para continuar com status "Liberado", se não tiver período de estorno, o status de período deve voltar para "Em liberação".

Arquivos: RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Intf.dll

## 12.1.2602.115

### Rotina: COCKPIT DE TAREFAS E INSUMOS

* **[Ticket: TOPEXECONTROL01-30509]** Ajuste no valor apropriado das tarefas no cockpit.

Arquivos: RM.Prj.Tarefa.Intf.dll; RM.Prj.Tarefa.Data.dll; RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Data.dll

## 12.1.2602.116

### Rotina: DIÁRIO DE OBRA (RDO)

* **[Ticket: 26600191 / TOPORCAPLAN001-29735]** Cadastro de Grupos de Usuário no Diário de Obra

Arquivo: Prj/portaldaobra

### Rotina: PORTAL DE MEDIÇÃO DE CONTRATOS PARA FORNECEDORES

* **[Ticket: 26526123 / TOPORCAPLAN001-29720]** Adiciona enumeração 'CancelamentoLiberacao' ao PeriodoStatusHistoricoEnum e atualiza o método switchCase para incluir novo status no componente TelaHistorico.

Arquivo: Prj/portal-contrato-fornecedor

## 12.1.2602.117

### Rotina: Sem Rotina Específica

* **[Ticket: TOPORCAPLAN001-19648]** Ajuste na leitura de dados de contratos.

Arquivo: RM.Prj.Contrato.Data.dll

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 25449607 / TOPORCAPLAN001-29790]** Ajuste no cálculo de valores de aditivos contratuais quando existe medição com preço liberado diferentes.

Arquivos: RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.Server.dll

* **[Ticket: 25449607 / TOPORCAPLAN001-29790]** Ajuste nos totalizadores de obras e etapas no relatório de Histograma de Insumos.

Arquivo: RM.Prj.Relatorios.Form.dll

* **[Ticket: 25449607 / TOPORCAPLAN001-29790]** Ajuste no cálculo de valores de aditivos contratuais quando existe medição com preço liberado diferente do atual.

Arquivos: RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.Contrato.IServer.dll; RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Data.dll

* **[Ticket: 26980860 / TOPORCAPLAN001-29914]** Ajuste na leitura de dados de contratos.

Arquivos: RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.IServer.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.Contrato.Server.dll

### Rotina: DIÁRIO DE OBRA (RDO)

* **[Ticket: 26600191 / TOPORCAPLAN001-29735]** Cadastro de Grupos de Usuário no Diário de Obra

Arquivos: RM.Prj.MinhaQualidade.Server.dll; Prj/minhasinspecoes

### Rotina: RELATÓRIOS PERIÓDICOS

* **[Ticket: 26564000 / TOPORCAPLAN001-29736]** Ajuste nos totalizadores de obras e etapas no relatório de Histograma de Insumos.

Arquivo: RM.Prj.Relatorios.Server.dll

### Rotina: SMART VIEW (TREPORTS)

* **[Ticket: TOPEXECONTROL01-30433]** Relatórios Suprimentos - Smart View dentro do TCOP

Arquivo: RM.Prj.Mobilidade.Form.dll

## 12.1.2602.120

### Rotina: FATURAMENTO DIRETO

* **[Ticket: 26888626 / TOPORCAPLAN001-29885]** Calculo do Contrato após associar objetos e validação de saldo de faturamento direto no server.

Arquivos: RM.Prj.Contrato.IServer.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Form.dll

## 12.1.2602.121

### Rotina: PROTHEUS EAI 2.0

* **[Ticket: 26342847 / TOPEXECONTROL01-30639]** Ajuste ao enviar retenção para o Protheus com rateio de municipio.

Arquivo: RM.Prj.Contrato.Data.dll

## 12.1.2602.123

### Rotina: Sem Rotina Específica

* **[Ticket: TOPORCAPLAN001-19648]** Otimização e adequação dos fontes do sistema

Arquivo: RM.Prj.Mobilidade.Data.dll

### Rotina: FOLHA DE PRODUTIVIDADE

* **[Ticket: 26322711 / TOPEXECONTROL01-30462]** Não gerar msg ao não ter dados para gerar arquivo de pagamento de produtividade

Arquivos: RM.Prj.Mobilidade.Server.dll; RM.Prj.Mobilidade.Intf.dll; RM.Prj.Mobilidade.Data.dll

## 12.1.2602.124

### Rotina: LIBERAÇÃO / INTEGRAÇÃO COM SUPRIMENTOS/FATURAMENTO

* **[Ticket: 26646009 / TOPORCAPLAN001-29853]** Ajuste na tela de associar faturamento direto do processo de liberação de período.

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: PLANILHA

* **[Ticket: 26750422 / TOPORCAPLAN001-29800]** Ajuste no tamanho dos campos de descrição de Unidade e Local de Serviço.

Arquivos: RM.Prj.Cadastros.Form.dll; RM.Prj.Cadastros.Intf.dll; RM.Prj.Cadastros.Data.dll

### Rotina: PROTHEUS EAI 2.0

* **[Ticket: 26342847 / TOPEXECONTROL01-30639]** Ajuste ao enviar retenção para o Protheus com rateio de municipio.

Arquivo: RM.Prj.Contrato.Data.dll

## 12.1.2602.125

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 27060939 / TOPORCAPLAN001-29941]** Ajuste nos cálculos de grandezas de cronograma quando o projeto utiliza vigência de preço.

Arquivos: RM.Prj.Cronograma.Server.dll; RM.Prj.Calculo.Data.dll; RM.Prj.Cronograma.IService.dll; RM.Prj.Calculo.Server.dll; RM.Prj.Calculo.Form.dll; RM.Prj.Cronograma.Data.dll; RM.Prj.Calculo.Intf.dll; RM.Prj.Cronograma.Intf.dll; RM.Prj.Cronograma.Form.dll

### Rotina: CURVAS

* **[Ticket: 26966433 / TOPORCAPLAN001-30001]** Ajuste no relatório de Histograma de Insumos por Tarefa - por Valor no campo Quantidade do Insumo.

Arquivo: RM.Prj.Relatorios.Form.dll

### Rotina: RELATÓRIOS BOOK

* **[Ticket: 26846777 / TOPORCAPLAN001-29818]** TCOP - Relatório Itens do Contrato trazendo todos os contratos do projeto

Arquivo: RM.Prj.Relatorios.Form.dll

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-29867]** Ajuste nos processos de sincronismo e aplicação de Revisão de Reprogramação após testes iniciais no cliente.

Arquivos: RM.Prj.Tarefa.Data.dll; RM.Prj.Cronograma.Intf.dll; RM.Prj.Insumo.Data.dll; RM.Prj.Cronograma.Form.dll; RM.Prj.Cronograma.Data.dll; RM.Prj.Tarefa.Intf.dll; RM.Prj.Projeto.Intf.dll; RM.Prj.Projeto.Data.dll; RM.Prj.Tarefa.Form.dll; RM.Prj.Calculo.Server.dll; RM.Prj.Projeto.Form.dll; RM.Prj.Cronograma.Server.dll

## 12.1.2602.127

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 27163509 / TOPORCAPLAN001-30029]** Ajuste na consulta de insumos relacionados com a curva S.

Arquivo: RM.Prj.Insumo.Data.dll

### Rotina: PERT

* **[Ticket: 26694184 / TOPEXECONTROL01-30576]** Correção do filtro de datas no diagrama de Gantt

Arquivo: Prj/portaldaobra

### Rotina: PORTAL DE MEDIÇÃO DE CONTRATOS PARA FORNECEDORES

* **[Ticket: 26314504 / TOPORCAPLAN001-29832]** ao Finalizar Medição - Portal de Medição

Arquivo: RM.Prj.Contrato.Data.dll

* **[Ticket: TOPORCAPLAN001-29879]** Ajuste ao liberar o período no portal de medição para atualizar o valor retido.

Arquivo: RM.Prj.Contrato.Server.dll

## 12.1.2602.129

### Rotina: Sem Rotina Específica

* **[Ticket: 27016158 / TOPORCAPLAN001-29951]** melhoria en el calculo de proyecto

Arquivo: RM.Prj.Planilhas.Intf.dll

### Rotina: ADITIVO

* **[Ticket: TOPORCAPLAN001-29833]** Validação de saldo de faturamento direto e adiantamentos em relação ao saldo do contrato.

Arquivos: RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.Server.dll; RM.Prj.IntegracaoEcmWF.Data.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.IntegracaoEcmWF.Intf.dll; RM.Prj.Contrato.Form.dll; RM.Prj.IntegracaoEcmWf.Form.dll

### Rotina: PROTHEUS EAI 2.0

* **[Ticket: 25926197 / TOPEXECONTROL01-30300]** Ajuste para que o valor da dedução de contratos a receber seja enviada como desconto em integração com Protheus

Arquivos: RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Data.dll

## 12.1.2602.130

### Rotina: ADITIVO

* **[Ticket: TOPORCAPLAN001-29833]** Validação de saldo de faturamento direto e adiantamentos em relação ao saldo do contrato.

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: APROPRIAÇÃO

* **[Ticket: 26943254 / TOPEXECONTROL01-30687]** Ajuste para que ao contabilizar a quantidade horas improdutivas rateadas para terceiros, sejam consideradas corretamente a quantidade de horas apropriadas.

Arquivos: RM.Prj.EquipeProjeto.Form.dll; RM.Prj.Mobilidade.Server.dll

### Rotina: CURVAS

* **[Ticket: 27213872 / TOPORCAPLAN001-30060]** Cálculo de HISTORGRAMA codificação performance

Arquivo: RM.Prj.Relatorios.Server.dll

### Rotina: DIÁRIO DE OBRA (RDO)

* **[Ticket: TOPORCAPLAN001-30050]** Implementado um novo componente de texto formatado (rich text) para permitir a edição de texto com formatação e imagens.

Arquivo: Prj/minhasinspecoes

## 12.1.2602.131

### Rotina: DIÁRIO DE OBRA (RDO)

* **[Ticket: TOPORCAPLAN001-30050]** Criação do tipo de questão texto formatado (rich text) no cadastro de formulário de inspeção/diário de obra.

Arquivo: RM.Prj.MinhaQualidade.Intf.dll

### Rotina: SMART VIEW (TREPORTS)

* **[Ticket: 27145094 / TOPORCAPLAN001-30039]** Ajuste na validação de conector de repositório de arquivos não sendo necessário para inspeções.

Arquivos: RM.Prj.NativeProvider.Service.dll; RM.Prj.Utils.Intf.dll; RM.Prj.Utils.Server.dll

## 12.1.2602.133

### Rotina: COMPOSIÇÃO

* **[Ticket: 27105831 / TOPORCAPLAN001-30002]** Ajuste no processo de exclusão de composições não utilizadas.

Arquivo: RM.Prj.Composicao.Data.dll

### Rotina: FATURAMENTO DIRETO

* **[Ticket: 27178125 / TOPORCAPLAN001-30061]** Envio de pedido de faturamento direto ao Suprimentos/Faturamento

Arquivos: RM.Prj.PedidoMaterial.Data.dll; RM.Prj.PedidoMaterial.Form.dll; RM.Prj.Menu.dll; RM.Prj.Contrato.Form.dll; RM.Prj.Api.dll

## 12.1.2602.134

### Rotina: ADITIVO

* **[Ticket: TOPORCAPLAN001-29773]** Melhoria no processo de geração de contratos a partir de movimentos

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: FATURAMENTO DIRETO

* **[Ticket: 27178125 / TOPORCAPLAN001-30061]** Envio de pedido de faturamento direto ao Suprimentos/Faturamento

Arquivos: RM.Prj.PedidoMaterial.Form.dll; RM.Prj.Api.dll; RM.Prj.Contrato.Form.dll; RM.Prj.PedidoMaterial.Data.dll; RM.Prj.Menu.dll

## 12.1.2602.135

### Rotina: DIÁRIO DE OBRA (RDO)

* **[Ticket: TOPORCAPLAN001-30050]** Remove o botão de imagem no RichText.

Arquivo: Prj/minhasinspecoes

### Rotina: PROTHEUS EAI 2.0

* **[Ticket: 26409545 / TOPEXECONTROL01-30714]** Ajuste no webservice WSGGPE para integração com a Folha de Pagamento do Protheus.

Arquivo: RM.Prj.Utils.Intf.dll

## 12.1.2602.136

### Rotina: APROPRIAÇÃO

* **[Ticket: 26963055 / TOPEXECONTROL01-30690]** Ajuste importação apropriação do BackOffice

Arquivo: RM.Prj.Apropriacao.Server.dll

## 12.1.2602.137

### Rotina: Sem Rotina Específica

* **[Ticket: 26762079 / TOPEXECONTROL01-30620]** Ajuste no valor total por periodo do Relatório SmartView Cronograma de Compras.

Arquivos: RM.Prj.NativeProvider.Service.dll; RM.Prj.Projeto.Data.dll

### Rotina: APROPRIAÇÃO

* **[Ticket: 26943254 / TOPEXECONTROL01-30804]** Ajuste no reateio e revaloração de mão de obra quando um terceiro é inativado e outro cadastrado usando o mesmo funcionário.

Arquivo: RM.Prj.Mobilidade.Server.dll

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: TOPORCAPLAN001-29978]** Ajustes no cálculo do cronograma na existência de vigência.

Arquivo: RM.Prj.Calculo.Server.dll

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-30059]** Ajustes em todo o processo de Revisão de Reprogramação atendendo aos testes do cliente.

Arquivos: RM.Prj.Projeto.Data.dll; RM.Prj.Projeto.Intf.dll; RM.Prj.Contrato.Data.dll; RM.Prj.Facade.dll; RM.Prj.Planilhas.Data.dll; RM.Prj.Projeto.Form.dll

## 12.1.2602.143

### Rotina: PEDIDO DE MATERIAL EXTRA

* **[Ticket: TOPEXECONTROL01-30877]** Geração de movimento Acordo - Pedido Extra

Arquivo: RM.Prj.PedidoMaterial.Server.dll

## 12.1.2602.144

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 26965164 / TOPORCAPLAN001-30245]** Ajuste no cálculo de contratos para quando existir reajustes e aditivos.

Arquivos: RM.Prj.Contrato.Intf.dll; RM.Prj.Contrato.IServer.dll; RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Data.dll

### Rotina: MEDIÇÃO

* **[Ticket: 27931154 / TOPORCAPLAN001-30313]** Ajuste na validação de medições, utilização e parâmetro de projetos.

Arquivo: RM.Prj.Contrato.Form.dll

## 12.1.2602.145

### Rotina: ANÁLISE DE VALOR AGREGADO

* **[Ticket: 26753761 / TOPEXECONTROL01-30659]** Ajustes funções de fórmulas.

Arquivo: RM.Prj.Formula.dll

### Rotina: FATURAMENTO DIRETO

* **[Ticket: 27594795 / TOPORCAPLAN001-30329]** Ajuste no cálculo de contrato para tratar contratos de insumos com aditivos e reajustes.

Arquivos: RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.BackupRestore.Data.dll; RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.Data.dll; RM.Prj.Contrato.IServer.dll

### Rotina: PROTHEUS EAI 2.0

* **[Ticket: 26736608 / TOPEXECONTROL01-30637]** Ajuste para que no sincronismo de projeto com o protheus, todos os status sejam considerados para enviar a mensagem.

Arquivo: RM.Prj.TotvsMessage.Adapter.dll

* **[Ticket: 27351428 / TOPEXECONTROL01-30803]** Ajuste para que sejá possível cancelar a liberação de retenção contratual que por alguma inconsistência tiver sido liberada sem gerar movimento, possibilitando assim uma nova liberação.

Arquivos: RM.Prj.Contrato.Form.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.Contrato.Data.dll

* **[Ticket: 27351428 / TOPEXECONTROL01-30803]** Mensagem desnecessária foi removida

Arquivo: RM.Prj.Contrato.Form.dll

## 12.1.2602.149

### Rotina: CRONOGRAMA DE DESEMBOLSO

* **[Ticket: 27897396 / TOPORCAPLAN001-30338]** Ajuste na carga de cache de cálculo de cronograma para melhoria de performance.

Arquivo: RM.Prj.Calculo.Server.dll

## 12.1.2602.150

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: TOPEXECONTROL01-30974]** Ajuste de validação ao executar processo de cancelamento de liberação de retenção

Arquivo: RM.Prj.Contrato.Form.dll

### Rotina: REVISÃO

* **[Ticket: TOPEXECONTROL01-31014]** Ajuste no processo de gerar revisão de projetos

Arquivo: RM.Prj.Projeto.Data.dll

## 12.1.2602.151

### Rotina: LIBERAÇÃO / INTEGRAÇÃO COM SUPRIMENTOS/FATURAMENTO

* **[Ticket: TOPORCAPLAN001-30423]** Ajuste na regra de validação do status de documentos do TAE para cenários com documentos cancelados.

Arquivo: RM.Prj.Facade.dll

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-30433]** Ajuste na cópia de itens da planilha executiva ao gerar revisão de reprogramação.

Arquivos: RM.Prj.Projeto.Data.dll; RM.Prj.Projeto.Form.dll; RM.Prj.Projeto.Intf.dll

## 12.1.2602.152

### Rotina: CÁLCULO

* **[Ticket: 28082063 / TOPEXECONTROL01-31054]** Pedido material - Diferença de arredondamento entre curva ABC e S

Arquivo: RM.Prj.PedidoMaterial.Server.dll

### Rotina: PEDIDO DE MATERIAL

* **[Ticket: TOPEXECONTROL01-30737]** Agora, gerar movimento por data a partir de um pedido de material extra está disponível para todos os projetos

Arquivo: RM.Prj.PedidoMaterial.Form.dll

### Rotina: PORTAL DE MEDIÇÃO DE CONTRATOS PARA FORNECEDORES

* **[Ticket: TOPORCAPLAN001-30447]** informar o fornecedor no portal de medição

Arquivo: RM.Prj.Contrato.Server.dll

## 12.1.2602.154

### Rotina: LIBERAÇÃO / INTEGRAÇÃO COM SUPRIMENTOS/FATURAMENTO

* **[Ticket: 28355737 / TOPORCAPLAN001-30538]** Melhoria na tela de liberação de período

Arquivo: RM.Prj.Contrato.Form.dll

## 12.1.2602.158

### Rotina: CRONOGRAMA

* **[Ticket: 28452871 / TOPEXECONTROL01-31120]** Edição de qtd de pedido com curva S para tarefas de valor cotado

Arquivo: RM.Prj.PedidoMaterial.Server.dll

### Rotina: LIBERAÇÃO / INTEGRAÇÃO COM SUPRIMENTOS/FATURAMENTO

* **[Ticket: 28355737 / TOPORCAPLAN001-30538]** Melhoria na tela de liberação de período

Arquivo: RM.Prj.Contrato.Form.dll

## 12.1.2602.159

### Rotina: APP MINHAS INSPEÇÕES

* **[Ticket: 27896085 / TOPORCAPLAN001-30545]** Ajuste ao responder uma inspeção sem conexão com a internet.

Arquivo: RM.Prj.MinhaQualidade.Server.dll

### Rotina: LIBERAÇÃO / INTEGRAÇÃO COM SUPRIMENTOS/FATURAMENTO

* **[Ticket: 28355737 / TOPORCAPLAN001-30538]** Melhoria na tela de liberação de período

Arquivo: RM.Prj.Contrato.Form.dll

## 12.1.2602.162

### Rotina: ORCECRTO / BIM

* **[Ticket: 27003364 / TOPORCAPLAN001-30069]** Melhoria na tela de liberação de período

Arquivo: RM.Prj.Projeto.Form.dll

### Rotina: REVISÃO MÚLTIPLA

* **[Ticket: TOPORCAPLAN001-30059]** Ajuste na validação preços aptos para o cálculo de tarefas em projetos com vigência.

Arquivo: RM.Prj.Calculo.Server.dll

## 12.1.2602.163

### Rotina: ADITIVO

* **[Ticket: 28235807 / TOPORCAPLAN001-30578]** Melhorias no processo de inclusão de aditivo

Arquivo: RM.Prj.Contrato.Server.dll

* **[Ticket: 28686780 / TOPORCAPLAN001-30599]** Melhoria de desempenho no cadastro de aditivos de contrato.

Arquivos: RM.Prj.Parametros.Data.dll; RM.Prj.Contrato.Data.dll; RM.Prj.Facade.dll; RM.Prj.Projeto.Data.dll; RM.Prj.Calculo.Server.dll; RM.Prj.Orcamento.Data.dll; RM.Prj.Importacao.Data.dll; RM.Prj.Planilhas.Data.dll; RM.Prj.Classes.Server.dll

## 12.1.2602.169

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 28540194 / TOPORCAPLAN001-30590]** Ajuste no cálculo de contrato e aditivos de contrato quando existir reajuste de itens.

Arquivos: RM.Prj.Contrato.Data.dll; RM.Prj.BackupRestore.Data.dll; RM.Prj.Projeto.Data.dll; RM.Prj.Contrato.Server.dll

## 12.1.2602.170

### Rotina: MEDIÇÃO

* **[Ticket: TOPORCAPLAN001-30615]** Melhorias no anexo de itens medidos do contrato

Arquivo: RM.Prj.Contrato.Data.dll

### Rotina: PLANILHA

* **[Ticket: 28301055 / TOPORCAPLAN001-30639]** Melhorias no anexo de cronograma da planilha de atividades

Arquivo: RM.Prj.Cronograma.Data.dll

## 12.1.2602.173

### Rotina: CRIAÇÃO / ASSOCIAÇÃO / CÁLCULO

* **[Ticket: 28429021 / TOPORCAPLAN001-30640]** Ajuste no realinhamento de itens de contrato para salvar o valor realinhado que deve ser considerado no cálculo.

Arquivos: RM.Prj.Contrato.IServer.dll; RM.Prj.Contrato.Server.dll; RM.Prj.Contrato.Intf.dll; RM.Prj.Contrato.Data.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 27988814 / TOPORCAPLAN001-30585]** Correção na importação via excel

Arquivo: RM.Prj.Importacao.Form.dll

## 12.1.2602.175

### Rotina: ANÁLISE DE VALOR AGREGADO

* **[Ticket: 28170188 / TOPEXECONTROL01-31121]** Ajuste no processo de gerar Análise do Valor Agregado

Arquivo: RM.Prj.AnaliseDeValorAgregado.Data.dll

# TOTVS Controle de Infecção Hospitalar

## 12.1.2602.117

### Rotina: Sem Rotina Específica

* **[Ticket: 26711554 / DSAUCLINICA-14371]** Ajuste na rotina de importação de antibióticos para validar pedidos que possuam mais de um antibiótico com indicações distintas. Ao identificar a situação, o sistema exibirá uma orientação para validação das indicações em Paciente > Interação > Antibiótico.

Arquivo: RM.SauIH.Importacao.Data.dll

* **[Ticket: 26711341 / DSAUCLINICA-14372]** Foram adicionadas políticas de permissão na tela de materiais de cultura, permitindo ao administrador definir se o perfil do usuário pode incluir e/ou excluir esses materiais.

Arquivo: RM.SauIH.Server.dll

## 12.1.2602.133

### Rotina: ANALISE DE ANTIMICROBIANOS - VISÃO

* **[Ticket: 27229250 / DSAUCLINICA-14519]** Foi realizado um ajuste no BI do componente cirúrgico, corrigindo o comportamento dos filtros e da exibição das informações. Com isso, agora é possível aplicar os filtros corretamente e visualizar os dados conforme esperado.

Arquivos: RM.SauIH.Estatisticos.Intf.dll; RM.SauIH.Paciente.Intf.dll; RM.SauIH.Estatisticos.Data.dll

* **[Ticket: 27229250 / DSAUCLINICA-14519]** Ajuste no cadastro de cirurgia: ao possuir especialidade vinculada, a tentativa de salvamento gerava uma mensagem não tratada. O comportamento foi corrigido permitindo ao usuário salvar a cirurgia.

Arquivo: RM.SauIH.Paciente.Data.dll

## 12.1.2602.163

### Rotina: Sem Rotina Específica

* **[Ticket: 28482303 / DSAUCLINICA-14753]** Ajuste na importação de cirurgias no módulo de Controle de Infecção Hospitalar: ao importar uma cirurgia, o sistema passará a preencher automaticamente o cirurgião responsável pelo procedimento, conforme definido no registro da cirurgia.

Arquivo: RM.SauIH.Importacao.Data.dll

# TOTVS Educacional

## 12.1.2602.100

### Rotina: Sem Rotina Específica

* **[Ticket: DEDUPACMEN-8105]** Ajuste na visibilidade da funcionalidade de tabela de preço

Arquivos: RM.Edu.Financeiro.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Utils.Server.dll; RM.Edu.Menu.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11073]** Alterações de log no processo de Preparação do Censo Superior

Arquivos: RM.Edu.Academico.Data.dll; RM.Edu.Professor.Form.dll; RM.Edu.Academico.Server.dll; RM.Edu.PeriodoLetivo.Server.dll

* **[Ticket: DEDUBOPE-11073]** Criadas novas regras de validação e novos campos relativos ao Arquivo 32 do Censo Superior

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-9707]** Ajustes para remover as colunas repetidas nos ites do filtro avançado

Arquivo: RM.Edu.Services.Server.dll

### Rotina: FREQUÊNCIA

* **[Ticket: DEDUSAGA-10262]** Ajuste no alinhamento dos campos de "Somatório de Notas" e "Nº de Aulas Dada" da tela de notas e faltas de etapa

Arquivo: Edu/portaldoprofessor

* **[Ticket: DEDUSAGA-10262]** Correção na exibição da barra de rolagem horizontal nas telas de Frequência Diária, Notas de Avaliação e Notas e Faltas por Etapa.

Arquivo: Edu/portaldoprofessor

### Rotina: LOGIN

* **[Ticket: 26283369 / DEDUSAGA-10184]** ajuste para não fazer cache dos arquivos de tradução

Arquivo: Edu/portaldoprofessor

* **[Ticket: 26283369 / DEDUSAGA-10184]** ajuste para alterar o título da aba do browser de acordo com a expressão appName cadastrada no portal do professor

Arquivo: Edu/portaldoprofessor

### Rotina: PROFESSORES

* **[Ticket: DEDUBOPE-11390]** Ajustes no cadastro de disciplinas do professor para adição dos campos que indicam professor Apto ou Autorizado a lecionar a disciplina.

Arquivos: RM.Edu.Professor.Intf.dll; RM.Edu.Professor.Data.dll; RM.Edu.PeriodoLetivo.Data.dll; RM.Edu.Professor.Server.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.dll; RM.Edu.Professor.Form.dll; RM.Edu.Utils.Server.dll; RM.Edu.Interfaces.Intf.dll

### Rotina: TOTVS ASSINATURA ELETRÔNICA

* **[Ticket: 26442925 / DEDUSAGA-10239]** Ajuste no busca de destinatários (secretários da instituição) para o envio de assinaturas do diário de classe para o TAE

Arquivos: RM.Edu.Cadastros.Server.dll; RM.Edu.TotvsSign.Server.dll; RM.Edu.Interfaces.Intf.dll

## 12.1.2602.101

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11414]** Adicionada regra de integridade no cadastro de alunos para validar a cidade informada contra a tabela de municípios e estado do sistema, bem como a validação de o campo de cidade foi preenchido.

Arquivos: RM.Edu.Interfaces.Intf.dll; RM.Edu.Aluno.Data.dll; RM.Edu.Aluno.Form.dll; RM.Edu.Facade.dll; RM.Edu.Aluno.Server.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11075]** Inclusão dos campos novos de Mediador para o Censo Superior.

Arquivos: RM.Edu.Academico.Server.dll; RM.Edu.Utils.Server.dll; RM.Edu.Cadastros.Intf.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Cadastros.Data.dll; RM.Edu.PeriodoLetivo.Data.dll; RM.Edu.Academico.Form.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.Cadastros.Form.dll; RM.Edu.PeriodoLetivo.Intf.dll

### Rotina: GESTÃO DE MENSAGENS

* **[Ticket: DEDUSAGA-9503]** Ajuste no comportamento responsável por criar nova conversa ao enviar um comunicado nas mensagens pessoais do Meu EduConnect.

Arquivos: RM.Edu.API.dll; RM.Edu.Mensagens.Server.dll

### Rotina: LOGIN

* **[Ticket: DEDUSAGA-10241]** Habilitar a tecla 'Enter' na tela de login do Portal do Aluno para disparar a ação do botão 'Entrar'.

Arquivo: Edu/portaleducacional

### Rotina: NOTAS E FALTAS DE ETAPA

* **[Ticket: 25228941 / DEDUSAGA-9774]** alteração para enviar separado as notas e faltas. Antes enviava tudo em um objeto apenas ficando difícil saber quando a alteração feita era em falta ou nota, desta forma as validações de etapa eram executadas para os dois casos mesmo que a alteração tinha sido feita apenas em nota ou falta

Arquivos: RM.Edu.API.dll; Edu/portaldoprofessor

* **[Ticket: 25228941 / DEDUSAGA-9774]** ajuste para atualizar as aulas dadas de cada linha ao alterar o número de aulas dadas da etapa

Arquivo: Edu/portaldoprofessor

## 12.1.2602.103

### Rotina: TURMAS E TURMAS / DISCIPLINAS

* **[Ticket: 26481432 / DEDUBOPE-11457]** Aprimoramos na busca de professores durante o processo de associação de horários.

Arquivos: RM.Edu.Lib.Server.dll; RM.Edu.PeriodoLetivo.Server.dll

## 12.1.2602.104

### Rotina: INSCRIÇÕES

* **[Ticket: DEDUPACMEN-6939]** Atualização da API v2 do PIX no portal do Processo Seletivo

Arquivo: Edu/portalprocessoseletivo

### Rotina: LOGIN

* **[Ticket: 25713173 / DEDUSAGA-10074]** Adição da validação da existência do RA do aluno para exibir alertas de atividades acadêmicas.

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

## 12.1.2602.105

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: DEDUPACMEN-8431]** Ajuste código indicador da operação para reforma tributária

Arquivos: RM.Edu.Financeiro.Server.dll; RM.Edu.Consts.dll

## 12.1.2602.106

### Rotina: ALOCAR HORÁRIO E PROFESSOR

* **[Ticket: DEDUBOPE-8283]** Nova funcionadalode para adiciona alocação de multiplos horarios para a mesma turma disc

Arquivos: RM.Edu.API.dll; RM.Edu.Lib.Intf.dll

* **[Ticket: DEDUBOPE-8283]** Nova funcionalidade de seleção de horários e alocação de turma-disc na etapa de alocação de horários e professores no modulo de gestão de ofertas - PGE

Arquivo: Edu/portalgestaoeducacional

### Rotina: ASSINATURA DE DIÁRIO DE CLASSE

* **[Ticket: 26609189 / DEDUSAGA-10309]** Ajuste para permitir a assinatura do diário de classe no Portal do Professor, para turma/disciplina gerencial sem matriz aplicada.

Arquivos: RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.MatrizCurricular.Server.dll; RM.Edu.TotvsSign.Server.dll; RM.Edu.TotvsSign.Intf.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11072]** Evolução continua no processo de cadastro dos dados do censo.

Arquivos: RM.Edu.Professor.Data.dll; RM.Edu.Professor.Form.dll

* **[Ticket: DEDUBOPE-11377]** Otimização na consulta dos registro 31 e 91 do censo superior.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: FALE COM A INSTITUIÇÃO

* **[Ticket: DEDUSAGA-10234]** Otimização dos filtros da tela de mensagens: a busca por aluno ou mensagens não lidas agora percorre todo o histórico, em vez de se limitar apenas aos itens exibidos na tela.

Arquivos: RM.Edu.Mensagens.Server.dll; RM.Edu.API.dll

## 12.1.2602.107

### Rotina: ALOCAR HORÁRIO E PROFESSOR

* **[Ticket: DEDUBOPE-8283]** Melhoria em avisos de nova funcionalidade de seleção de horários e alocação de turma-disc na etapa de alocação de horários e professores no módulo de gestão de ofertas - PGE

Arquivo: Edu/portalgestaoeducacional

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11445]** Adequação das alterações no layout de exportação da situação do aluno para o Censo Básico.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11073]** Melhoria continua no processo de cadastro dos dados do censo do Professor

Arquivo: RM.Edu.Professor.Data.dll

### Rotina: PAGAMENTO TOTVS TPC

* **[Ticket: DEDUPACMEN-8404]** Ajuste para build do Educacional com o pacote atualizado do edu-elements

Arquivo: Edu/portaleducacional

* **[Ticket: DEDUPACMEN-8404]** Atualização nas mensagens de recusa nos pagamentos via TPC

Arquivo: Edu/portalprocessoseletivo

## 12.1.2602.108

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11073]** Inclusão dos campos novos de Mediador para o Censo Superior.

Arquivos: RM.Edu.Cadastros.Form.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Cadastros.Data.dll; RM.Edu.Cadastros.Intf.dll

## 12.1.2602.109

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11073]** Inclusão dos campos novos de Mediador para o Censo Superior.

Arquivo: RM.Edu.Professor.Form.dll

### Rotina: SERVIÇOS

* **[Ticket: 26681965 / DEDUPACMEN-8464]** Foi ajustado o tamanho do campo REGRATRIBUTARIADESCRICAO para 255, de modo a refletir o real tamanho do campo da tabela DREGRATRIBUTARIA do fiscal.Com o tamanho antigo, se fosse informada uma descrição com mais de 150 caracteres no fiscal, a visão do serviço não tinha o comportamento esperado, o que impossibilitava ser atualizada.O ajuste foi feito para o serviço e histórico do serviço.

Arquivo: RM.Edu.Financeiro.Intf.dll

## 12.1.2602.110

### Rotina: CADASTRAR OCORRÊNCIAS PARA OS ALUNOS

* **[Ticket: 25331609 / DEDUSAGA-9817]** Corrigir o envio de notificações no processo de "Assistente de Cadastro de Ocorrências".

Arquivos: RM.Edu.Aluno.Data.dll; RM.Edu.Aluno.Server.dll; RM.Edu.Consts.dll; RM.Edu.Interfaces.Intf.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11072]** Otimizações realizadas na rotina de cadastros relacionados ao Censo Superior

Arquivos: RM.Edu.Professor.Form.dll; RM.Edu.Professor.Data.dll

* **[Ticket: DEDUBOPE-11072]** Inclusão dos campos novos de Mediador para o Censo Superior.

Arquivos: RM.Edu.Professor.Data.dll; RM.Edu.Professor.Form.dll; RM.Edu.Lib.Intf.dll

* **[Ticket: DEDUBOPE-11074]** Criação da exportação do arquivo de mediadores do Censo Superior

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: DEDUCAPCOM-10166]** Reorganização das etapas de envio de mensagens na Central de Comunicação

Arquivo: Edu/portalgestaoeducacional

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10066]** Reorganização das etapas de envio de mensagens na Central de Comunicação

Arquivo: RM.Edu.API.dll

* **[Ticket: DEDUCAPCOM-10066]** Reorganização das etapas de envio de mensagens na Central de Comunicação: o público-alvo passará a ser apresentado inicialmente, fornecendo o contexto necessário para o Assistente de IA TOTVS

Arquivo: Edu/portalgestaoeducacional

### Rotina: FREQUÊNCIA/PLANO DE AULA

* **[Ticket: 26556129 / DEDUSAGA-10339]** Ajuste na leitura do nome da disciplina para interpretação correta do apóstrofo.

Arquivo: App\_Web\_edudisciplinasprofwebform.ascx.497dfae.dll

### Rotina: PARÂMETROS

* **[Ticket: DEDUCAPCOM-10165]** Implementação da tela de parametros do assistente de IA e ajustes na API para enviar os novos parametros para o PGE

Arquivos: RM.Edu.Parametros.Data.dll; RM.Edu.Parametros.Intf.dll; RM.Edu.Consts.dll; RM.Edu.API.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Parametros.Form.dll; RM.Edu.Lib.Intf.dll

## 12.1.2602.111

### Rotina: CARTEIRINHA

* **[Ticket: DEDUCAPCOM-9086]** Meu eduCONNECT - Criar parâmetro para imagem modo escuro.

Arquivos: RM.Edu.Parametros.Data.dll; RM.Edu.Parametros.Form.dll; RM.Edu.Parametros.Intf.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Interfaces.Intf.dll

### Rotina: CHECK-IN POR LOCALIZAÇÃO

* **[Ticket: DEDUSAGA-10328]** Ajuste ao salvar e recuperar os check-ins da aula realizados pelos alunos no meu EduConnect.

Arquivo: RM.Edu.API.dll

### Rotina: PAGAMENTO BOLETO

* **[Ticket: DEDUPACMEN-7414]** Ajustes para permitir registro de boleto híbrido no portal do alunoCriada nas configurações de relatório um campo para registrar o report do boleto híbrido

Arquivos: RM.Edu.Financeiro.Server.dll; RM.Edu.Facade.dll; RM.Edu.Rest.Server.dll; RM.Edu.Parametros.Form.dll; RM.Edu.API.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Formula.dll; RM.Edu.Parametros.Intf.dll

* **[Ticket: DEDUPACMEN-7414]** Alteração nas visões de impressão de boleto e código de barras para utilização dos webcomponents do projeto edu-elements

Arquivo: Edu/portaleducacional

## 12.1.2602.112

### Rotina: CONTRATOS

* **[Ticket: 26442565 / DEDUPACMEN-8392]** Ajuste na validação de contexto na inclusão de contrato educacional

Arquivo: RM.Edu.Financeiro.Form.dll

### Rotina: CURSOS/MATRIZES CURRICULARES

* **[Ticket: 26500005 / DEDUBOPE-11513]** Melhoria continua no processo de cadastro dos modelos de etapa

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUBOPE-11520]** Otimização no serviço de atualização de dados dos responsáveis no portal do aluno.

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

### Rotina: GESTÃO DE MENSAGENS

* **[Ticket: 26729814 / DEDUSAGA-10402]** Ajuste na listagem de turmas/disciplinas em "Mensagens Pessoais" do professor. O objetivo é respeitar o parâmetro: Parâmetros > Secretaria > Utilizar Turma/Disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária, plano de aula e upload de materiais no portal e mensagens pessoais no Meu Educonnect.

Arquivos: RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Mensagens.Server.dll; RM.Edu.API.dll

### Rotina: LOGIN

* **[Ticket: 26709012 / DEDUSAGA-10373]** Ajuste para permitir a mudança de senha

Arquivo: Edu/portaldoprofessor

### Rotina: PARÂMETROS

* **[Ticket: DEDUCAPCOM-8220]** Alterações para melhorar o sincronismo das notificações do Meu eduCONNECT entre Azure e TOTVS Educacional.

Arquivos: RM.Edu.Consts.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Integracoes.Intf.dll

### Rotina: PROFESSORES

* **[Ticket: DEDUBOPE-11390]** Ajuste na visibilidade dos campos "Apto" e "Autorizado" na visualização de Disciplinas Autorizdas do Professor

Arquivo: RM.Edu.Professor.Intf.dll

## 12.1.2602.113

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11532]** Adequação das alterações no layout de exportação do docente para o Censo Superior.

Arquivo: RM.Edu.Professor.Data.dll

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: DEDUCAPCOM-10166]** Implementação da API de execução do Assintente de IA na Central de Comunicação no PGE

Arquivos: RM.Edu.Lib.Intf.dll; RM.Edu.API.dll; RM.Edu.CentralComunicacao.Server.dll; RM.Edu.Consts.dll; RM.Edu.Menu.dll; RM.Edu.Utils.Server.dll

## 12.1.2602.114

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: 26858586 / DEDUBOPE-11548]** Melhoria continua no processo de exportação dos arquivos do censo ensino basico

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUSAGA-10474]** Ajuste de segurança no processo de recuperar senha.

Arquivo: RM.Edu.API.dll

### Rotina: DOWNLOAD DE MATERIAIS

* **[Ticket: 26882465 / DEDUBOPE-11557]** Otimização no serviço de fazer download do arquivo de documento no portal do aluno.

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

### Rotina: NÍVEIS DE ENSINO

* **[Ticket: 26685473 / DEDUBOPE-11484]** Melhoria continua no processo de cadastro de Autorização da Instituição

Arquivos: RM.Edu.Cadastros.Server.dll; RM.Edu.Cadastros.Form.dll; RM.Edu.Cadastros.Data.dll

### Rotina: NOTAS E FALTAS DE ETAPA

* **[Ticket: 26800624 / DEDUSAGA-10434]** Ajuste na consulta de notas e faltas para exibir alunos vinculados a etapas que possuam predecessoras.

Arquivo: Edu/portaldoprofessor

### Rotina: OCORRÊNCIAS

* **[Ticket: 26794292 / DEDUSAGA-10437]** Correção no fluxo responsável por marcar a ocorrência como ciente pelo responsável do aluno.

Arquivo: RM.Edu.Aluno.Data.dll

* **[Ticket: DEDUSAGA-10455]** Correção ao editar uma ocorrência de um aluno de turma/disciplina gerencial, ela continua sendo exibida corretamente para o professor.

Arquivo: RM.Edu.API.dll

### Rotina: PLANO DE AULA

* **[Ticket: DEDUSAGA-10475]** Correção na exibição dos arquivos anexados ao Plano de Aula no RM.exe.

Arquivo: RM.Edu.PeriodoLetivo.Data.dll

## 12.1.2602.115

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: 26742299 / DEDUCAPCOM-10245]** Ajuste no cadastro de regra de comunicação: Alteração do campo de pesquisa de permissões por categoria para exibir o Nome Fantasia da filial em vez da Razão Social. O objetivo é padronizar o comportamento com os demais campos do sistema, como o filtro de filial na aba "Filtro Avançado".

Arquivo: RM.Edu.Smart.API.dll

## 12.1.2602.116

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11433]** Implementado novo parâmetro para considerar somente municípios previamente cadastrados no campo "Naturalidade" do aluno

Arquivos: RM.Edu.Facade.dll; RM.Edu.Cadastros.Server.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Aluno.Server.dll; RM.Edu.Parametros.Intf.dll; RM.Edu.Parametros.Form.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11532]** Criação da exportação do arquivo de mediadores do Censo Superior

Arquivos: RM.Edu.Professor.Intf.dll; RM.Edu.Professor.Form.dll

* **[Ticket: DEDUBOPE-11532]** Modificação no preenchimento dos campos "Docente" na geração de saídas para o Registro 32

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: DEDUBOPE-11532]** Adequação das alterações no layout de exportação do docente para o Censo Superior.

Arquivos: RM.Edu.Academico.Server.dll; RM.Edu.Professor.Form.dll

* **[Ticket: DEDUBOPE-11532]** Removidas validações de campos não utilizados no Censo Superior

Arquivo: RM.Edu.Professor.Data.dll

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: 26742299 / DEDUCAPCOM-10245]** Ajuste no cadastro da regra de comunicação no TOTVS Educacional, pois os valores do tipo de mensagem não estavam sendo apresentado na inclusão de uma nova regra

Arquivo: RM.Edu.Smart.API.Shared.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUSAGA-10503]** Adicionando validação de segurança para os campos complementares.

Arquivo: RM.Edu.API.dll

### Rotina: DOWNLOAD DE MATERIAIS

* **[Ticket: 26882465 / DEDUBOPE-11557]** Otimização no serviço de fazer download do arquivo de documento no portal do aluno.

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 26739201 / DEDUPACMEN-8493]** Ajuste para calculo de fórmula da bolsa na geração do movimento por competência

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: MATRÍCULA ON-LINE ENSINO BÁSICO

* **[Ticket: 25805613 / DEDUPACMEN-8443]** Foi ajustada api ObterDadosDocumentoContratoAssinadoTae: foi incorporada ao retorno do método ObterListaDocumentosComDestinatarios uma verificação, quando não tem nenhum destinatário referente ao usuário logado no TAE, o sistema verifica se o usuário logado é um potencial assinante, mas não está no TAE por causa de mudança de e-mail ou de parametrização, se ele for, ele será adicionado a lista de destinatários que é retornado no método

Arquivos: RM.Edu.Rest.Server.dll; RM.Edu.Integracoes.Server.dll

### Rotina: OCORRÊNCIAS

* **[Ticket: 26794292 / DEDUSAGA-10437]** Ajuste para impedir o professor de editar uma ocorrência caso já tenha o aceite do responsável.

Arquivos: RM.Edu.API.dll; RM.Edu.Aluno.Data.dll

* **[Ticket: 26794292 / DEDUSAGA-10437]** Ajuste na apresentação da mensagem quando o professor não tem permissão de alterar uma ocorrência com aceite do responsável.

Arquivo: Edu/portaldoprofessor

## 12.1.2602.117

### Rotina: ANEXOS - CANDIDATOS INSCRITOS

* **[Ticket: DEDUCAPCOM-10338]** Ajustes de CPF cenario 3

Arquivo: Edu/portalprocessoseletivo-e2e

* **[Ticket: DEDUCAPCOM-10338]** Ajustes cenario cypress

Arquivo: Edu/portalprocessoseletivo-e2e

* **[Ticket: DEDUCAPCOM-10338]** Ajustes de CPF cenario 2

Arquivo: Edu/portalprocessoseletivo-e2e

* **[Ticket: DEDUCAPCOM-10338]** Ajustes de CPF cenario 2 e 3

Arquivo: Edu/portalprocessoseletivo-e2e

* **[Ticket: DEDUCAPCOM-10338]** Ajustes de CPF inscricaoCenario04

Arquivo: Edu/portalprocessoseletivo-e2e

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11532]** Adequação das alterações no layout de exportação do docente para o Censo Superior.

Arquivos: RM.Edu.Professor.Form.dll; RM.Edu.Professor.Data.dll

* **[Ticket: DEDUBOPE-11590]** Alteração na rotina do Censo Superior para buscar corretamente a situação de transferência interna do aluno.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: DESMATRICULAR PROCESSO SELETIVO RM

* **[Ticket: 26504642 / DEDUCAPCOM-10134]** Alterações no processo de desmatricula de alunos matriculados através da matrícula do processo seletivo RM.

Arquivo: RM.Edu.ProcSel.Server.dll

### Rotina: DOWNLOAD DE MATERIAIS

* **[Ticket: 26882465 / DEDUBOPE-11557]** Otimização no serviço de fazer download do arquivo de documento no portal do aluno.

Arquivo: RM.Edu.Aluno.Server.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10167]** Ajustes na central de comunicação

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: 26495269 / DEDUCAPCOM-10253]** Ajustamos o comportamento dos filtros avançados na Central de Comunicação. Identificamos que, em cenários onde diferentes cursos compartilhavam códigos de habilitação idênticos (ex: Habilitação "05" presente tanto no Infantil quanto no Fundamental), o sistema exibia opções indevidas para o usuário.

Arquivos: RM.Edu.CentralComunicacao.Server.dll; RM.Edu.API.dll

### Rotina: GESTÃO DE MENSAGENS

* **[Ticket: 26953902 / DEDUSAGA-10514]** Ajuste de performance ao carregar o painel de mensagens do Meu eduCONNECT.

Arquivo: RM.Edu.Mensagens.Server.dll

### Rotina: LOGIN

* **[Ticket: DEDUSAGA-10440]** Migração da identificação do usuário do client para o server.

Arquivos: Edu/portaldoprofessor; RM.Edu.API.dll

### Rotina: MATRÍCULA ON-LINE ENSINO BÁSICO

* **[Ticket: 25805613 / DEDUPACMEN-8443]** Adicionado campo no backend, na rota "v1/Matricula/Habilitacao/ObterDadosDocumentoContratoAssinadoTae" um campo para informar se houve mudança de e-mail dentre os assinantes

Arquivos: RM.Edu.Integracoes.Server.dll; RM.Edu.Integracoes.Intf.dll; RM.Edu.Lib.Intf.dll

* **[Ticket: 25805613 / DEDUPACMEN-8443]** Ajuste no front-end, quando houver mudança de e-mail do assinante na rematrícula, chamar o método para cancelamento do envelope

Arquivo: Edu/portaleducacional

### Rotina: OCORRÊNCIAS

* **[Ticket: 26794292 / DEDUSAGA-10437]** Ajuste para enviar uma nova notificação para o responsável quando o professor editar uma ocorrência com aceite do responsável.

Arquivo: RM.Edu.Aluno.Server.dll

### Rotina: UPLOAD DE MATERIAIS

* **[Ticket: 26491388 / DEDUSAGA-10398]** Redirecionamento a partir do portal do professor para o módulo "Arquivos da Instituição" no Corpore

Arquivo: RM.Edu.API.dll

* **[Ticket: 26491388 / DEDUSAGA-10398]** Criação de ícone "Arquivos da instituição" no menu do portal

Arquivo: Edu/portaldoprofessor

* **[Ticket: 26491388 / DEDUSAGA-10398]** Ajuste no nome do portal

Arquivo: Edu/portaldoprofessor

## 12.1.2602.121

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: DEDUBOPE-11590]** Campos Docente modificados para permitir vazio no cadastro anexo de Professores da Turma /Disciplina

Arquivos: RM.Edu.Utils.Server.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.Academico.Server.dll; RM.Edu.PeriodoLetivo.Intf.dll; RM.Edu.Professor.Data.dll

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 26711643 / DEDUPACMEN-8571]** Ajuste do dado enviado ao campo Tipo de endereço nos campos complementares do movimento

Arquivos: RM.Edu.Lib.Intf.dll; RM.Edu.Financeiro.Server.dll

### Rotina: VISUALIZACÃO DE BOLETOS

* **[Ticket: 27032535 / DEDUPACMEN-8591]** Ajuste de slot Portal do Aluno

Arquivo: RM.Edu.API.dll

## 12.1.2602.122

### Rotina: PARÂMETROS

* **[Ticket: 26105453 / DEDUPACMEN-8283]** Otimização no processo de geração de lançamento quando o parâmetro “Gerar contabilização após a geração de lançamentos.” presente em Configurações ? Parâmetros Educacionais ? Integração ? Financeiro ? Educacional ? Fin - Geral 2/4 estiver marcado para ser considerado somente nos processos de geração de lançamento

Arquivos: RM.Edu.PesquisaExtensao.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Consts.dll; RM.Edu.Aluno.Server.dll; RM.Edu.Financeiro.Server.dll; RM.Edu.Matricula.Server.dll; RM.Edu.Financeiro.Intf.dll; RM.Edu.Customizacao.Intf.dll; RM.Edu.Financeiro.Data.dll; RM.Edu.Contabil.Server.dll; RM.Edu.Cst.Facade.dll; RM.Edu.Interfaces.Intf.dll

## 12.1.2602.124

### Rotina: CRIAR TURMAS

* **[Ticket: DEDUBOPE-11602]** Otimizada rotina de processamento de sessão e periodo letivo na geração de código de turma

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

### Rotina: PARÂMETROS

* **[Ticket: 26671128 / DEDUBOPE-11480]** Inclusão da tela de Diretores por Filial e alteração do processo de unificação e ativação da Instituição do MEC para permitir gravar os diretores também na filial.

Arquivos: RM.Edu.Academico.Server.dll; RM.Edu.Utils.Server.dll; RM.Edu.Cadastros.Form.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Menu.dll; RM.Edu.Cadastros.Intf.dll; RM.Edu.Cadastros.Data.dll

* **[Ticket: DEDUCAPCOM-9174]** Melhorias na persistência de dados de geolocalização utilizada pelo app Meu eduCONNECT.

Arquivos: RM.Edu.API.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.Integracoes.Intf.dll

## 12.1.2602.125

### Rotina: CONTRATOS

* **[Ticket: 26827047 / DEDUPACMEN-8550]** Melhoria continua no registro de logs de cancelamento de recorrencia

Arquivos: RM.Edu.Interfaces.Intf.dll; RM.Edu.Financeiro.Server.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUSAGA-10556]** remoção do recebimento da url do portal do aluno para envio do token de troca de senha, agora passa a buscar a url do parametro url da frameHtml cadastrada em globais para montagem da url.

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

* **[Ticket: DEDUSAGA-10556]** remoção do envio da url para a api de recuperar a senha.

Arquivo: Edu/portaleducacional

### Rotina: DISCIPLINAS

* **[Ticket: 26661264 / DEDUBOPE-11528]** Otimização da apresentação de dados da tela de Análise Curricular para carga integralizada.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: HISTÓRICO ESCOLAR

* **[Ticket: 26275535 / DEDUBOPE-11483]** Histórico Escolar: Otimizamos o processo de geração do histórico escolar, garantindo maior precisão e agilidade na consolidação das notas e etapas finais das disciplinas em que o aluno possui vínculo.Matrícula de Itinerário Formativo (Lote): Implementamos uma nova trava de segurança no processo de matrícula em lote. Agora, o sistema valida automaticamente se as turmas e disciplinas selecionadas pertencem à matriz aplicada do aluno, impedindo inconsistências e garantindo que o currículo escolar seja rigorosamente respeitado.

Arquivos: RM.Edu.Matricula.Server.dll; RM.Edu.Historico.Server.dll

### Rotina: MATRICULAR PROCESSO SELETIVO RM

* **[Ticket: 27123698 / DEDUPACMEN-8620]** Melhoria continua no processo de matricular alunos do processo seletivo

Arquivo: RM.Edu.ProcSel.Form.dll

### Rotina: NOTAS E FALTAS DE AVALIAÇÃO

* **[Ticket: 27004056 / DEDUSAGA-10538]** Definindo casas decimais de acordo com o RM

Arquivo: Edu/portaldoprofessor

### Rotina: PARÂMETROS

* **[Ticket: 26671128 / DEDUBOPE-11480]** Inclusão da tela de Diretores por Filial e alteração do processo de unificação e ativação da Instituição do MEC para permitir gravar os diretores também na filial.

Arquivo: RM.Edu.Interfaces.Intf.dll

* **[Ticket: DEDUCAPCOM-9174]** Melhorias na persistência de dados de geolocalização utilizada pelo app Meu eduCONNECT.

Arquivos: RM.Edu.Mensagens.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.API.dll

* **[Ticket: 26742785 / DEDUPACMEN-8513]** Ajuste nos parâmetros dos serviços que permitem registro do boleto online

Arquivos: RM.Edu.Parametros.Data.dll; RM.Edu.Utils.Server.dll; RM.Edu.Parametros.Intf.dll

## 12.1.2602.126

### Rotina: ANÁLISE DE LOG - HOMOLOGAÇÃO

* **[Ticket: 27142838 / DEDUPACMEN-8652]** Ajustado o código defensivo para contemplar a nova marcação

Arquivo: RM.Edu.Utils.Server.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27157906 / DEDUBOPE-11642]** Otimização do processo de preparação de dados do censo do ensino superior.

Arquivo: RM.Edu.Academico.Data.dll

### Rotina: NOTAS E FALTAS DE AVALIAÇÃO

* **[Ticket: 27004056 / DEDUSAGA-10538]** ajuste teste automatizado de interface

Arquivo: Edu/portaldoprofessor-e2e

## 12.1.2602.127

### Rotina: CRIAR TURMAS

* **[Ticket: DEDUBOPE-11602]** Otimização na altura da grid do cadastro de modelo de turma no planejamento de oferta.

Arquivo: Edu/portalgestaoeducacional

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUSAGA-10556]** remoção do recebimento da url do portal do aluno para envio do token de troca de senha, agora passa a buscar a url do parametro url da frameHtml cadastrada em globais para montagem da url.

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

### Rotina: GERAÇÃO DE HORÁRIO

* **[Ticket: 26598347 / DEDUBOPE-11469]** Otimização realizada no processo de geração de horários do professor

Arquivos: RM.Edu.PeriodoLetivo.Data.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Academico.Server.dll

### Rotina: VISUALIZACÃO DE BOLETOS

* **[Ticket: 26869375 / DEDUPACMEN-8600]** Ajuste na query do método AtualizarBoletoComBolsaFIES que identifica se um boleto possui bolsa FIES vinculada: ele passa não considerar se tem lançamento cancelado com bolsa fies associada ao boleto. Essa informação impacta diretamente nas permissões de pagamento do boleto já que "Boletos com \*\*Novo FIES\*\* bloqueiam pagamento por cartão, boleto e PIX."

Arquivo: RM.Edu.Financeiro.Server.dll

## 12.1.2602.128

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10169]** Melhorias na central de comunicação Web

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.129

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 26952337 / DEDUBOPE-11628]** Melhoria de performance no processo de preparação de dados do Censo.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: GERAÇÃO DE HORÁRIO

* **[Ticket: 26598347 / DEDUBOPE-11469]** Ajustada mensagem de progresso no processo de geração de horários

Arquivo: RM.Edu.PeriodoLetivo.Data.dll

## 12.1.2602.130

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11433]** Ajustada label de parâmetro de validação de endereços nacionais do aluno

Arquivo: RM.Edu.Parametros.Form.dll

### Rotina: AVALIAÇÃO INSTITUCIONAL

* **[Ticket: 26973023 / DEDUSAGA-10555]** Ajuste na composição das urls das avaliações institucionais

Arquivo: Edu/portaleducacional

### Rotina: BANNER

* **[Ticket: DEDUCAPCOM-10322]** Ajustes para tratar nas validações de origin ao carregar a ficha médica

Arquivo: Edu/portalprocessoseletivo

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 26973335 / DEDUBOPE-11622]** Alteração no processo de preparação dos dados do Censo para buscar todos os aluno.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CONTRATOS

* **[Ticket: 26553364 / DEDUBOPE-11632]** Ajustada validação de arquivo de contrato vazio para ocorrer apenas quando o contrato financeiro está disponível para impressão

Arquivo: RM.Edu.Rest.Server.dll

* **[Ticket: 26553364 / DEDUBOPE-11632]** Adicionada validação para barrar matrícula via portal caso não haja arquivo vinculado a assinatura do contrato

Arquivo: RM.Edu.Rest.Server.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10169]** Corrigida uma não conformidade que impedia o carregamento do público-alvo e dos filtros ao utilizar as funções "Visualizar" ou "Usar como modelo"

Arquivo: Edu/portalgestaoeducacional

### Rotina: ESTRUTURA CURRICULAR/ESTRUTURA DE OFERTA

* **[Ticket: 27118120 / DEDUBOPE-11626]** Otimização do processo de exibição das cargas horárias integralizadas na Análise Curricular.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: GERAÇÃO DE MOVIMENTO POR COMPETÊNCIA

* **[Ticket: DEDUPACMEN-8667]** Adicionada tela de alerta de descontinuidade do processo de geração de movimento por competência quando o mesmo é aberto pelo usuário

Arquivos: RM.Edu.Financeiro.Form.dll; RM.Edu.Consts.dll

### Rotina: PERGAMUM

* **[Ticket: 26598231 / DEDUCAPCOM-10426]** Ajustes para evitar recorrência e duplicações no processo de exportação de usuários para o Pergamum.

Arquivos: RM.Edu.Integracoes.Server.dll; RM.Edu.Integracoes.Data.dll

### Rotina: TOTVS ASSINATURA ELETRÔNICA

* **[Ticket: 26904051 / DEDUPACMEN-8625]** Ajuste de validação mensagem TAE

Arquivo: RM.Edu.Rest.Server.dll

## 12.1.2602.131

### Rotina: CONTRATOS

* **[Ticket: 26553364 / DEDUBOPE-11632]** Ajustada validação de arquivo de contrato vazio para ocorrer apenas quando o contrato financeiro está disponível para impressão

Arquivo: RM.Edu.Rest.Server.dll

* **[Ticket: DEDUPACMEN-8609]** Foi ajustada a api do resumo de pagamento api para verificar se os boletos pertencem ao usuário logado

Arquivos: RM.Edu.API.dll; RM.Edu.Financeiro.Server.dll

### Rotina: MENSAGENS PESSOAIS

* **[Ticket: 26796022 / DEDUSAGA-10489]** Correção na listagem de mensagens do eduCONNECT em cenários de impossibilidade de compressão da imagem

Arquivo: RM.Edu.API.dll

### Rotina: OCORRÊNCIAS

* **[Ticket: 27245475 / DEDUSAGA-10617]** Ajuste na apresentação da coluna 'Nº' na página de ocorrências

Arquivo: Edu/portaldoprofessor

### Rotina: PROFESSORES

* **[Ticket: 26602834 / DEDUSAGA-10629]** Ajuste ao buscar o código do professor baseado no código do usuário logado, primeiramente buscando pela chapa informada no cadastro da filial do professor e caso não encontre busca pela chapa informada no cadastro do professor

Arquivo: RM.Edu.Professor.Server.dll

## 12.1.2602.132

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11433]** Modificada validação de municipio válido para o campo Cidade e Estado e não Naturalidade no cadastro do aluno

Arquivo: RM.Edu.Cadastros.Server.dll

### Rotina: AVALIAÇÃO INSTITUCIONAL

* **[Ticket: DEDUSAGA-10652]** Remover restrição de abertura da Avaliação Institucional no navegador Safari via Portal do Aluno.

Arquivos: Portal Corpore.Net

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10169]** Ajustes pontuais na Assistente de IA Central de Comunicação

Arquivo: Edu/portalgestaoeducacional

### Rotina: NOTAS E FALTAS DE AVALIAÇÃO

* **[Ticket: 27004056 / DEDUSAGA-10538]** Ajuste casas decimais dos campos valor e média avaliações.

Arquivos: Edu/portaldoprofessor; RM.Edu.Interfaces.Intf.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.PeriodoLetivo.Data.dll

### Rotina: OCORRÊNCIAS

* **[Ticket: 27245475 / DEDUSAGA-10617]** Redimensionamento da coluna na página de ocorrências

Arquivo: Edu/portaldoprofessor

## 12.1.2602.133

### Rotina: Sem Rotina Específica

* **[Ticket: 26888876 / DEDUPACMEN-8633]** Melhoria de visualização de boletos

Arquivos: RM.Edu.Rest.Server.dll; RM.Edu.Financeiro.Server.dll

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11433]** Otimizações realizadas na rotina de geração de horário da turma e professor em lote

Arquivos: RM.Edu.Aluno.Server.dll; RM.Edu.Aluno.Form.dll; RM.Edu.PeriodoLetivo.Data.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Aluno.Data.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Professor.Data.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUSAGA-10572]** Remoção de artefatos desnecessários da customização

Arquivo: Edu/portaldoprofessor

### Rotina: GERAR OFERTA

* **[Ticket: DEDUBOPE-11618]** Nova funcionadalode para adiciona alocação de multiplos horarios para a mesma turma disc

Arquivos: RM.Edu.Parametros.Form.dll; RM.Edu.Lib.Intf.dll; RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.Parametros.Intf.dll; RM.Edu.Interfaces.Intf.dll

### Rotina: PAGAMENTO COM CARTÃO

* **[Ticket: DEDUPACMEN-8647]** Foram incluídas novas validações de segurança na visualização do recibo do extrato financeiro

Arquivo: RM.Edu.Rest.Server.dll

## 12.1.2602.134

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10168]** Ajustes na I.A da central de comunicação web

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: DEDUCAPCOM-10169]** Melhorias na central de comunicação web

Arquivo: Edu/portalgestaoeducacional

### Rotina: MATRÍCULA ON-LINE ENSINO SUPERIOR

* **[Ticket: 27199776 / DEDUBOPE-11667]** Otimização do processo de armazenamento do arquivo do documento ao realizar matrícula do aluno via portal do aluno.

Arquivo: RM.Edu.Aluno.Server.dll

## 12.1.2602.135

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11619]** Efetuado ajuste na regra de validação do cadastro de professores na turma no processo de preparação dos dados do censo.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27137930 / DEDUBOPE-11709]** Otimizações nas consultas Oracle do Censo e na passagem de contexto para o Registro 30

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8588]** Ajustes no fluxo de desconto por antecipação para melhorias de performance.

Arquivos: RM.Edu.Financeiro.Server.dll; RM.Edu.Lib.Intf.dll

## 12.1.2602.136

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11433]** Ajustes nas mensagens de validação de cadastros de município

Arquivos: RM.Edu.Aluno.Form.dll; RM.Edu.Aluno.Server.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27372793 / DEDUBOPE-11716]** Alteração na busca da instituição do MEC para a geração dos arquivos de docente e mediador no Censo Superior.

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: 27389923 / DEDUBOPE-11723]** Otimização na consulta do Registro 42 do Censo Superior para tratar corretamente a informação de turno para ser exibida somente em modalidade presencial

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: DISCIPLINAS

* **[Ticket: 26661264 / DEDUBOPE-11722]** Otimização do processo de exclusão de Componentes e Itens Curriculares da Matriz Curricular, validando a existência de Atividades Ofertadas associadas.

Arquivos: RM.Edu.AtvCurricular.Data.dll; RM.Edu.MatrizCurricular.Data.dll; RM.Edu.Services.Server.dll; RM.Edu.Academico.Server.dll; RM.Edu.Interfaces.Intf.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: 26973371 / DEDUCAPCOM-10469]** Ajuste para evitar o carregamento infinito de categorias ao enviar uma notificação para o Meu eduCONNECT.

Arquivo: Edu/portalgestaoeducacional

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8587]** Melhoria continua no processo de criação de lançamentos

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: GESTÃO DE MENSAGENS

* **[Ticket: 26984801 / DEDUSAGA-10691]** Otimização de performance de comunicados com anexos no eduCONNECT

Arquivos: RM.Edu.API.dll; RM.Edu.Mensagens.Server.dll

### Rotina: NOTAS E FALTAS DE ETAPA

* **[Ticket: 27315966 / DEDUSAGA-10690]** Ajuste para retornar notas e faltas para períodos encerrados

Arquivo: RM.Edu.API.dll

## 12.1.2602.137

### Rotina: ALUNOS

* **[Ticket: DEDUBOPE-11433]** Ajustes nas mensagens de validação de cadastros de município

Arquivos: RM.Edu.Cadastros.Server.dll; RM.Edu.Aluno.Form.dll; RM.Edu.Aluno.Server.dll

* **[Ticket: DEDUBOPE-11619]** Validação de Documentos via IA: Agora é possível personalizar as regras de aprovação de campos específicos. Com essa melhoria, o sistema utiliza suas parametrizações de restrição para decidir, de forma inteligente e automática, quais documentos atendem aos critérios da sua operação, oferecendo mais controle e precisão no processo.

Arquivos: RM.Edu.Aluno.Server.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Facade.dll; RM.Edu.Academico.Server.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Cadastros.Server.dll; RM.Edu.Consts.dll

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: DEDUCAPCOM-10170]** Implementação do Assistente de IA TOTVS na Central de Comunicação

Arquivos: RM.Edu.Consts.dll; RM.Edu.Global.Intf.dll; RM.Edu.CentralComunicacao.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Facade.dll; RM.Edu.API.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10169]** Ajustes na central de comunicação Web

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: DEDUCAPCOM-10169]** Implementação da opções do assistente de IA TOTVS dentro da Central de Comunicação

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.138

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10169]** Ajustes na central de comunicação Web

Arquivo: Edu/portalgestaoeducacional

### Rotina: PROCESSADOR DE FREQUÊNCIA DIÁRIA

* **[Ticket: 27273495 / DEDUSAGA-10725]** Atualizar a data/hora do processamento da frequência diária para a hora real da execução do agendamento;Ajustar o log de "Fim do processamento" com os dados corretos da Turma/Disciplina;Incluir log de "Início do processamento" para turmas/disciplinas sem alunos matriculados;

Arquivo: RM.Edu.NotaFalta.Data.dll

### Rotina: RM EXECUTOR (WEB SERVICE)

* **[Ticket: DEDUSAGA-10280]** Implementação do atendente de sala de atendimento poder iniciar conversa

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: DEDUSAGA-10280]** Implementação de Iniciar conversa de atendimento pelo atendente.

Arquivos: RM.Edu.Menu.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.API.dll; RM.Edu.Consts.dll; RM.Edu.Mensagens.Server.dll

## 12.1.2602.139

### Rotina: RM EXECUTOR (WEB SERVICE)

* **[Ticket: DEDUSAGA-10280]** Implementação de Iniciar conversa de atendimento pelo atendente.

Arquivo: RM.Edu.Menu.dll

## 12.1.2602.140

### Rotina: AUXILIARES

* **[Ticket: 26778499 / DEDUBOPE-11570]** Melhorias no tratamento de exclusão motivo de alteracao de status de matricula para verificar se o motivo esta em uso

Arquivos: RM.Edu.Academico.Data.dll; RM.Edu.Academico.Server.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUSAGA-10594]** Ajuste para fins de padronização de projeto.

Arquivo: RM.Edu.API.dll

* **[Ticket: DEDUSAGA-10594]** Ajuste na sala de conversa para fins de padronização de projeto.

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.141

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27399604 / DEDUBOPE-11727]** Alteração do cadastro de Autorização da Instituição de Ensino para utilizar coligada global.

Arquivo: RM.Edu.Cadastros.Data.dll

### Rotina: CONTRATOS

* **[Ticket: DEDUPACMEN-8635]** Permitir obrigatoriedade de assinatura via TAE na rematrícula por curso

Arquivos: RM.Edu.Utils.Server.dll; RM.Edu.Services.Server.dll; RM.Edu.Matricula.Data.dll; RM.Edu.Parametros.Intf.dll; RM.Edu.Financeiro.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Matricula.Server.dll; RM.Edu.Parametros.Form.dll; RM.Edu.PeriodoLetivo.Data.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.PeriodoLetivo.Intf.dll; RM.Edu.Rest.Server.dll; RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.Integracoes.Server.dll

* **[Ticket: DEDUPACMEN-8635]** Implementação obrigatoriedade de assinatura via TAE na rematrícula por curso

Arquivo: Edu/portaleducacional

### Rotina: NFS-E - CONSULTA AUTORIZAÇÃO/CANCELAMENTO

* **[Ticket: 27631535 / DEDUPACMEN-8734]** Otimização no processo de geração de movimento por caixa, por competência e para a taxa de inscrição do candidato os dados do destinatário do consumidor do serviço quando o aluno/candidato e o responsável financeiro são as mesmas pessoas.

Arquivo: RM.Edu.Facade.dll

## 12.1.2602.142

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10168]** Bloqueio de envio de imagens para i.a na central de comunicação web

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: 26973371 / DEDUCAPCOM-10519]** Melhorias no carregamento de categorias para envio de notificações do Meu eduCONNECT na Central de Comunicação do TOTVS Portal Gestão Educacional

Arquivo: RM.Edu.API.dll

### Rotina: PROCESSADOR DE FREQUÊNCIA DIÁRIA

* **[Ticket: 27584794 / DEDUSAGA-10733]** Ajuste para que as ausências em subturmas sejam computadas ao executar o processador de frequência diária.

Arquivos: RM.Edu.NotaFalta.Data.dll; RM.Edu.NotaFalta.Intf.dll; RM.Edu.NotaFalta.Server.dll

### Rotina: TURMAS E TURMAS / DISCIPLINAS

* **[Ticket: 27696318 / DEDUSAGA-10773]** Ajuste na visualização de etapas da Turma/Disciplina.

Arquivos: RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.PeriodoLetivo.Data.dll

## 12.1.2602.143

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27399604 / DEDUBOPE-11727]** Alteração do cadastro de Autorização da Instituição de Ensino para utilizar coligada global.

Arquivo: RM.Edu.Cadastros.Data.dll

### Rotina: CERTIFICADOS/DIPLOMAS/SOLENIDADES

* **[Ticket: 27077060 / DEDUBOPE-11662]** Melhorias no filtro genérico de atividades ofertadas em Diplomação

Arquivos: RM.Edu.Academico.Form.dll; RM.Edu.Academico.Data.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10168]** Implementação do Assistente de IA TOTVS na Central de Comunicação

Arquivo: RM.Edu.Facade.dll

### Rotina: MUDANÇA DE TURMA

* **[Ticket: 26785075 / DEDUBOPE-11579]** Adicioanda validação no processo de mudança de turma em casos de alunos com todas as matrículas em disciplinas finalizadas

Arquivos: RM.Edu.Matricula.Server.dll; RM.Edu.Matricula.Data.dll

## 12.1.2602.144

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10168]** Melhorias na central de comunicação

Arquivo: Edu/portalgestaoeducacional

### Rotina: TABELA DE PREÇO

* **[Ticket: DEDUPACMEN-8640]** Melhoria continua no processo de cadastro dos dados da tabela de preço

Arquivo: RM.Edu.Financeiro.Server.dll

## 12.1.2602.145

### Rotina: Sem Rotina Específica

* **[Ticket: 27710139 / DEDUSAGA-10783]** Alteração de nomenclatura para o parâmetro "Quadro de Avisos" (disponível no menu Parâmetros Gerais 2/18) informando que se aplica apenas para o eduCONNECT e Educa Mobile.

Arquivo: RM.Edu.Parametros.Form.dll

### Rotina: ALUNOS

* **[Ticket: 26941436 / DEDUBOPE-11612]** Ajustes para validar o tamanho da imagem de perfil de aluno e professor.

Arquivos: RM.Edu.Aluno.Form.dll; RM.Edu.Consts.dll; RM.Edu.Aluno.Server.dll; RM.Edu.Utils.Server.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Professor.Form.dll; RM.Edu.Professor.Data.dll

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27399604 / DEDUBOPE-11727]** Alteração do cadastro de Autorização da Instituição de Ensino para utilizar coligada global.

Arquivo: RM.Edu.Cadastros.Data.dll

### Rotina: ENADE

* **[Ticket: 27639920 / DEDUBOPE-11777]** Implementação do layout do arquivo do Enade para os cursos de Medicina.

Arquivos: RM.Edu.Academico.Server.dll; RM.Edu.Academico.Form.dll; RM.Edu.Matricula.Server.dll; RM.Edu.Consts.dll; RM.Edu.Lib.Intf.dll

* **[Ticket: 27981386 / DEDUBOPE-11823]** Unificada a regra de análise do curso do aluno entre a Análise Curricular e a geração do arquivo do Enade

Arquivos: RM.Edu.Matricula.Server.dll; RM.Edu.Academico.Server.dll; RM.Edu.Lib.Intf.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: 27121921 / DEDUCAPCOM-10441]** Ajuste no filtro avançado para respeitar os filtros anteriores de Habilitação e matriz aplicada

Arquivos: RM.Edu.CentralComunicacao.Server.dll; RM.Edu.Services.Server.dll

* **[Ticket: DEDUCAPCOM-10503]** Melhorias Central comunicação web

Arquivo: Edu/portalgestaoeducacional

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 26748359 / DEDUPACMEN-8749]** Melhorias nas validações na geração de movimento

Arquivos: RM.Edu.Financeiro.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.MatrizCurricular.Form.dll

### Rotina: LOGIN

* **[Ticket: DEDUSAGA-10748]** adição do recurso de customização usando o native federation e micro front ends

Arquivo: Edu/portalgestaoeducacional

### Rotina: RM EXECUTOR (WEB SERVICE)

* **[Ticket: DEDUSAGA-10280]** Ajuste para exibir o nome do responsável quando o agente selecionar a opção de iniciar uma conversa.

Arquivo: Edu/portalgestaoeducacional

### Rotina: SALAS/AGENTES DE ATENDIMENTO

* **[Ticket: DEDUSAGA-10830]** Ocultar os campos de envio de mensagens quando o agente não houver iniciado uma conversa.

Arquivo: Edu/portalgestaoeducacional

### Rotina: SERVIÇOS

* **[Ticket: DEDUPACMEN-8771]** Otimização no processo de pagamento para saber o número máximo de parcelas para pagamento via cartão de crédito

Arquivos: RM.Edu.Lib.Intf.dll; RM.Edu.Financeiro.Server.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Facade.dll

## 12.1.2602.146

### Rotina: CONFIRMAÇÃO DE MATRÍCULA POR PAGAMENTO

* **[Ticket: 27427860 / DEDUPACMEN-8717]** Ajuste no log de confirmação de matricula por pagamento para registrar somente quando houver alteração no status de matricula.

Arquivo: RM.Edu.Matricula.Server.dll

### Rotina: ENADE

* **[Ticket: 27981386 / DEDUBOPE-11823]** Unificada a regra de análise do curso do aluno entre a Análise Curricular e a geração do arquivo do Enade

Arquivo: RM.Edu.Lib.Intf.dll

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: 26952265 / DEDUPACMEN-8728]** Melhoria continua no processo de geração de lançamentos

Arquivo: RM.Edu.Financeiro.Server.dll

## 12.1.2602.147

### Rotina: DADOS PESSOAIS

* **[Ticket: DEDUBOPE-11435]** Inclusão de tratamento para validação de campos Tipo de Bairro e Tipo de Rua durante atualização de dados do aluno via Portal do Aluno. Em conjunto, adequação das regras de cadastro de município para o Portal.

Arquivo: Edu/portaleducacional

### Rotina: ENADE

* **[Ticket: 27981386 / DEDUBOPE-11823]** Unificada a regra de análise do curso do aluno entre a Análise Curricular e a geração do arquivo do Enade

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: LOGIN

* **[Ticket: DEDUSAGA-10748]** ajuste para alterar aonde a ic busca os arquivos buildados

Arquivo: Edu/portalgestaoeducacional

### Rotina: MATRÍCULA / REMATRÍCULA ENSINO SUPERIOR

* **[Ticket: 27929019 / DEDUBOPE-11808]** Otimização da seleção de alunos na tela de rematricula

Arquivo: RM.Edu.Matricula.Form.dll

## 12.1.2602.148

### Rotina: CONTRATOS

* **[Ticket: 27977992 / DEDUPACMEN-8795]** Ajuste na simulação de valores para a remoção do uso de cache de valores no cálculo de desconto por antecipação.

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10619]** Melhoria central comunicação web

Arquivo: Edu/portalgestaoeducacional

### Rotina: LOGIN

* **[Ticket: DEDUSAGA-10748]** adição de fontes (fontawesome) ao projeto

Arquivo: Edu/portalgestaoeducacional

### Rotina: RM EXECUTOR (WEB SERVICE)

* **[Ticket: DEDUSAGA-10280]** Implementação de Iniciar conversa de atendimento pelo atendente.

Arquivo: RM.Edu.Menu.dll

## 12.1.2602.149

### Rotina: DADOS PESSOAIS

* **[Ticket: DEDUBOPE-11435]** Otimização da atualização de dados pessoais do aluno na tela de cadastro acadêmico do Portal do Aluno.

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10520]** Evolução do Assistente de IA: Suporte a Enquetes (Central de Comunicação)

Arquivos: Edu/portalgestaoeducacional; RM.Edu.API.dll; RM.Edu.CentralComunicacao.Server.dll; RM.Edu.Lib.Intf.dll

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 27601591 / DEDUPACMEN-8818]** Criação de parametro para enviar os dados do destinatário do serviço na geração de movimento.

Arquivos: RM.EduPS.Facade.Intf.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Aluno.Server.dll; RM.Edu.Aluno.Data.dll; RM.EduPS.Processos.Form.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Aluno.Intf.dll; RM.Edu.Aluno.Form.dll; RM.Edu.Utils.Server.dll; RM.Edu.Facade.dll; RM.EduPS.Processos.Intf.dll; RM.EduPS.Facade.Server.dll; RM.Edu.Financeiro.Form.dll; RM.EduPS.Processos.Data.dll; RM.Edu.Financeiro.Server.dll; RM.Edu.Financeiro.Intf.dll

## 12.1.2602.150

### Rotina: CENTRAL DO CANDIDATO

* **[Ticket: DEDUCAPCOM-10530]** Ajustes central comunicação web

Arquivo: Edu/portalgestaoeducacional

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10503]** Ajustes central comunicação web

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: DEDUCAPCOM-10520]** Acerto para manter opções de enquete cadastradas

Arquivo: Edu/portalgestaoeducacional

### Rotina: RM EXECUTOR (WEB SERVICE)

* **[Ticket: DEDUSAGA-10280]** Ajuste para retornar informação para o usuário ao iniciar atendimento

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.151

### Rotina: Sem Rotina Específica

* **[Ticket: DEDUSAGA-10732]** ajuste no interceptor que altera a url de retorno do signalr

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: DEDUSAGA-10732]** alteração no endereço de conexão do signalR

Arquivo: Edu/portalgestaoeducacional

### Rotina: ALUNOS

* **[Ticket: 27953043 / DEDUBOPE-11839]** Valida descrição ao cadastrar doc

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10520]** Acerto para manter opções de enquete cadastradas ao voltar um passo

Arquivo: Edu/portalgestaoeducacional

### Rotina: GERAR OFERTA

* **[Ticket: DEDUBOPE-11618]** Melhorias no processo de gerar ofertas - Gestão de ofertas.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

### Rotina: PARÂMETROS

* **[Ticket: DEDUCAPCOM-9176]** Criação do processo de exclusão de dados do Meu eduCONNECT

Arquivos: RM.Edu.Interfaces.Intf.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.SmartX.Integracoes.Modelos.Service.dll; RM.Edu.Integracoes.Data.dll; RM.Edu.Menu.dll; RM.Edu.Integracoes.Intf.dll

### Rotina: SALAS/AGENTES DE ATENDIMENTO

* **[Ticket: DEDUSAGA-10830]** Adiciona feedback visual orientando a seleção de uma sala

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.152

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11813]** Inclusão do campo de carga horária total do curso para o Censo Básico.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: DADOS PESSOAIS

* **[Ticket: DEDUBOPE-11435]** Otimização na validação de campos obrigatórios nos dados pessoais do aluno na seção de endereço (Tipo Bairro e Tipo Rua).

Arquivo: Edu/portaleducacional

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: 28107397 / DEDUCAPCOM-10618]** Melhoria no envio de mensagem na central de comunicação no PGECorreção no Filtro de Turmas: Ajustada a listagem de turmas para garantir que códigos idênticos em períodos letivos diferentes não apareçam duplicados na tela.Correção na Seleção de Alunos: Resolvido o que impedia a seleção de alunos devido à duplicidade de registros de turmas. O sistema agora filtra os dados de forma única, normalizando a seleção.

Arquivos: RM.Edu.CentralComunicacao.Data.dll; RM.Edu.Services.Server.dll

* **[Ticket: 28107397 / DEDUCAPCOM-10618]** Melhorias central comunicação web

Arquivo: Edu/portalgestaoeducacional

* **[Ticket: 28107397 / DEDUCAPCOM-10618]** Melhorias na central de comunicação web

Arquivo: Edu/portalgestaoeducacional

### Rotina: PARÂMETROS

* **[Ticket: DEDUCAPCOM-9176]** Criação do processo de exclusão de dados do Meu eduCONNECT

Arquivos: RM.Edu.SmartX.Integracoes.Modelos.Service.dll; RM.Edu.Menu.dll

## 12.1.2602.153

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10171]** Implementação do assistente de IA na Central de Comunicação

Arquivos: RM.Edu.Facade.dll; RM.Edu.CentralComunicacao.Server.dll

### Rotina: IMPORTADOR - TOTVS EDUCACIONAL

* **[Ticket: 27669981 / DEDUBOPE-11786]** Ajuste na importação de arquivo

Arquivo: RM.Edu.Processos.Server.dll

### Rotina: SERVIÇOS

* **[Ticket: DEDUPACMEN-8862]** Melhoria serviço cartão de crédito

Arquivos: RM.Edu.Facade.dll; RM.Edu.Financeiro.Server.dll; RM.Edu.Lib.Intf.dll

## 12.1.2602.154

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11812]** Criados novos campos na Instituição MEC para atender aos Registros 00 e 10 do Censo Básico

Arquivos: RM.Edu.Services.Server.dll; RM.Edu.Academico.Server.dll; RM.Edu.Utils.Server.dll; RM.Edu.Cadastros.Form.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Cadastros.Data.dll; RM.Edu.Cadastros.Intf.dll; RM.Edu.Consts.dll

### Rotina: CONTRATOS

* **[Ticket: 28275565 / DEDUPACMEN-8861]** Melhoria continua no processo de cadastro de contratos

Arquivo: RM.Edu.Financeiro.Data.dll

## 12.1.2602.155

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10172]** Melhorias no educacional

Arquivos: RM.Edu.CentralComunicacao.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Consts.dll; RM.Edu.API.dll

* **[Ticket: DEDUCAPCOM-10172]** Melhorias central comunicação web

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.156

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11813]** Inclusão do campo de carga horária total do curso para o Censo Básico.

Arquivos: RM.Edu.Academico.Server.dll; RM.Edu.Utils.Server.dll

## 12.1.2602.157

### Rotina: ALUNOS

* **[Ticket: 27429690 / DEDUBOPE-11751]** Ajustes nos campos complementares do cadastro do aluno

Arquivos: RM.Edu.AtvCurricular.Data.dll; RM.Edu.Aluno.Data.dll; RM.Edu.Cadastros.Data.dll; RM.Edu.PeriodoLetivo.Data.dll; RM.Edu.MatrizCurricular.Data.dll; RM.Edu.Professor.Data.dll; RM.Edu.Matricula.Data.dll; RM.Edu.Financeiro.Data.dll

### Rotina: PAINEL DO ALUNO

* **[Ticket: 28087090 / DEDUSAGA-10847]** Ajuste na formatação do valores relacionados a prova.

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

## 12.1.2602.158

### Rotina: CONTRATOS

* **[Ticket: DEDUPACMEN-8877]** Foi atualizado a lista dos campos que são usados de referência na FPARAM e FFILIALPARAM, para serem considerados somente aqueles que o usuário informam na tela

Arquivo: RM.Edu.Facade.dll

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8589]** Ajustes no fluxo de geração de lançamento com calculo por credito para melhoria de performance

Arquivo: RM.Edu.Financeiro.Server.dll

## 12.1.2602.161

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8556]** Otimização no processo de movimentações financeiras das disciplinas para a geração de lançamento

Arquivos: RM.Edu.Financeiro.Data.dll; RM.Edu.Processos.Form.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Consts.dll; RM.Edu.MatrizCurricular.Data.dll; RM.Edu.Academico.Intf.dll; RM.Edu.Matricula.Data.dll; RM.Edu.Utils.Server.dll; RM.Edu.Services.Server.dll; RM.Edu.Lib.WinForms.dll; RM.Edu.Financeiro.Server.dll; RM.Edu.Academico.Data.dll; RM.Edu.MatrizCurricular.Server.dll; RM.Edu.Processos.Data.dll; RM.Edu.Matricula.Form.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Processos.Intf.dll; RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.Matricula.Intf.dll; RM.Edu.Matricula.Server.dll; RM.Edu.Financeiro.Form.dll; RM.Edu.Academico.Form.dll; RM.Edu.dll

### Rotina: PAINEL DO ALUNO

* **[Ticket: 28291871 / DEDUBOPE-11896]** Ajustes ao visualizar aluno com irmão cadastrado

Arquivo: RM.Edu.API.dll

## 12.1.2602.162

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11812]** Otimizações no cadastro de Instituição do MEC

Arquivos: RM.Edu.Academico.Server.dll; RM.Edu.Services.Server.dll; RM.Edu.Cadastros.Form.dll

* **[Ticket: DEDUBOPE-11812]** Ajustes no group box de informações de Ensino Indigena na tela de Instituição do MEC

Arquivo: RM.Edu.Cadastros.Form.dll

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: 28552472 / DEDUCAPCOM-10721]** Melhoria nos filtros da Central de Comunicação: Ajustar a consulta por código para utilizar a busca por similaridade (LIKE) e ocultar as matrizes inativas nos filtros.

Arquivo: RM.Edu.Services.Server.dll

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8587]** Melhoria continua no processo de cadastro de bolsas

Arquivo: RM.Edu.Financeiro.Server.dll

### Rotina: MODELO DE FICHA MÉDICA

* **[Ticket: 27433127 / DEDUCAPCOM-10523]** Ajustes para não cortar o texto nos campos da ficha medica

Arquivo: Edu/portalgestaoeducacional

### Rotina: MODELOS DE TURMA

* **[Ticket: 28261876 / DEDUBOPE-11902]** Ajusta listagem dos modelos de turma no planejamento de ofertas

Arquivo: Edu/portalgestaoeducacional

### Rotina: PAGAMENTO BOLETO

* **[Ticket: DEDUPACMEN-8710]** Implementada validação com relação a data do vencimento no registro do boleto hibrido, essa validação já existe no serviço da techfin ou do banco, porém ela retorna uma mensagem não amigável ao usuário (em inglês). Implementando a validação a posteriori, elimina também a necessidade de tentar orquestrar o serviço do financeiro, da techfin e do banco de forma desnecessária

Arquivo: RM.Edu.Facade.dll

### Rotina: PARÂMETROS

* **[Ticket: DEDUCAPCOM-10553]** Feito pequeno ajuste, adicionando os campos de data, operação e registro excluído na resposta da enquete

Arquivos: RM.Edu.Integracoes.Server.dll; RM.Edu.Lib.Intf.dll

* **[Ticket: DEDUCAPCOM-10553]** Feito a criação das apis de mensagens individuais (listar, buscar por id, buscar por mensagem comum, marcar como lida, salvar resposta de enquete, excluir) e suporte a expand (image, attachment, pollResponse).

Arquivos: RM.Edu.Integracoes.Server.dll; RM.Edu.Lib.Intf.dll; RM.Edu.API.dll; RM.Edu.Interfaces.Intf.dll

* **[Ticket: DEDUCAPCOM-10553]** Feito ajuste para não retornar a mensagem individual ao marcar como lida na rota markread, e remove reconversão de datas já persistidas em UTC

Arquivos: RM.Edu.Lib.Intf.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.API.dll

* **[Ticket: DEDUCAPCOM-10553]** Pequeno ajuste na validação de data mínima na busca de mensagens individuais

Arquivo: RM.Edu.API.dll

* **[Ticket: DEDUCAPCOM-10553]** - Feito pequeno ajuste no tipo dos campos operação e registro excluído na resposta da enquete.- Feito ajuste no salvamento de anexos, imagens e mensagens para que não sejam mais salvos no Azure quando o parâmetro estiver habilitado.- Feito pequeno ajuste para obtém o total de mensagens individuais do usuário.- Feito ajuste nas datas de envio e expiração da mensagem individual para o formato UTC, quando a data for válida.

Arquivos: RM.Edu.Interfaces.Intf.dll; RM.Edu.API.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.Lib.Intf.dll

* **[Ticket: DEDUCAPCOM-10553]** Feito ajuste no filtro de busca de mensagem individual para trazer apenas mensagem salva localmente no RM.Ajustado o método de cálculo da data de expiração para retornar DateTimeOffset.MinValue em vez de DateTime.MinValue, evitando distorções com o fuso horário local.

Arquivos: RM.Edu.Integracoes.Server.dll; RM.Edu.Lib.Intf.dll

* **[Ticket: DEDUCAPCOM-10553]** Pequeno ajuste na paginação da busca de mensagens individuais

Arquivo: RM.Edu.API.dll

## 12.1.2602.163

### Rotina: EXECUTOR WEB

* **[Ticket: 28623528 / DEDUSAGA-10947]** adição do arquivo de resources da página de login por token

Arquivos: Portal Corpore.Net

### Rotina: MODELOS DE TURMA

* **[Ticket: 28261876 / DEDUBOPE-11902]** Ajusta colunas e ações na listagem dos modelos de turma no planejamento de ofertas

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.164

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11814]** Implementados novos campos, regras e geração do arquivo para o Registro 20 do Censo Básico 2026

Arquivos: RM.Edu.Utils.Server.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.Academico.Server.dll; RM.Edu.PeriodoLetivo.Data.dll; RM.Edu.Interfaces.Intf.dll; RM.Edu.Lib.Intf.dll; RM.Edu.PeriodoLetivo.Intf.dll; RM.Edu.Consts.dll; RM.Edu.Academico.Intf.dll; RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.Academico.Data.dll

* **[Ticket: DEDUBOPE-11815]** Inclusão da carga horária integralizada pelo aluno no Censo Básico.

Arquivos: RM.Edu.Utils.Server.dll; RM.Edu.Academico.Server.dll

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8556]** Otimização no processo de desmatricular o aluno referente às movimentações financeiras da matricula do aluno

Arquivo: RM.Edu.ProcSel.Server.dll

## 12.1.2602.165

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11814]** Modificada lógica de habiltiação campo de Turma de formação por Alternância no anexo de Turma do MEC

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: DEDUBOPE-11814]** Ajustada validação do campo 29 do Registro 20 do EducaCenso

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: DEDUBOPE-11815]** Inclusão da carga horária integralizada pelo aluno no Censo Básico.

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: TOTVS ASSINATURA ELETRÔNICA

* **[Ticket: 28329601 / DEDUPACMEN-8866]** Implementação obrigatoriedade de assinatura via TAE na rematrícula por curso

Arquivos: RM.Edu.Rest.Server.dll; RM.Edu.Integracoes.Server.dll; RM.Edu.Parametros.Form.dll; Edu/portaleducacional

## 12.1.2602.166

### Rotina: PAGAMENTO BOLETO

* **[Ticket: 27008863 / DEDUPACMEN-8846]** Melhoria extrato financeiro

Arquivo: RM.Edu.Financeiro.Server.dll

## 12.1.2602.167

### Rotina: FALE COM A INSTITUIÇÃO

* **[Ticket: DEDUSAGA-10909]** Ajuste visual no campo de envio de mensagem nas conversas da Sala de Atendimento.

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.168

### Rotina: CENSO ENSINO SUPERIOR

* **[Ticket: 27588077 / DEDUBOPE-11770]** Alteração no processo "Alteração global de professores da turma/disciplina" para inclusão dos novos campos do Censo Superior de 2026

Arquivo: RM.Edu.PeriodoLetivo.Data.dll

### Rotina: ENTURMAÇÃO DE TURMA MISTA

* **[Ticket: 26556042 / DEDUBOPE-11581]** Melhorias de segurança e performance

Arquivo: RM.Edu.Matricula.Form.dll

### Rotina: INSTALAÇÃO

* **[Ticket: DEDUSAGA-10999]** remoção de arquivo que não está sendo usado

Arquivo: Edu/portaleducacional

### Rotina: LOGIN

* **[Ticket: 28242683 / DEDUSAGA-10986]** Correção do login LDAP no portal do aluno

Arquivos: FrameHTML/RM.Edu.WebAPI.dll

### Rotina: PAGAMENTO BOLETO

* **[Ticket: 27008863 / DEDUPACMEN-8846]** Melhoria extrato financeiro

Arquivo: RM.Edu.Financeiro.Server.dll

## 12.1.2602.170

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: 28865558 / DEDUBOPE-11964]** Ajustes no cadastro e processo de edição em lote de Turmas do MEC no Ensino Básico

Arquivos: RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.PeriodoLetivo.Server.dll

* **[Ticket: 28865558 / DEDUBOPE-11964]** Ajustada validação do campo Etapa Agregada no cadastro e processo de Turma do MEC no Ensino Básico

Arquivo: RM.Edu.PeriodoLetivo.Server.dll

* **[Ticket: 28865558 / DEDUBOPE-11964]** Ajustada regra de seleção de Etapa Agregada no cadastro e processo de Turma do MEC quando houver Local de ensino diferenciado

Arquivos: RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.PeriodoLetivo.Server.dll

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 27672093 / DEDUPACMEN-8767]** Ajuste para enviar somente o primeiro email para a nota fiscal quando o aluno possui mais de um.

Arquivos: RM.Edu.Financeiro.Server.dll; RM.Edu.Aluno.Server.dll

### Rotina: IMPORTAÇÃO DE FOTOS

* **[Ticket: 28858164 / DEDUBOPE-11963]** Ajustes ao importar foto do aluno

Arquivos: RM.Edu.Processos.Data.dll; RM.Edu.Aluno.Server.dll

### Rotina: VISÕES DE DADOS (SQL)

* **[Ticket: 29010127 / DEDUBOPE-11991]** Ajusta rotina de alunos inscritos de forma que seja listada na busca de acoes para serem inseridas em consultas sql.

Arquivo: RM.Edu.AtvCurricular.Form.dll

## 12.1.2602.171

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: 28865558 / DEDUBOPE-11964]** Ajustes nas consultas de geração dos registros do Educa Censo

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: 28865558 / DEDUBOPE-11964]** Ajustado comportamento de seleção de local diferenciado no processo de alteração em lote de Turmas do MEC

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: 28865558 / DEDUBOPE-11964]** Otimizações no cadastro de Turmas do MEC

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

* **[Ticket: DEDUBOPE-11975]** Inclusão da opção de não enviar carga horária para o Censo.

Arquivos: RM.Edu.Cadastros.Intf.dll; RM.Edu.Cadastros.Form.dll; RM.Edu.Cadastros.Data.dll; RM.Edu.Academico.Server.dll; RM.Edu.Utils.Server.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUSAGA-10590]** Implementa validação de perfil (professor e coordenador) checando as permissões.

Arquivos: RM.Edu.API.dll; RM.Edu.PeriodoLetivo.Server.dll

### Rotina: TABELA DE PREÇO

* **[Ticket: 28424028 / DEDUPACMEN-8904]** Simulação na matrícula usando tabela de preço

Arquivo: RM.Edu.Financeiro.Server.dll

## 12.1.2602.173

### Rotina: ANEXOS - ATIVIDADES AGENDADAS

* **[Ticket: DEDUCAPCOM-10714]** Implementação da integração Smartlink com a RDStation

Arquivos: RM.Edu.RDStation.Marketing.SmartLink.Server.dll; RM.Edu.RDStation.Marketing.SmartLink.Form.dll; RM.Edu.RDStation.Marketing.SmartLink.Intf.dll; RM.Edu.Menu.dll; RM.Edu.Consts.dll; RM.Edu.Lib.Intf.dll; RM.Edu.RDStation.Marketing.SmartLink.Service.dll; RM.Edu.ProcSel.Server.dll; RM.Edu.RDStation.Marketing.SmartLink.Data.dll

* **[Ticket: DEDUCAPCOM-10714]** Ajustes do projeto RD Station

Arquivos: RM.Edu.Classes.Server.dll; RM.Edu.RDStation.Marketing.SmartLink.Data.dll

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: DEDUBOPE-11975]** Inclusão da opção de não enviar carga horária para o Censo.

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: 29114866 / DEDUBOPE-12039]** Alteração na consulta do registro 60 para levar em conta os novos campos do registro 20 para os campos 21 e 22

Arquivos: RM.Edu.PeriodoLetivo.Server.dll; RM.Edu.Academico.Server.dll; RM.Edu.Consts.dll; RM.Edu.PeriodoLetivo.Form.dll; RM.Edu.PeriodoLetivo.Intf.dll

* **[Ticket: 29114866 / DEDUBOPE-12039]** Otimizado campo de atendimento diferenciado no cadastro e processo de Turmas do MEC no Ensino Básico

Arquivo: RM.Edu.PeriodoLetivo.Form.dll

### Rotina: CURSOS/MATRIZES CURRICULARES

* **[Ticket: 29051805 / DEDUBOPE-12018]** Corrigindo exibição dos valores de carga horária na matriz curricular.

Arquivo: RM.Edu.MatrizCurricular.Data.dll

### Rotina: EXECUTOR WEB

* **[Ticket: 28623528 / DEDUSAGA-10947]** alteração na versão da biblioteca de componentes utilizada no portal

Arquivo: Edu/portaldoprofessor

### Rotina: MATRICULAR PROCESSO SELETIVO RM

* **[Ticket: 28689264 / DEDUCAPCOM-10823]** Realizado ajuste para considerar apenas registros válidos, evitando inconsistências durante a gravação das habilitações dos alunos.

Arquivo: RM.Edu.Facade.dll

### Rotina: OCORRÊNCIAS

* **[Ticket: 29098225 / DEDUSAGA-11053]** Ajuste de responsividade na tabela de ocorrências de alunos

Arquivo: Edu/portaldoprofessor

### Rotina: PARÂMETROS

* **[Ticket: 27711471 / DEDUBOPE-11879]** Correção na ativação da instituição do MEC, migrando vínculos de direção sem filial antes da exclusão do registro antigo e preservando a integridade dos dados.

Arquivo: RM.Edu.Academico.Server.dll

* **[Ticket: 28493518 / DEDUBOPE-11909]** Ajuste ao mostrar fórmula visual global

Arquivo: RM.Edu.Parametros.Form.dll

* **[Ticket: 28493518 / DEDUBOPE-11909]** Ajuste ao mostrar fórmulas visuais globais

Arquivo: RM.Edu.Parametros.Form.dll

### Rotina: RM EXECUTOR (WEB SERVICE)

* **[Ticket: DEDUSAGA-10857]** alteração no caminho aonde os testes unitários são gerados

Arquivo: Edu/portaldoprofessor

## 12.1.2602.174

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: 28865558 / DEDUBOPE-12040]** Alterado envio padrão de novos campos do Registro 30 no Censo Básico

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CENTRAL DE COMUNICAÇÕES

* **[Ticket: 26835583 / DEDUCAPCOM-10513]** Ajustes para evitar emails duplicados durante a rotina de notificação de boleto proximo ao vencimento

Arquivo: RM.Edu.Academico.Server.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DEDUBOPE-12059]** Melhorias de performance e segurança

Arquivos: RM.Edu.RDStation.Marketing.SmartLink.Intf.dll; RM.Edu.RDStation.Marketing.SmartLink.Server.dll; RM.Edu.Matricula.Server.dll; RM.Edu.Lib.Intf.dll

### Rotina: METADADOS

* **[Ticket: 29123619 / DEDUBOPE-12068]** Ajuste no menu executar para aparecer EduHabilitacaoFilialAction e EduHabilitacaoAction

Arquivo: RM.Edu.MatrizCurricular.Form.dll

### Rotina: NOTAS E FALTAS DE AVALIAÇÃO

* **[Ticket: 29097450 / DEDUSAGA-11052]** Ajuste para manter as permissões do usuário logado atualizadas.

Arquivo: Edu/portaldoprofessor

### Rotina: PAINEL DO ALUNO

* **[Ticket: 29201140 / DEDUSAGA-11082]** Ajuste para apresentar notas com 'Vírgula' e não com 'Ponto' no gráfico de notas.

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.175

### Rotina: ANÁLISE CURRICULAR

* **[Ticket: 26436951 / DEDUBOPE-11485]** Criando logica para evitar reprovação no aproveitamento do curso.

Arquivo: RM.Edu.Historico.Data.dll

### Rotina: CENSO ENSINO BÁSICO

* **[Ticket: 29058691 / DEDUBOPE-12019]** Refatorado campo 180 do Registro 10 do Censo Básico para permitir a seleção de valores corretos

Arquivos: RM.Edu.Cadastros.Form.dll; RM.Edu.Cadastros.Intf.dll; RM.Edu.Consts.dll

### Rotina: FORMULA VISUAL

* **[Ticket: 29207574 / DEDUPACMEN-9024]** Disponbilização da lista de contratos selecionados da contabilização na lista de parâmetros do processo.

Arquivos: RM.Edu.Contabil.Data.dll; RM.Edu.Lib.Intf.dll; RM.Edu.Contabil.Form.dll; RM.Edu.Contabil.Intf.dll

### Rotina: PAINEL DO ALUNO

* **[Ticket: 29201140 / DEDUSAGA-11082]** Ajuste para apresentar notas com 'Vírgula' e não com 'Ponto' no gráfico de notas.

Arquivo: Edu/portalgestaoeducacional

## 12.1.2602.176

### Rotina: FORMULA VISUAL

* **[Ticket: 29207574 / DEDUPACMEN-9024]** Ajuste na inicialização da lista de contratos do processo de contabilização quando utilizado via Webservice.

Arquivos: RM.Edu.Contabil.Data.dll; RM.Edu.Contabil.Intf.dll

### Rotina: OCORRÊNCIAS

* **[Ticket: 29098225 / DEDUSAGA-11053]** Ajuste de responsividade na tabela de ocorrências de alunos

Arquivo: Edu/portaldoprofessor

### Rotina: TABELA DE PREÇO

* **[Ticket: DEDUPACMEN-9048]** Ajuste para funcionamento da gestão de fiador após atualização para angular 21

Arquivo: Edu/portalgestaoeducacional

# TOTVS Folha de Pagamento

## 12.1.2602.100

### Rotina: AUTOMAÇÃO

* **[Ticket: DAUDITPROJ-462]** Retirado do publicador que informar o término de calculo na fila de mensageria.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: ENVIO DE DADOS PARA A FEEDZ

* **[Ticket: DRHROTRM-14773]** fix: Exibir mensagem de descontinuação somente para performance e metas

Arquivo: RM.Fop.Integracao.Form.dll

### Rotina: EVENTOS PERIÓDICOS

* **[Ticket: DRHROTRM-17328]** Ajuste na geração do evento S-1210 para imprimir a dedução de dependente sempre que tiver valor no cadastro

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 26542284 / DRHROTRM-17332]** Ajuste na antecipação de férias para considerar a data de pagamento das férias para funcionários transferidos

Arquivo: RM.Fop.Dominio.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: DRHROTRM-17261]** Ajuste na localização do campo Data da entrega que passa a ficar nos parâmetros Específicos do informe de rendimentos

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: DRHROTRM-17261]** Liberação da dirf por conferência

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: DRHROTRM-17261]** Ajuste para carregar parâmetros e identificar código de quebra, ao salvar dados por requisição REST no FopHstAftData

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: RELAT. - RELATÓRIO CONFERÊNCIA IRRF (TAF)

* **[Ticket: 26251312 / DRHROTRM-16645]** Ajuste no relatório de conferência de IRRF para eventos que estornam IRRF

Arquivo: RM.Fop.Relatorios.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26288503 / DRHROTRM-17274]** Na geração do relatório de conferência S5002 funcionário com IRRF férias dedução: \* Exibe corretamente os valores da folha.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26465300 / DRHROTRM-17165]** Na geração do relatório de conferência S5002 com dependente sem INCIRRF, porém em periodos anteriores era dependente INCIRRF = 1: \* Exibe corretamente os valores do dependente

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26395913 / DRHROTRM-17222]** Na geração do relatório de conferência, dependente ano caixa superior a competência: \* Obtém corretamente a dedução.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26563771 / DRHROTRM-17395]** Na geração do relatório de conferência informações complementares, cuja quantidade de chapas é um multiplo exato de 999:\* Segmenta corretamente a paginação do lote, evitando um lote vazio.

Arquivos: RM.Fop.Lib.Intf.dll; RM.Fop.Api.dll

* **[Ticket: 26353420 / DRHROTRM-17253]** Na geração do relatório de conferência S5002 com base negativa: \* Exibe valor zerado conforme leiaute do esocial.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26278102 / DRHROTRM-16953]** No relatório de conferência S5002 contendo evento com dedução de IRRF: \* Considera como dedução

Arquivos: RM.Fop.Esocial.Intf.dll; RM.Fop.Esocial.Data.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 26313756 / DRHROTRM-17334]** Ajuste na tela Informações Complementares Períodos Anteriores S-1210" para retificar o evento S-1210 de funcionários demitidos em 12/2024 com pagamento em 01/2025

Arquivos: RM.Fop.Esocial.Server.dll; RM.Fop.Api.dll; RM.Fop.Esocial.Data.dll

* **[Ticket: 26494365 / DRHROTRM-17300]** Ajuste no evento S-1210 para funcionários com eventos a serem retificados em 01/2025 na competência 12/2024

Arquivos: RM.Fop.Dominio.dll; RM.Fop.Infraestrutura.Repositorios.dll

## 12.1.2602.101

### Rotina: CONFIGURAÇÕES

* **[Ticket: DRHMEURH-20746]** Possibilitar a visualização de documentos com email pessoal na integração com TAE | Meu RH

Arquivos: FrameHTML/RM.Fop.WebAPI.dll

### Rotina: ENVIAR E-MAILS PARA FUNCIONÁRIOS

* **[Ticket: 25679585 / DRHROTRM-16112]** Ajuste para obter Nome Fantasia da empresa no Envio Global de E-mails

Arquivo: RM.Fop.Lib.Data.dll

### Rotina: FÉRIAS - LANÇ. EMPRÉSTIMO CRÉDITO DO TRABALHADOR

* **[Ticket: 26093699 / DRHCALCRM-11346]** Tratramento no cálculo das férias para verificar se o arquivo já foi importado na competência, antes de efetuar o lançamento do provisionamento do credito do trabalhador

Arquivos: RM.Fop.Calc.CalculosBase.dll; RM.Fop.Calc.Calculos.dll

### Rotina: IMPORTAÇÃO - IMPORTAÇÃO DO EMPRÉSTIMO CONSIGNADO - CRÉDITO DO TRABALHADOR SOCIAL

* **[Ticket: DRHCALCRM-11376]** Inclusão melhoria de controle para provisionamento Crédito Trabalhador.

Arquivos: RM.Fop.CalcularFolha.Intf.dll; RM.Fop.Parametros.Form.dll; RM.Fop.Rotinas.Data.dll; RM.Fop.Parametros.Intf.dll; RM.Fop.CalcularFolha.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26505964 / DRHROTRM-17431]** Na geração do relatório de conferência S5002 com retificação tag (perAnt) contida em infoIRComplem:\* gera corretamente o relatório.

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Intf.dll

### Rotina: RESCISÃO

* **[Ticket: 21376164 / DRHCALCRM-7222]** Tratativa do FGTS Digital quando o valor adiantado de 13º salário é maior que o valor final do 13º proporcional devido ao funcionário na rescisão.

Arquivos: RM.Fop.Const.Intf.dll; RM.Fop.Calc.CalculosBase.dll; RM.Fop.Calc.Calculos.dll

## 12.1.2602.103

### Rotina: CÁLCULO

* **[Ticket: 25702760 / DRHCALCRM-10983]** No cálculo da media utilizando a opção de maiores valores estava sendo considerado mês onde o valor do evento estava zerado.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26634440 / DRHROTRM-17565]** Na geração do relatório de conferência S5002:\* Prover corretamente estado de processamento para tela.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.105

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 26609965 / DRHROTRM-17481]** Ajuste no informe de rendimentos para não exibir mensagem de desconto simplificado

Arquivo: RM.Fop.Relatorios.Form.dll

* **[Ticket: 26341336 / DRHROTRM-17535]** Ajuste no informe de rendimentos para funcionários com múltiplos vinculos onde um dos vinculos possui base de IRRF negativo devido a faltas

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26424673 / DRHROTRM-17496]** Na geração do relatório de conferência S5002 tendo funcionário transferido:\* Determina corretamente qual envelope usar.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.106

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 26605387 / DRHROTRM-17639]** Ajuste no informe de rendimentos para funcionário com devolução de assistência saúde no dependente

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: MEU RH - DEMONSTRATIVO DE PAGAMENTO

* **[Ticket: 26633485 / DRHCALCRM-11659]** Implementado ajuste na visualização do envelope de pagamento, desconsiderando a exibição de eventos com valor zerado, visando melhorar a clareza e legibilidade das informações apresentadas ao colaborador.

Arquivo: RM.Fop.Envelope.Data.dll

### Rotina: MEU RH - GESTÃO DE FÉRIAS EQUIPE

* **[Ticket: 26095283 / DRHMEURH-20640]** Ajuste na visualização do filtro de equipes da gestão de férias do Meu RH.

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: PORTAL WEB - SUBORDINADOS (LAB.01.213)

* **[Ticket: DRHHCM-17030]** Ajuste na visualização de subordinados de supervisores

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: DRHROTRM-15716]** Na geração do relatório de conferência S5002: \* Gera valores relativos autonomos externos.

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Intf.dll

* **[Ticket: DRHROTRM-17463]** Na geração do relatório de conferência S5002: \* Permite conferência dos autonomos.

Arquivos: RM.Fop.Esocial.Intf.dll; RM.Fop.Esocial.Data.dll

## 12.1.2602.107

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 26617475 / DRHROTRM-17672]** Ajuste no informe de rendimentos para permitir informar os valores de juros de mora

Arquivos: RM.Fop.Relatorios.Data.dll; RM.Fop.Relatorios.Form.dll

### Rotina: FÉRIAS - LANÇ. EMPRÉSTIMO CRÉDITO DO TRABALHADOR

* **[Ticket: 26214736 / DRHCALCRM-11410]** Correção de exclusões feitas ao editar dias de férias.

Arquivo: RM.Fop.FuFerias.Data.dll

* **[Ticket: 26214736 / DRHCALCRM-11410]** Verifica arredondamento dos valores do provisionamento do credito do trabalhador nas ferias, quando nos dois meses ocorre 5 na terceira casa decimal.

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: MIDDLEWARE - RELATÓRIO CONFERÊNCIA IRRF

* **[Ticket: 26663226 / DRHROTRM-17624]** Na geração do relatório de conferência S5002 RRA:\* Processa os valores corretamente.

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26634614 / DRHCALCRM-11651]** Revisão dos códigos de cálculos considerados no cálculo base IRRF Férias

Arquivo: RM.Fop.Calc.CalculosBase.dll

* **[Ticket: 26633890 / DRHROTRM-17644]** Na geração do relatório de conferência S5002 quando funcionário tem dependente lançado duplicado: \* Considera somente um dependente pelo cpf e tipoRendimento.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26587054 / DRHROTRM-17669]** Na geração do relatório de conferência S5002 com diversos autonomos:\* consulta corretamente os valores.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.108

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 26633276 / DRHROTRM-17626]** Liberação da DIRF para clientes que se enquadram no Art. 2º da Portaria RFB nº 632

Arquivo: RM.Fop.Relatorios.Form.dll

## 12.1.2602.109

### Rotina: IMPORTAÇÃO - IMPORTAÇÃO DO EMPRÉSTIMO CONSIGNADO - CRÉDITO DO TRABALHADOR SOCIAL

* **[Ticket: DRHCALCRM-10245]** Importação Crédito Trabalhador via API

Arquivos: RM.Fop.CalcularFolha.Form.dll; RM.Fop.CalcularFolha.Intf.dll; RM.Fop.Parametros.Form.dll; RM.Fop.Common.Intf.dll; RM.Fop.CalcularFolha.Data.dll; RM.Fop.Lib.Intf.dll

## 12.1.2602.110

### Rotina: DIRF/INF.REND.- CONVERSÃO DE OPERADORA PERFIL X CADASTRO

* **[Ticket: 26601465 / DRHROTRM-17732]** Na geração do relatório de conferência S5002 havendo funcionário transferido entre coligadas:\* Gera corretamente as informações da coligada origem e destino.

Arquivos: RM.Fop.Esocial.Intf.dll; RM.Fop.Relatorios.Data.dll; RM.Fop.Esocial.Data.dll; RM.Fop.Relatorios.Intf.dll

### Rotina: ESCALA DE FÉRIAS

* **[Ticket: 22907269 / DRHCALCRM-8088]** Ajuste no processo de aprovação de férias para funcionários com registro de faltas, permitindo a aprovação sem exibição de aviso quando não houver perda de dias de direito decorrente das faltas.

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: IMPORTAÇÃO - IMPORTAÇÃO DO EMPRÉSTIMO CONSIGNADO - CRÉDITO DO TRABALHADOR SOCIAL

* **[Ticket: DRHCALCRM-10245]** Importação Crédito Trabalhador via API

Arquivos: RM.Fop.Lib.Extensions.dll; RM.Fop.CalcularFolha.Form.dll; RM.Fop.Utils.Intf.dll; RM.Fop.Utils.Server.dll

### Rotina: MIDDLEWARE - GERAL/ OUTROS

* **[Ticket: 26623994 / DRHROTRM-17522]** Liberação da nota técnica do eSocial S-1.3 NT 06/2026

Arquivos: RM.FopFolha.dll; RM.Fop.Const.Intf.dll; RM.Fop.Parametros.Form.dll; RM.Fop.Esocial.Intf.dll; RM.Fop.Dominio.dll; RM.Fop.Common.Data.dll; RM.Fop.Esocial.Form.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26621140 / DRHROTRM-17741]** Na geração do relatório de conferência S5002 quando existe um evento de restituição IRRF:\* Realiza a subtração.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26712815 / DRHROTRM-17754]** Na geração do relatório de conferência S5002 com evento de previdência que deduz:\* Gera relatório corretamente exibindo previdência complementar.

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Intf.dll

* **[Ticket: DRHROTRM-17808]** Corrige inconsistência análise de impactos dll RM.Fop.Esocial.Data.TesteUnitario.dll

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.111

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 26707718 / DRHROTRM-17743]** Ajuste no informe de rendimentos na discriminação dos valores de pensão dos dependentes de RRA

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: ENVIO DE DADOS PARA A FEEDZ

* **[Ticket: DRHROTRM-14773]** feat (Feedz) : Envio por token por seção

Arquivos: RM.Fop.Integracao.Data.dll; RM.Fop.Parametros.Data.dll; RM.Fop.Parametros.Intf.dll; RM.Fop.Parametros.Form.dll

* **[Ticket: DRHROTRM-14773]** fix: implementação dos prefixos de tokens

Arquivos: RM.Fop.Integracao.Data.dll; RM.Fop.Parametros.Form.dll

### Rotina: LOTAÇÃO TRIBUTÁRIA

* **[Ticket: 26533326 / DRHROTRM-17444]** fix: resolve ambiguidade SQL e mapeamento de campos no lookup de CEI

Arquivo: RM.Fop.Esocial.Form.dll

### Rotina: SMART VIEW

* **[Ticket: 24933524 / DRHCALCRM-11192]** Correção na busca pelos Dados INSS das Seções no relatório de Provisão de Férias - SmartView

Arquivos: RM.Fop.FuFerias.Data.dll; RM.Fop.NativeProvider.Service.dll

### Rotina: SOLICITAÇÃO DE FÉRIAS

* **[Ticket: 26537717 / DRHMEURH-20931]** Ajuste na visualização dos dias disponíveis de férias no Meu RH, para o correto funcionamento.

Arquivo: RM.Fop.Rest.Server.dll

## 12.1.2602.112

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26459872 / DRHMEURH-20885]** Ajuste na mensagem de validação de salário na requisição de substituição | Meu RH

Arquivos: RM.Fop.Rest.Server.dll; RM.Fop.Rest.Intf.dll

### Rotina: GERAÇÃO DOS LANÇAMENTOS

* **[Ticket: 26441746 / DRHROTRM-17049]** Ajuste na contabilização ao excluir um lote que possui integração com o protheus

Arquivo: RM.Fop.Rotinas.Server.dll

### Rotina: MIDDLEWARE - RELATÓRIO CONFERÊNCIA IRRF

* **[Ticket: 26785799 / DRHROTRM-17880]** Na geração do relatório de conferência S5002 com pensão de férias pagas anterior a competência do envelope: \* Encontra corretamente as movimentações do dependente pensão e contabiliza.

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Intf.dll

### Rotina: S-1200 - REMUNERAÇÃO TRABALHADOR - RGPS

* **[Ticket: 25904653 / DRHROTRM-16546]** Ajuste na geração do evento S-1200 anual para funcionários MV onde um dos vinculos é autônomo do financeiro

Arquivo: RM.Fop.Dominio.dll

### Rotina: S-3500 - EXCLUSÃO DE EVENTOS - PROC. TRABALHISTA

* **[Ticket: 26265202 / DRHROTRM-16978]** Ajuste no processo de gerar evento de exclusão para o S-3500

Arquivos: RM.Fop.Dominio.dll; RM.Fop.Esocial.Data.dll

## 12.1.2602.113

### Rotina: COMPATIBILIZAÇÃO - UPGRADE DE RELEASE/VERSÃO (BSO)

* **[Ticket: 26692097 / DRHROTRM-17868]** Ajuste na tela Informações Complementares Períodos Anteriores S-1210" para retificar o evento S-1210 de funcionários demitidos em 12/2024 com pagamento em 02/2026

Arquivo: RM.Fop.Api.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: 26451424 / DRHROTRM-17291]** Na integração com Ahgora, no envio de funcionário campos nome\_chefia e matricula\_chefia:\* Encontra corretamente o supervisor.

Arquivos: RM.Fop.ChefeSupervisor.Data.dll; RM.Fop.Funcionario.Server.dll; RM.Fop.ChefeSupervisor.Intf.dll; RM.Fop.Paramquiosque.Intf.dll; RM.Fop.Lib.Intf.dll; RM.Fop.Paramquiosque.Data.dll; RM.Fop.Integracao.Intf.dll

### Rotina: FÉRIAS - LANÇ. EMPRÉSTIMO CRÉDITO DO TRABALHADOR

* **[Ticket: 26673225 / DRHCALCRM-11727]** Credito do trabalhador - Provisionamento férias

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: MINHA EQUIPE

* **[Ticket: 26194131 / DRHHCM-16951]** Ajuste na visualização de subordinados diretos com filtro de usuário

Arquivo: RM.Fop.Funcionario.Data.dll

## 12.1.2602.114

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26799425 / DRHMEURH-21176]** Ajuste no carregamento de campos complementares na edição de requisição, para correta visualização.

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: 26544826 / DRHROTRM-17935]** Ao visualizar detalhes do log, visualiza corretamente o mês do log

Arquivo: Fop/fop-logger

### Rotina: HISTÓRICOS

* **[Ticket: 26720023 / DRHROTRM-17845]** Ajuste no cadastro de funcionário ao acessar o histórico salarial pela aba Históricos

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: IMPORTAÇÃO - IMPORTAÇÃO DO EMPRÉSTIMO CONSIGNADO - CRÉDITO DO TRABALHADOR SOCIAL

* **[Ticket: DRHCALCRM-11789]** Inclusão código defensivo para API Crédito Trabalhador

Arquivo: RM.Fop.Lib.Extensions.dll

* **[Ticket: DRHCALCRM-11796]** Ajuste integração Crédito Trabalhador via cliente piloto.

Arquivos: RM.Fop.CalcularFolha.Data.dll; RM.Fop.CalcularFolha.Form.dll

### Rotina: INTEGRAÇÕES - CONCEITO E WEBSERVICE

* **[Ticket: 25299232 / DRHCALCRM-10353]** Correção para efetuar integração com DataServer FopAvisoPrevioData via API.

Arquivo: RM.Fop.Rescisao.Data.dll

### Rotina: MINHA EQUIPE

* **[Ticket: 26787830 / DRHMEURH-21170]** Ajuste no avanço de etapa na requisição de transferência quando salário não é informado | Meu RH

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: NOVA SOLICITAÇÃO

* **[Ticket: DRHCONS-8873]** Melhorias nos Logs Meu RH- Consignado

Arquivos: FrameHTML/RM.Fop.Lib.WebAPI.dll

### Rotina: QUIRONS

* **[Ticket: 26613326 / DRHMEURH-21144]** Ajuste para permitir utilização do ambiente sandbox do Quirons | Meu RH

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: RELAT. - RELATÓRIO CONFERÊNCIA INSS PATRONAL

* **[Ticket: 25310224 / DRHROTRM-16193]** Ajuste no relatório patronal para funcionários transferidos com dissidio

Arquivos: RM.Fop.Relatorios.Data.dll; RM.Fop.Dominio.dll; RM.Fop.Esocial.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26675115 / DRHROTRM-17881]** Na geração do relatório de conferência S5002 com um autonomo MEI:\* Gera relatório corretamente.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.115

### Rotina: LOTAÇÃO TRIBUTÁRIA

* **[Ticket: 26775249 / DRHROTRM-17941]** fix: resolve ambiguidade SQL e mapeamento de campos no lookup de CEI

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Form.dll

### Rotina: PERÍODO DE APURAÇÃO

* **[Ticket: DRHROTRM-18005]** fix: remove baseUrl e ajusta mapeamento da coluna CODCOLESTABTOMADOR

Arquivo: RM.Fop.Api.dll

### Rotina: TOTVS ASSINATURA ELETRÔNICA

* **[Ticket: 26543859 / DRHCALCRM-11616]** Ajuste da regra para cadastro do id de grupo

Arquivos: RM.Fop.TotvsSign.Intf.dll; RM.Fop.TotvsSign.Data.dll

## 12.1.2602.116

### Rotina: ALT. CAD. - ALTERAÇÃO CAMPOS DO CADASTRO

* **[Ticket: DRHROTRM-15753]** fix: realizar alteração de status considerando o código de vaga

Arquivos: RM.Fop.Funcionario.Intf.dll; RM.Fop.Funcionario.Server.dll; RM.Fop.ATS.Server.dll; RM.Fop.ATS.IService.dll; RM.Fop.ATS.Service.dll; RM.Fop.Funcionario.Form.dll

* **[Ticket: 26903066 / DRHROTRM-18009]** Ajuste no processo de alteração global de campos do cadastro do funcionário para gerar gatilho do evento S-2206 quando o campo código da categoria do eSocial é alterado

Arquivo: RM.Fop.Rotinas.Data.dll

* **[Ticket: DRHROTRM-15753]** feat : Implementação de atualização do status do ATS

Arquivos: RM.Fop.ATS.Service.dll; RM.Fop.Funcionario.Form.dll

* **[Ticket: DRHROTRM-15753]** fix: não deve validar o código de vaga registro preliminar

Arquivo: RM.Fop.Funcionario.Form.dll

### Rotina: CADASTRO

* **[Ticket: 25488087 / DRHROTRM-16096]** fix: adição de verificação entre data de admissão e data de transferência na alteração do código da seção

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 26884352 / DRHROTRM-17981]** Ajuste no informe de rendimentos para considerar o código de cálculo 85 quando o código de cálculo 89 estiver zerado

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: 26544826 / DRHROTRM-17935]** Na integração com Ahgora cujos funcionários e afastamentos não contenham codInterno preenchido na base:\* Atualiza codinterno e valida o status na Ahgora corretamente.

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: MINHA EQUIPE

* **[Ticket: 26413181 / DRHHCM-17040]** Ajuste na visualização de subordinados diretos de chefes de outras coligadas

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26544943 / DRHCALCRM-11691]** Alteração no evento de licença remunerada lançado nas férias coletivas, para gravar zero na flag que indica que é verba de férias

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.Calc.CalculosBase.dll

### Rotina: TOTALIZADORES - S-5002/ S-5012 - IRRF

* **[Ticket: 26506343 / DRHROTRM-17936]** Na geração do relatório de conferência S5002 comm funcionário transferido no mesmo mês / ano da geração do relatório porém com data pagamento diferente da data de transferência: \* Não gera duplicidade das informações

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.117

### Rotina: ANEXOS - FOLHA DE PAGAMENTO

* **[Ticket: DRHCALCRM-11781]** Correção Metodo POST no dataserver RestAPI FopEventoProgramadoData quando for mais de um registro

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: DIFERENÇA 13° SALÁRIO

* **[Ticket: 26365019 / DRHCALCRM-11564]** No cálculo da segunda diferença de 13o a base de INSS está considerando o valor da primeira diferença em duplicidade

Arquivos: RM.Fop.Calc.CalculosBase.dll; RM.Fop.Calc.Calculos.dll

### Rotina: INTEGRAÇÃO - GERAL/ OUTROS

* **[Ticket: 26572363 / DRHROTRM-17435]** Ajuste na geração dos eventos S-1200 e S-1210 de autônomo externo para considerar o campo código do cadastro do autônomo externo na tag ideDmDev

Arquivos: RM.Fop.Infraestrutura.Repositorios.dll; RM.Fop.Dominio.dll; RM.Fop.Relatorios.Data.dll

### Rotina: OUTROS PROC. - RETIFICAÇÃO INFO. COMPL. S-1210

* **[Ticket: 26851096 / DRHROTRM-17943]** Ajuste no evento S-1210 de retificação quando o funcionário possui plano de saúde e evento de IRRF mas não possui dedução de dependente

Arquivo: RM.Fop.Dominio.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26587054 / DRHROTRM-17669]** Na geração do relatório de conferência S5002 para um período que foi retificado: \*Realiza leitura da tag infoIRComplem do governo retificada.

Arquivos: RM.Fop.Lib.Server.dll; RM.Fop.Lib.Intf.dll; RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Intf.dll

* **[Ticket: 26738612 / DRHROTRM-17877]** Na geração do relatório de conferência S5002 com desconto de PLR (CC126):\* Realizar corretamente desconto da PLR.

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: TOTALIZADORES - S-5001/ S-5011 - CONTRIBUIÇÕES SOCIAIS

* **[Ticket: 25871255 / DRHROTRM-16521]** Ajuste no relatório patronal anual de obra própria para buscar o FAP cadastrado no CEI do tomador de serviço

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.118

### Rotina: DIFERENÇA 13° SALÁRIO

* **[Ticket: 26365019 / DRHCALCRM-11564]** No cálculo da segunda diferença de 13o a base de INSS está considerando o valor da primeira diferença em duplicidade

Arquivo: RM.Fop.Calc.Calculos.dll

## 12.1.2602.119

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26343462 / DRHMEURH-20756]** Permitir desabilitar justificativa na requisição de desligamento | Meu RH

Arquivos: FrameHTML/RM.Fop.WebAPI.dll

### Rotina: DIFERENÇA 13° SALÁRIO

* **[Ticket: 26365019 / DRHCALCRM-11564]** No cálculo da segunda diferença de 13o a base de INSS está considerando o valor da primeira diferença em duplicidade

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: DRHROTRM-17477]** Na geração do relatório de conferência S5002 havendo devolução de plano de saúde:\* Debita corretamente a devolução no totalizador.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26999671 / DRHROTRM-18086]** Na geração do relatório de conferência S5002 tendo vários dependentes com mesmo CPF e movimentação de plano de saúde:\* Gera relatório corretamente.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.120

### Rotina: EVENTOS PERIÓDICOS

* **[Ticket: 26996068 / DRHROTRM-18082]** Ajuste no evento S-1210 para não imprimir o grupo planSaude caso não tenha valor de assistência saúde para o titular e tenha devolução do plano de saúde zerando o valor do dependente

Arquivo: RM.Fop.Dominio.dll

### Rotina: NOVA SOLICITAÇÃO

* **[Ticket: DRHCONS-8925]** Disponibilizar UserAgent no envio da Simulação Totvs Consignado.

Arquivo: RM.Fop.Rest.Intf.dll

### Rotina: RELAT. - RELATÓRIO CONFERÊNCIA INSS PATRONAL

* **[Ticket: 25976325 / DRHROTRM-17264]** Ajuste na rotina que carrega distribuição de tomador para que caso não exista valor no histórico utilize o tomador empresa

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.121

### Rotina: PARAMETRIZADOR - ESOCIAL

* **[Ticket: 24821471 / DRHROTRM-15563]** Criação do campo data de mudança no cadastro de observações contratuais e tratamento nos eventos do eSocial

Arquivos: RM.Fop.Utils.Intf.dll; RM.Fop.Dominio.dll; RM.Fop.Funcionario.Intf.dll; RM.Fop.Funcionario.Form.dll; RM.Fop.Utils.Server.dll; RM.Fop.Funcionario.Data.dll; RM.Fop.Common.Intf.dll; RM.Fop.Infraestrutura.Repositorios.dll

### Rotina: RECALCULO

* **[Ticket: 25983098 / DRHCALCRM-11432]** Mensagem sobre a criação do periodo de retificação na rescisão só deve ser exibida se após o segundo cálculo houver valor a ser lançadao de restituição

Arquivo: RM.Fop.Calc.Calculos.dll

## 12.1.2602.123

### Rotina: GESTOR SOLICITAR AS FÉRIAS DO COLABORADOR

* **[Ticket: 26288565 / DRHMEURH-20838]** Ajuste no processo de solicitação de férias do Meu RH, para considerar corretamente o grupo de quiosque dos colaboradores, quando o acesso é realizado pelo gestor.

Arquivo: RM.Fop.Rest.Server.dll

## 12.1.2602.124

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26053647 / DRHMEURH-20568]** Ajuste no retorno do salário Hora nas requisições de alteração de dados e Transferência com alteração de dados | Meu RH

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: BUSCAR COLABORADOR E ORGANOGRAMA

* **[Ticket: 25295447 / DRHMEURH-20192]** Ajuste no retorno da busca avançada de colaboradores no Meu RH, para permitir retornar corretamente as informações.

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: CAD. - CAD. CONTÁBEIS - AGRUPAMENTO DE CONTAS

* **[Ticket: 27009858 / DRHROTRM-18103]** fix(agrupamento contábil): processo cópia entre coligadas

Arquivo: RM.Fop.Cadastros.Data.dll

### Rotina: FOLHA MENSAL - LANÇ. EMPRÉSTIMO CRÉDITO DO TRABALHADOR

* **[Ticket: 26953369 / DRHROTRM-18115]** Ajuste no evento S-1010 para que os eventos de estorno de pensão (cc 199, 200, 201 e 327) sejam gerados com o codIncIRRF 51, 52 e 53

Arquivo: RM.Fop.Dominio.dll

### Rotina: MIDDLEWARE - RELATÓRIO CONFERÊNCIA FGTS

* **[Ticket: 25875625 / DRHROTRM-16579]** Ajuste no relatório de conferência de INSS ao filtrar um CNO que não existe na distribuição do tomador

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: PORTAL WEB - SUGESTÃO DE FÉRIAS (LAB.01.215)

* **[Ticket: 26497449 / DRHCALCRM-11615]** Correção na descrição do relatório com integração TAE

Arquivos: RM.Fop.TotvsSign.Intf.dll; RM.Fop.TotvsSign.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27028479 / DRHROTRM-18114]** Na geração do relatório de conferência S5002 contendo autônomos fluxus e vários CODCOLCFO para um mesmo CODCOLIGADA: \* Gera relatório corretamente.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 26845415 / DRHROTRM-18044]** Na exportação do relatório de conferência S5002, funcionários em vários códigos de receita: \* Não duplica informações do plano de saúde e reembolsos.

Arquivo: RM.Fop.Api.dll

### Rotina: SOFTWARE HOUSE

* **[Ticket: 10894606 / DRHCALCRM-112]** Tratamento para permitir gerar retificação de folha para funcionário demitido

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.CalcularFolha.Form.dll

## 12.1.2602.125

### Rotina: CÁLCULO

* **[Ticket: 26612346 / DRHCALCRM-11819]** Ajuste no cálculo de férias para permitir a execução correta mesmo quando houver empréstimo com competência atual zerada.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: CHEFES E SUP. - CHEFES E SUPERVISORES

* **[Ticket: 26938219 / DRHROTRM-18211]** No cadastro de chefe / supervisor: \* Permite cadastro corretamente

Arquivos: RM.Fop.Lib.Intf.dll; RM.Fop.Lib.Server.dll

### Rotina: CONFIGURAÇÃO

* **[Ticket: DRHMEURH-20787]** Inclusão de melhorias relacionadas a segurança.

Arquivos: FrameHTML/RM.Fop.Lib.WebAPI.dll; FrameHTML/RM.Fop.WebAPI.dll

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 27084821 / DRHROTRM-18171]** Ajuste no informe de rendimentos no limite de obrigatoriedade do recebimento de rendimentos tributáveis

Arquivos: RM.Fop.Relatorios.Intf.dll; RM.Fop.Relatorios.Data.dll

### Rotina: FGTS - ARQUIVO FGTS DIGITAL

* **[Ticket: 26213146 / DRHROTRM-18037]** Ajuste na geração do lançamento financeiro do FGTS digital agrupado por lotação tributária para considerar o período informado na tela

Arquivos: RM.Fop.Utils.Server.dll; RM.Fop.Dominio.dll; RM.Fop.Utils.Intf.dll

### Rotina: IMPORTAÇÃO - IMPORTAÇÃO DO EMPRÉSTIMO CONSIGNADO - CRÉDITO DO TRABALHADOR SOCIAL

* **[Ticket: DRHCALCRM-11796]** Ajuste no código fonte do Folha de Pagamento

Arquivo: RM.Fop.Lib.Server.dll

### Rotina: INTEGRAÇÕES - CONCEITO E WEBSERVICE

* **[Ticket: 26571400 / DRHROTRM-17919]** Inclusão do campo UFCNH na tabela PFUNC, para atender a limitação do rmsrestdataserver (FopFuncData)

Arquivo: RM.Fop.Funcionario.Intf.dll

### Rotina: NOVA SOLICITAÇÃO

* **[Ticket: DRHCONS-8868]** Disponibilizar UserAgent no envio da Simulação Totvs Consignado.

Arquivo: RM.Fop.Rest.Intf.dll

### Rotina: PORTAL WEB - SUGESTÃO DE FÉRIAS (LAB.01.215)

* **[Ticket: 26497449 / DRHCALCRM-11615]** Portal RH - Data 'Limite para ínicio de Gozo' incorreta quando o colaborador possui um período de férias cadastrado

Arquivos: RM.Fop.FuFerias.Data.dll; RM.Fop.FuFerias.Intf.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26714465 / DRHROTRM-18040]** Na geração do relatório de conferência S5002 quando filtra somente divergências:\* Exibe somente os funcionários com divergências.

Arquivos: RM.Fop.Esocial.Intf.dll; RM.Fop.Esocial.Data.dll

## 12.1.2602.126

### Rotina: PARAMETRIZADOR - ESOCIAL

* **[Ticket: 23184373 / DRHCALCRM-8456]** Criação do parâmetro 'Arredonda INSS teto quando funcionário possui outro vínculo de terceiro'

Arquivos: RM.Fop.Calc.CalculosBase.dll; RM.Fop.Rotinas.Data.dll; RM.Fop.Parametros.Intf.dll; RM.Fop.Calc.Calculos.dll; RM.Fop.Parametros.Form.dll

## 12.1.2602.127

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 27082708 / DRHROTRM-18255]** Ajuste na geração do informe de rendimentos em ambiente cloud

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: LANÇAMENTOS - GRUPO DE EVENTOS

* **[Ticket: 26656852 / DRHCALCRM-11668]** No cálculo do salário maternidade em fevereiro, quando marcado o parametro Calcula conforme Sefip, a divisão deve ser feita pelo numero de dias do mês.

Arquivos: RM.Fop.Rotinas.Data.dll; RM.Fop.Calc.CalculosBase.dll; RM.Fop.Parametros.Form.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27139973 / DRHROTRM-18184]** Na geração do relatório de conferência S5002, ao obter conjunto de funcionários para processamento: \* Normaliza paginação provomento consistência entre gerações.

Arquivos: RM.Fop.Lib.Extensions.dll; RM.Fop.Esocial.Data.dll

### Rotina: VISUALIZAR AFASTAMENTOS

* **[Ticket: DRHMEURH-21101]** Bloquear reenvio de atestado Colaborador e Gestor

Arquivos: RM.Fop.Rest.Intf.dll; RM.Fop.Rest.Server.dll

* **[Ticket: DRHMEURH-21101]** Bloquear reenvio de atestado médico pelo Colaborador e Gestor

Arquivos: RM.Fop.Rest.Intf.dll; RM.Fop.Menu.dll; RM.Fop.Rest.Server.dll

## 12.1.2602.128

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27173577 / DRHROTRM-18241]** Na geração do relatório de conferência S5002 para Autonomo: \* Obtém último evento S1210 enviado com sucesso.

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 27079874 / DRHROTRM-18271]** Ajuste no evento S-1210 quando o funcionário possui evento de pensão e evento de IRRF mas não possui dedução de dependente

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.129

### Rotina: LANÇAMENTOS - DIFERENÇA SALARIAL

* **[Ticket: 27053803 / DRHCALCRM-11884]** Quando o aumento salarial é posterior ao mês da rescisão, o FGTS 13o indenizado deve ser proporcional aos dias da projeção do aviso prévio, após a data do aumento.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: MINHA EQUIPE

* **[Ticket: 27014445 / DRHHCM-17209]** Gestor logado sem permissão para Exportar Excel

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: NOVA SOLICITAÇÃO

* **[Ticket: DRHCONS-8983]** [EFIGESTAO-961] Atualizar Logo do parceiro - Casca RM

Arquivos: FrameHTML/RM.Fop.WebAPI.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 26665264 / DRHROTRM-18107]** Ajuste no evento S-1210 quando o funcionário possui evento de pensão e evento de IRRF mas não possui dedução de dependente

Arquivo: RM.Fop.Relatorios.Data.dll

## 12.1.2602.130

### Rotina: S-1200 - REMUNERAÇÃO TRABALHADOR - RGPS

* **[Ticket: 26867449 / DRHROTRM-18011]** Ajuste no evento S-1210 quando o funcionário possui evento de pensão e evento de IRRF mas não possui dedução de dependente

Arquivo: RM.Fop.Dominio.dll

### Rotina: SEGURANÇA

* **[Ticket: DRHMEURH-21471]** Melhorias de segurança | Meu RH

Arquivos: FrameHTML/RM.Fop.WebAPI.dll

## 12.1.2602.131

### Rotina: INTEGRAÇÃO

* **[Ticket: DRHSSTPT-1922]** Ajuste no processo de Transferência com alteração de chapa do funcionário demitido para geração de mensagem de integração com o Quírons

Arquivos: RM.Fop.Facade.dll; RM.Fop.Calc.Calculos.dll; RM.Rhu.Integracao.Services.dll; RM.Rhu.Integracao.Server.dll

### Rotina: PERÍODO DE APURAÇÃO

* **[Ticket: 26147138 / DRHROTRM-16532]** Ajusta mapeamento de propriedades e ordenação de campos de remuneração

Arquivo: RM.Fop.Api.dll

## 12.1.2602.132

### Rotina: AUTOMAÇÃO

* **[Ticket: DAUDITPROJ-574]** Exibição do menu da análise de anomalia da folha de pagamento

Arquivo: RM.Fop.Menu.dll

### Rotina: PORTAL - ESPELHO DO CARTÃO

* **[Ticket: 27294966 / DRHHCM-17294]** Tratamento query banco oracle

Arquivo: RM.Fop.Funcionario.Server.dll

## 12.1.2602.133

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: DRHMEURH-21263]** Ajuste na visualização e edição das requisições de transferência para correto funcionamento em matrículas com caracteres especiais

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: 26523044 / DRHROTRM-17926]** Ao realizar uma alteração de situação do funcionário, com integração Ahgora ativa e funcionário integrado na Ahgora:\* Registra afastamento para posterior envio para Ahgora

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: GERAÇÃO DOS LANÇAMENTOS

* **[Ticket: DRHCALCRM-12005]** Ajuste na geração do lançamento financeiro, permitindo sua inclusão, tratando o placeholder [FUN] no complemento do histórico com a substituição pelo nome do funcionário.

Arquivos: RM.Fop.Rotinas.Intf.dll; RM.Fop.Rotinas.Server.dll; RM.Fop.Dominio.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27197042 / DRHROTRM-18393]** Na geração do relatório de conferência S5002 com pensão de férias 13º, cujo código de cálculo e código da verba do registro do recibo de férias é diferente da ficha financeira: \* Preenche corretamente pensão 13º

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: RESILIÇÃO AUTOMÁTICA

* **[Ticket: DRHCALCRM-11988]** Permite cancelar a resilição quando não existe histórico salarial do processo de cálculo

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.Calc.CalculosBase.dll

### Rotina: SEÇÕES

* **[Ticket: 24215136 / DRHROTRM-14494]** feat: adequar validação de CNPJ para formato alfanumérico

Arquivos: RM.Fop.Utils.Server.dll; RM.Fop.Relatorios.Form.dll; RM.Fop.Processos.Form.dll; RM.Fop.Secao.Form.dll; RM.Fop.Utils.Intf.dll; RM.Fop.Esocial.Data.dll; RM.Fop.Api.dll; RM.Fop.Funcionario.Form.dll; RM.Fop.ATS.Service.dll; RM.Fop.Cadastros.Form.dll; RM.Fop.Informe.Data.dll; RM.Fop.Sindicato.Form.dll; RM.Fop.Calc.Calculos.dll; RM.Fop.Dominio.dll; RM.Fop.Const.Intf.dll; RM.Fop.Calc.CalculosBase.dll; RM.Fop.Sefip.Form.dll; RM.Fop.Secao.Data.dll; RM.Fop.Common.Data.dll; RM.Fop.Funcionario.Server.dll; RM.Fop.Relatorios.Data.dll; RM.Fop.Sefip.Data.dll; RM.Fop.CalcularFolha.Data.dll; RM.Fop.Manad.Form.dll; RM.Fop.Secao.Services.dll

* **[Ticket: 24215136 / DRHROTRM-14494]** feat(cadastro funcionário): adequar validação de CNPJ para formato alfanumérico

Arquivos: RM.Fop.Funcionario.Intf.dll; RM.Fop.Utils.Intf.dll

* **[Ticket: 24215136 / DRHROTRM-14494]** feat(CampoTipo.AlfaNumerico): adequar validação de CNPJ para formato alfanumérico

Arquivo: RM.Fop.Dominio.dll

* **[Ticket: 24215136 / DRHROTRM-14494]** feat(Manad | FuncionarioMod): adequar validação de CNPJ para formato alfanumérico

Arquivos: RM.Fop.Manad.Intf.dll; RM.Fop.Funcionario.Server.dll; RM.Fop.Manad.Form.dll

* **[Ticket: 24215136 / DRHROTRM-14494]** feat(DelphiToDotNetMask): adequar validação de CNPJ para formato alfanumérico

Arquivos: RM.Fop.Funcionario.Form.dll; RM.Fop.Sefip.Form.dll; RM.Fop.Cadastros.Form.dll; RM.Fop.Secao.Form.dll; RM.Fop.Relatorios.Form.dll; RM.Fop.Esocial.Form.dll

## 12.1.2602.134

### Rotina: CONFIGURAÇÃO

* **[Ticket: DRHMEURH-21688]** Implementações de melhoria no Meu RH.

Arquivo: RM.Fop.Rest.Server.dll

## 12.1.2602.135

### Rotina: MARCAÇÃO

* **[Ticket: DRHCALCRM-12016]** Edição do cadastros de férias já calculadas

Arquivos: RM.Fop.FuFerias.Data.dll; RM.Fop.FuFerias.Form.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 27310916 / DRHROTRM-18450]** Ajuste no evento S-1210 para funcionários com IRRF de PLR mas sem valor de pensão no dependente

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.136

### Rotina: FUNCIONÁRIOS - CADASTRO EMPRÉSTIMO CRÉDITO DO TRABALHADOR

* **[Ticket: DRHCALCRM-12093]** Implementada adequação para suporte ao CNPJ alfanumérico, permitindo caracteres alfanuméricos nas 12 primeiras posições e mantendo obrigatoriedade de dígitos numéricos nos dois últimos caracteres (DV), no processo de importação de empréstimos do crédito trabalhador.

Arquivos: RM.Fop.Processos.Form.dll; RM.Fop.CalcularFolha.Intf.dll; RM.Fop.CalcularFolha.Data.dll

### Rotina: MINHA EQUIPE

* **[Ticket: 26175700 / DRHHCM-17068]** Meu RH - Gestor - Visualização de subordinados indiretos

Arquivo: RM.Fop.Lib.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27012071 / DRHROTRM-18104]** Na geração do relatório S5002 com diferência de dissídio:\* Visualiza corretamente a comparação.

Arquivos: RM.Fop.Esocial.Intf.dll; RM.Fop.Lib.Extensions.dll; RM.Fop.Esocial.Data.dll

* **[Ticket: 26993217 / DRHROTRM-18111]** Na geração do relatório S5002 com diferência de dissídio:\* Visualiza corretamente a comparação.

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 27401655 / DRHROTRM-18488]** Na geração do relatório de conferência S5002:\* Obtém corretamente as verbas.

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: S-2500 - PROCESSO TRABALHISTA

* **[Ticket: DRHROTRM-17942]** Nota Técnica 06/2026: Adequação do XML do evento S-2500

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.137

### Rotina: MEU RH - DEMONSTRATIVO DE PAGAMENTO

* **[Ticket: 26465324 / DRHCALCRM-11667]** Correção na busca do Quiosque do Gestor ao visualizar o envelope de pagamento do subordinado

Arquivo: RM.Fop.Envelope.Data.dll

### Rotina: MINHAS SOLICITAÇÕES

* **[Ticket: DRHCONS-8778]** Adequação privacidade TOTVS - OPTIN/Versionamento

Arquivos: FrameHTML/RM.Fop.WebAPI.dll

### Rotina: PORTAL WEB - SUBORDINADOS (LAB.01.213)

* **[Ticket: 27358144 / DRHHCM-17307]** Refatoracao logica de consulta subordinados chefe/supervisor

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27117692 / DRHROTRM-18170]** Na geração do relatório de conferência S5002 cujo funcionário foi transferido no mesmo período da geração do relatório e contenha mais de uma chapa associada a mesma pessoa e todas as chapas estão demitidas:\* Exibe totalizadores corretamente sem duplicações.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.138

### Rotina: CÁLCULO

* **[Ticket: DRHCALCRM-12078]** Provisão de férias no mês onde houve antecipação de dias do próximo periodo aquisitivo estava considerando ferias antecipadas da competência seguinte.

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: GERAÇÃO DOS ENCARGOS

* **[Ticket: DRHCALCRM-12112]** Na geração do encargo de provisão de férias quando usa o parâmetro "Inibe reversão de valores na provisão mensal de férias" e não existe a linha do mês anterior, estava sendo considerada a provisao mensal.

Arquivos: RM.Fop.Dominio.dll; RM.Fop.FuFerias.Data.dll

### Rotina: PARAMETRIZADOR - CONFIGURAÇÕES GERAIS

* **[Ticket: 26982335 / DRHROTRM-18105]** Ajuste para possibilitar filtrar a fila de eventos do eSocial por filial.

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Intf.dll

### Rotina: PORTAL WEB - SUBORDINADOS (LAB.01.213)

* **[Ticket: 27363746 / DRHHCM-17310]** Usuário não tem permissão para visualizar os dados do funcionário na coligada

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 26721208 / DRHROTRM-18235]** Na geração do relatório de conferência S5002 cujo funcionário foi transferido no mesmo período da geração do relatório e contenha mais de uma chapa associada a mesma pessoa e todas as chapas estão demitidas:\* Exibe totalizadores corretamente sem duplicações.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.140

### Rotina: MINHA EQUIPE

* **[Ticket: 27585056 / DRHHCM-17371]** Chefe/supervisor - Ao marcar a opção para ver colaboradores indiretos está apresentando todos os colaboradores da coligada

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 26637058 / DRHROTRM-18252]** Ajuste ao buscar a filial do TAF para verificar o histórico de situação nos eventos periódicos retroativos

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.141

### Rotina: Sem Rotina Específica

* **[Ticket: DRHROTRM-18574]** Integração RM x Ahgora: Envio de Alteração de Chefia da Hierarquia por Posição

Arquivos: RM.Fop.Parametros.Form.dll; RM.Fop.Informe.Data.dll

### Rotina: ANEXOS - HISTÓRICOS

* **[Ticket: 26043509 / DRHCONS-9060]** Ajuste no configurador do anexo exibido na tela inicial de funcionários.

Arquivos: RM.Fop.Menu.dll; RM.Fop.Funcionario.Form.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: DRHROTRM-18574]** Integração RM x Ahgora: Envio de Alteração de Chefia da Hierarquia por Posição

Arquivos: RM.Fop.Funcionario.Server.dll; RM.Rhu.NovaHierarquia.Service.dll; RM.Fop.Facade.dll; RM.Fop.Funcionario.Intf.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 27239128 / DRHROTRM-18527]** Ajuste na geração do evento S-1200 quando funcionário está alocado no tomador empresa com antecipação de férias e existe autônomos do TOTVS Gestão Financeira

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.143

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27636642 / DRHROTRM-18599]** Na geração do relatório de conferência S5002 em bases oracle: \* Realiza corretamente as consultas SQL da ficha financeira e recibo de férias.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.144

### Rotina: CAD. - CAD. CONTÁBEIS - AGRUPAMENTO DE CONTAS

* **[Ticket: 27604046 / DRHROTRM-18538]** fix12602(agrupamento contábil): processo cópia entre coligadas

Arquivo: RM.Fop.Cadastros.Data.dll

* **[Ticket: 27604046 / DRHROTRM-18538]** fix22602(agrupamento contábil): processo cópia entre coligadas

Arquivo: RM.Fop.Cadastros.Data.dll

### Rotina: PERFIL DO COLABORADOR

* **[Ticket: DRHMEURH-21269]** Ajuste na visualização de dados de perfil para o correto funcionamento com diversas matrículas.

Arquivos: FrameHTML/RM.Fop.WebAPI.dll; FrameHTML/RM.Fop.Lib.WebAPI.dll

### Rotina: S-1200 - REMUNERAÇÃO TRABALHADOR - RGPS

* **[Ticket: 27244769 / DRHROTRM-18452]** Ajuste na antecipação de férias para considerar a data de pagamento das férias para funcionários transferidos

Arquivo: RM.Fop.Dominio.dll

### Rotina: S-2299 - DESLIGAMENTO

* **[Ticket: 27385066 / DRHROTRM-18623]** Ajuste no evento S-2299 ao preencher o grupo observacoes com as informações do exame toxicológico

Arquivo: RM.Fop.Utils.Server.dll

## 12.1.2602.145

### Rotina: LANÇAMENTOS - GRUPO DE EVENTOS

* **[Ticket: 26784368 / DRHCALCRM-11829]** Quando o desconto do IRRF fica abaixo do mínimo, os valores correspondentes não devem compor a formula de cálculo da pensão alimentícia

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: PER. APUR. - REMUNERAÇÃO TRAB. AVULSOS NÃO PORTUÁRIOS

* **[Ticket: DRHROTRM-18703]** Atualização interna de páginas smartui

Arquivos: RM.Fop.Esocial.Form.dll; RM.Fop.Funcionario.Form.dll

### Rotina: PORTAL - ESPELHO DO CARTÃO

* **[Ticket: 27338547 / DRHHCM-17356]** Ajuste para melhorar performance para carregar espelho de ponto subordinados.

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RECIBO DE PAGAMENTO DE FÉRIAS

* **[Ticket: 26778239 / DRHCALCRM-11824]** Ajuste das tag de segurança no relatório de Recibo de Férias

Arquivo: RM.Fop.NativeProvider.Service.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27081783 / DRHROTRM-18478]** Ajuste no relatório de IRRF S-5002 quando o prefixo do periodo possui letras

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 27673625 / DRHROTRM-18570]** Ajuste no relatório de IRRF S-5002 quando existe o mesmo evento de dissidio em duas chapas diferentes

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 27864471 / DRHROTRM-18604]** fix: trata DTFINAL nula na PFDADOSRESIDEXTERIOR para correta identificação de expatriado

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: TOTVS ASSINATURA ELETRÔNICA

* **[Ticket: 25324874 / DRHCALCRM-10361]** Mudança no caminho das WebActions - Cálculo

Arquivos: RM.Fop.Funcionario.Form.dll; RM.Fop.Cadastros.Form.dll; RM.Fop.CalcularFolha.Form.dll

## 12.1.2602.148

### Rotina: AUTOMAÇÃO

* **[Ticket: DAUDITPROJ-669]** Garantir que o consumidor de mensagens suporte o processamento de valores decimais para os campos de período (periodYear e periodMonth), evitando exceções de tipagem e assegurando que os dados de competência sejam gravados de forma íntegra para o correto funcionamento das lógicas de apuração.

Arquivos: RM.Fop.Auditoria.IService.dll; RM.Fop.Auditoria.SmartLink.Service.dll; RM.Fop.Auditoria.Service.dll; RM.Fop.Auditoria.Server.dll

### Rotina: CÁLCULO IRRF FOLHA

* **[Ticket: DRHCALCRM-12018]** Histórico de deduções por dependente de IRRF deverá ser preenchido sempre que aplicável e não somente quando houver o desconto de IRRF

Arquivo: RM.Fop.Calc.Calculos.dll

## 12.1.2602.149

### Rotina: Sem Rotina Específica

* Nova release App Ahgora

Arquivo: Rh/ahgora

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: 27282493 / DRHROTRM-18367]** Integração RM x AHGORA: Não gera gatilho de alteração de seção via requisições de transferência

Arquivo: RM.Fop.Funcionario.Server.dll

* **[Ticket: 27710886 / DRHROTRM-18576]** Integração RM x AHGORA: alteração do Processo "Trocar Data de Admissão" para gera gatilho

Arquivo: RM.Fop.Funcionario.Server.dll

* **[Ticket: 27710886 / DRHROTRM-18576]** Integração RM x AHGORA: Processo "Trocar Data de Admissão" não gera gatilho

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RECIBO DE PAGAMENTO DE FÉRIAS

* **[Ticket: 26778239 / DRHCALCRM-11824]** Ajuste das tag de segurança no relatório de Recibo de Férias

Arquivo: RM.Fop.FuFerias.Data.dll

## 12.1.2602.150

### Rotina: Sem Rotina Específica

* Nova release App Ahgora

Arquivo: Rh/ahgora

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 27635908 / DRHMEURH-21793]** Ajuste processo de avanço de etapa da requisição de requisições de transferência do Meu RH para considerar corretamente as validações de quadro de lotação.

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27985807 / DRHROTRM-18660]** Ajuste no relatório de IRRF S-5002 para buscar os valores de RRA da ficha financeira

Arquivos: RM.Fop.Esocial.Intf.dll; RM.Fop.Esocial.Data.dll

## 12.1.2602.151

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 27523292 / DRHROTRM-18712]** Ajuste no informe de rendimentos para considerar o evento com código de cálculo 180 (Diferença de 13º Salário por Dissídio)

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 27923493 / DRHROTRM-18748]** Ajuste no informe de rendimentos para não abater valor negativo da base de IRRF de um mês no outro

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: PRÉ-ATESTADO

* **[Ticket: 27960145 / DRHMEURH-21970]** Ajuste na exibição dos status de atestado no Meu RH.

Arquivo: RM.Fop.Rest.Server.dll

## 12.1.2602.152

### Rotina: CÁLCULO IRRF FOLHA

* **[Ticket: DRHCALCRM-12156]** Criação de processo no cadastro de funcionário para atualização retroativa das deduções por dependente

Arquivos: RM.Fop.Funcionario.Form.dll; RM.Fop.Funcionario.Data.dll; RM.Fop.Funcionario.Intf.dll

### Rotina: COMPLEMENTAR

* **[Ticket: 28236625 / DRHCALCRM-12253]** No cálculo de RRA na rescisão complementar está duplicando a base de FGTS no evento de CC 133

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: PRÉ-ATESTADO

* **[Ticket: 27315241 / DRHHCM-17469]** Lentidão rotinas de subordinados

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 27085927 / DRHROTRM-18315]** Ajuste no evento S-1210 para buscar a dedução de dependente sempre que existir no cadastro de dedução do dependente

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.153

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 27407929 / DRHROTRM-18661]** Na geração do informe de rendimentos com vários RRA de pensão para um mesmo funcionário e período pagamento: \* Exibe corretamente o campo 3 linha 4 \* Exibe corretamente o campo 7 Beneficiários de pensão alimentícia Vr Folha.

Arquivo: RM.Fop.Relatorios.Data.dll

* **[Ticket: 27898293 / DRHROTRM-18802]** Na geração do informe de rendimentos com RRA 13º diferença:Não contabiliza CC 395 como elegível para comport o campo 5 linha 1

Arquivo: RM.Fop.Relatorios.Data.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: DRHROTRM-18732]** Na integração com Ahgora: Envia origem do sistema 'RM'.

Arquivo: RM.Fop.Integracao.Services.dll

### Rotina: INTEGRAÇÕES - CONCEITO E WEBSERVICE

* **[Ticket: 27321457 / DRHROTRM-18473]** Ajuste controllers - Migração de WebAPI de Owin para Kestrel

Arquivo: RM.Fop.Funcionario.Intf.dll

### Rotina: OUTROS PROC. - RETIFICAÇÃO INFO. COMPL. S-1210

* **[Ticket: 27386687 / DRHROTRM-18804]** Ajuste no evento S-1210 de retificação quando o funcionário possui plano de saúde na folha e evento de IRRF nas férias mas não possui dedução de dependente

Arquivo: RM.Fop.Dominio.dll

### Rotina: PARAMETRIZADOR - FOLHA DE PAGAMENTO

* **[Ticket: 26950962 / DRHCALCRM-12084]** TOTVS Folha de Pagamento | TAE | Inclusão de Chefes da Hierarquia no Docto

Arquivos: RM.Fop.TotvsSign.Form.dll; RM.Fop.TotvsSign.Intf.dll; RM.Fop.TotvsSign.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27225685 / DRHROTRM-18510]** Ajuste para obter o número do período desconsiderando o prefixo do período eSocial no relatório de conferência S-5002

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Relatorios.Data.dll; RM.Fop.Relatorios.Intf.dll

* **[Ticket: 27489363 / DRHROTRM-18528]** Ajuste no relatório S-5002 para eventos cadastrados com letra

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 28161748 / DRHROTRM-18747]** Corrigida a lógica de filtragem por Data de Pagamento. O ajuste impede o arredondamento indevido de milissegundos que causava a inclusão de lançamentos do mês seguinte no fechamento do mês anterior

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.154

### Rotina: PARAMETRIZADOR - FOLHA DE PAGAMENTO

* **[Ticket: 26950962 / DRHCALCRM-12084]** TOTVS Folha de Pagamento | TAE | Inclusão de Chefes da Hierarquia no Docto

Arquivo: RM.Fop.TotvsSign.Intf.dll

## 12.1.2602.155

### Rotina: RELAT. - RELATÓRIO CONFERÊNCIA INSS (TAF)

* **[Ticket: 27899512 / DRHROTRM-18629]** Ajuste no progresso de conclusão do Relatório de Conferência INSS

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: S-1210 - PAGTOS DE RENDIMENTOS TRABALHO

* **[Ticket: 28075353 / DRHROTRM-18827]** Ajuste no evento S-1210 quando existe evento de restituição de IRRF na ficha financeira do funcionário

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.156

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: 27282493 / DRHROTRM-18367]** Integração RM x AHGORA: Não gera gatilho de alteração de seção via requisições de transferência

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 27316821 / DRHROTRM-18468]** Na geração do relatório de conferência S5002 cujas verbas são Tipo de Pagamento 5: \* Atribui corretamente ao código de receita "353301"

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 27247923 / DRHROTRM-18829]** Na geração do relatório de conferência S5002 de autônomos com CODCOLCFO diferentes: \* Atribui corretamente os valores pagos.

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.157

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: DRHMEURH-21212]** Ajuste na validação de férias para permitir alteração da data fim e salvamento do registro durante inclusão de licença maternidade.

Arquivos: FrameHTML/RM.Fop.WebAPI.dll

### Rotina: CÁLCULO

* **[Ticket: 26685928 / DRHCALCRM-11880]** Tratamento no cálculo do Abono em Dobro para verificar o parâmetro de Antes/Durante/Depois do Parametrizador

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.Calc.CalculosBase.dll; RM.Fop.Calc.Integracao.dll; RM.Fop.Parametros.Form.dll

### Rotina: FINALIZA

* **[Ticket: 28296717 / DRHCALCRM-12296]** Ajuste na validação de férias para permitir alteração da data fim e salvamento do registro durante inclusão de licença maternidade.

Arquivo: RM.Fop.FuFerias.Data.dll

### Rotina: FOLHA MENSAL - LANÇ. EMPRÉSTIMO CRÉDITO DO TRABALHADOR

* **[Ticket: 27241685 / DRHCALCRM-12022]** O evento de CC 484 não estava sendo lançado quando o CC 481 estava no mesmo periodo do envelope

Arquivo: RM.Fop.Calc.CalculosBase.dll

### Rotina: PARAMETRIZADOR - FOLHA DE PAGAMENTO

* **[Ticket: 26950962 / DRHCALCRM-12084]** Correção na visualização de envelope zerado com parametrização "Visualização de eventos com valores zerados no envelope"

Arquivos: RM.Fop.Envelope.Data.dll; RM.Fop.Envelope.Form.dll

### Rotina: RECIBO DE PAGAMENTO DE FÉRIAS

* **[Ticket: 27421033 / DRHCALCRM-12106]** Alteração no recibo de férias smartview para gerar recibos de períodos fechados

Arquivos: RM.Fop.FuFerias.Data.dll; RM.Fop.NativeProvider.Service.dll

* **[Ticket: 26911507 / DRHCALCRM-11849]** Correção na visualização de envelope zerado com parametrização "Visualização de eventos com valores zerados no envelope"

Arquivos: RM.Fop.Envelope.Form.dll; RM.Fop.Envelope.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 28464283 / DRHCALCRM-12315]** Remoção de ícone sem funcionalidade na parte de Funcionário do Menu - Folha de Pagamento

Arquivo: RM.Fop.Menu.dll

* **[Ticket: 27118272 / DRHROTRM-18677]** Na geração do relatório de conferência CNPJ preenchido na coluna CGCCFO, tabela FCFO: \* Gera autônomos.

Arquivos: RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Intf.dll

* **[Ticket: 28060346 / DRHROTRM-18871]** Ajuste no relatório de IRRF S-5002 para funcionários com data de pagamento das férias no primeiro dia subsequente à competência gerada

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 28061104 / DRHROTRM-18872]** Ajuste no relatório de IRRF S-5002 para funcionários com férias finalizadas no próximo mês

Arquivo: RM.Fop.Esocial.Data.dll

* **[Ticket: 27600560 / DRHROTRM-18963]** Ajuste no relatório de IRRF S-5002 para funcionários com IRRF de PLR nas verbas de diferença

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.158

### Rotina: MARCAÇÃO

* **[Ticket: 27018954 / DRHCALCRM-11894]** Ajuste no cadastro de férias, possibilitando cadastrar 3 períodos de férias partidas.

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.Calc.CalculosBase.dll

## 12.1.2602.159

### Rotina: MARCAÇÃO

* **[Ticket: 27018954 / DRHCALCRM-11894]** Rollback férias partidas, devido calculos do sistema.

Arquivos: RM.Fop.Calc.CalculosBase.dll; RM.Fop.Calc.Calculos.dll

### Rotina: PORTAL WEB - SUBORDINADOS (LAB.01.213)

* **[Ticket: 28511342 / DRHHCM-17580]** Portal RH - Supervisor visualiza todos os funcionários da seção, mesmo sendo de outra(s) equipe(s)

Arquivo: RM.Fop.Funcionario.Server.dll

## 12.1.2602.162

### Rotina: PARÂMETROS LOCAIS

* **[Ticket: 27025057 / DRHCALCRM-11996]** Ajuste ao carregar parâmetros locais no campo "Dia de Pagamento". Não estava sendo carregado o valor salvo ao abrir novamente o parâmetro locais.

Arquivo: RM.Fop.Parametros.Form.dll

## 12.1.2602.163

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: DRHROTRM-18696]** Integração RM X AHGORA: Não gera gatilho em "Substituição de Chefe e Supervisor"

Arquivos: RM.Fop.Funcionario.Intf.dll; RM.Fop.ChefeSupervisor.Intf.dll; RM.Fop.ChefeSupervisor.Data.dll; RM.Fop.Funcionario.Server.dll; RM.Fop.Substituto.Data.dll; RM.Fop.Rest.Server.dll; RM.Fop.Integracao.Data.dll; RM.Fop.Api.dll; RM.Fop.Lib.Intf.dll

* **[Ticket: DRHROTRM-18696]** Integração RM X AHGORA: realiza alteração de salario composto em anexos > folha de pagamento > salário composto ou realiza alteração de salário em alterações casdastrais > Alteração de Salários

Arquivos: RM.Fop.Lib.Server.dll; RM.Fop.Lib.Intf.dll; RM.Fop.Funcionario.Data.dll; RM.Fop.Rotinas.Data.dll; RM.Fop.Funcionario.Intf.dll; RM.Fop.Funcionario.Server.dll

### Rotina: LANÇAMENTOS - EXECUTA RECÁLCULO

* **[Ticket: 28465799 / DRHCALCRM-12312]** Evento de restituição de IRRF, CC 122, só deve ser permitido pelo lançamento manual

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.Calc.CalculosBase.dll

## 12.1.2602.165

### Rotina: S-2200 - ADMISSÃO TRABALHADOR

* **[Ticket: 27581258 / DRHROTRM-18975]** Ajuste no evento S-2200 ao preencher o grupo observacoes com as informações de curso

Arquivo: RM.Fop.Dominio.dll

## 12.1.2602.167

### Rotina: DIRF/INF.REND. - INF.RENDIMENTOS

* **[Ticket: 28482251 / DRHCALCRM-12323]** No processo para Atualizar as Deduções por Dependente, se o registro já existir na tabela, será mantido o original

Arquivo: RM.Fop.Funcionario.Data.dll

### Rotina: IMPORTAÇÃO - IMPORTAÇÃO DO EMPRÉSTIMO CONSIGNADO FEBRABAN

* **[Ticket: DRHCALCRM-8284]** Programa Crédito do Trabalhador - Importação de Layout (API)

Arquivo: RM.Fop.CalcularFolha.Form.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 28619552 / DRHROTRM-19011]** Ajuste no relatório S-5002 para funcionários com diferença de férias e com férias no mês

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: S-1010 - RUBRICAS

* **[Ticket: 26023454 / DRHROTRM-16904]** Ajuste no evento S-1200 para buscar os eventos de DE/PARA de férias do envelope do cadastro de eventos

Arquivos: RM.Fop.Infraestrutura.Repositorios.dll; RM.Fop.Evento.Data.dll; RM.Fop.Evento.Intf.dll; RM.Fop.Dominio.dll; RM.Fop.Rotinas.Data.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Ajuste no evento S-1200 para buscar os eventos de DE/PARA de antecipação de férias do cadastro de eventos

Arquivos: RM.Fop.Infraestrutura.Repositorios.dll; RM.Fop.Dominio.dll; RM.Fop.Utils.Intf.dll; RM.Fop.Evento.Intf.dll; RM.FopFolha.dll; RM.Fop.Relatorios.Server.dll; RM.Fop.Utils.Server.dll; RM.Fop.Esocial.Data.dll; RM.Fop.Esocial.Form.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Parametrizador: Descontinuação do de/para de eventos de férias eSocial

Arquivos: RM.Fop.Parametros.Form.dll; RM.Fop.Parametros.Intf.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Inclusão da aba eSocial no cadastro de eventos

Arquivos: RM.Fop.Evento.Form.dll; RM.Fop.Parametros.Intf.dll; RM.Fop.Evento.Data.dll; RM.Fop.Evento.Intf.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Inclusão do campo Forçar codIncCP eSocial no cadastro de eventos

Arquivos: RM.Fop.Evento.Form.dll; RM.Fop.Evento.Intf.dll

## 12.1.2602.168

### Rotina: CÁLCULO

* **[Ticket: DRHCALCRM-12399]** Criação da coluna CODEVENTODEPARARECIBO da tabela PFUFERIASVERBAS no recibo de férias.

Arquivos: RM.Fop.FuFerias.Data.dll; RM.Fop.FuFerias.Intf.dll

### Rotina: CARGOS/FUNÇÕES - CARGOS

* **[Ticket: 28055533 / DRHROTRM-18749]** Ajuste no cenário que salvava o usuário do banco de dados ao realizar a operação de cópia de função entre coligadas, para passar a salvar o usuário logado no sistema

Arquivo: RM.Fop.Processos.Data.dll

### Rotina: LANÇAMENTOS - EXECUTA RECÁLCULO

* **[Ticket: DRHCALCRM-12398]** Criação de campos para gravar informação dos eventos de De Para do eSocial no envelope de pagamento e no recibo de férias

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.Calc.CalculosBase.dll

### Rotina: S-1010 - RUBRICAS

* **[Ticket: 26023454 / DRHROTRM-16904]** Ajuste na validação de eventos com de/para para eventos com suspensão de incidência

Arquivos: RM.Fop.Esocial.Form.dll; RM.Fop.Evento.Data.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Fila de Eventos: Processo de alteração em lote da competência

Arquivos: RM.Fop.Esocial.Form.dll; RM.Fop.Esocial.Data.dll; RM.Fop.Menu.dll; RM.Fop.Esocial.Intf.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Inclusão do processo para converter os evento do de/para de férias do parametrizador

Arquivos: RM.Fop.Menu.dll; RM.Fop.Lib.Extensions.dll; RM.Fop.Esocial.Intf.dll; RM.Fop.Esocial.Data.dll; RM.Fop.Evento.Intf.dll; RM.Fop.Evento.Data.dll; RM.Fop.Esocial.Form.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Ajuste na geração dos eventos do eSocial para verificar o de/para de eventos a partir de 2026

Arquivos: RM.Fop.Relatorios.Data.dll; RM.Fop.Relatorios.Server.dll; RM.Fop.Esocial.Data.dll; RM.Fop.Dominio.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Cadastro de Eventos: Exportação e Importação tratando novos campos da aba eSocial

Arquivo: RM.Fop.Importacao.Data.dll

* **[Ticket: 26023454 / DRHROTRM-16904]** Parametrização ESocial Geral

Arquivo: RM.Fop.Parametros.Form.dll

## 12.1.2602.169

### Rotina: ANEXOS - HISTÓRICOS

* **[Ticket: DRHSSTPT-2205]** Ajuste na API sickNote a fim de aplicar ajustes de segurança de acesso.

Arquivos: RM.Fop.Funcionario.Intf.dll; RM.Fop.Api.dll; RM.Fop.Funcionario.Server.dll

### Rotina: AUDITORIA DE FOLHA (ANALISE DE CONFORMIDADE)

* **[Ticket: DAUDITPROJ-704]** Realizada a implementaçao no dashboard de auditoria de folha de pagamento, incluindo os recursos, visao de funcionarios e filtros

Arquivos: RM.Fop.Auditoria.SmartLink.Service.dll; RM.Fop.Auditoria.IService.dll; RM.Fop.Auditoria.Service.dll; RM.Fop.Auditoria.Server.dll; RM.Fop.Auditoria.Api.dll

### Rotina: CÁLCULO

* **[Ticket: DRHCALCRM-12399]** Criação da coluna na tela de envelope de pagamento e na ficha financeira.

Arquivos: RM.Fop.Funcionario.Intf.dll; RM.Fop.Envelope.Data.dll; RM.Fop.Envelope.Intf.dll; RM.Fop.Funcionario.Data.dll

### Rotina: LANÇAMENTOS - GRUPO DE EVENTOS

* **[Ticket: DRHROTRM-19124]** Ajuste na geração dos eventos do eSocial para verificar o de/para de eventos a partir de 2026

Arquivos: RM.Fop.Dominio.dll; RM.Fop.Parametros.Form.dll; RM.Fop.Evento.Data.dll; RM.Fop.Evento.Form.dll; RM.Fop.Utils.Intf.dll; RM.Fop.Importacao.Data.dll; RM.FopFolha.dll; RM.Fop.Utils.Server.dll; RM.Fop.Lib.Extensions.dll; RM.Fop.Esocial.Form.dll

## 12.1.2602.170

### Rotina: AUDITORIA DE FOLHA (ANALISE DE CONFORMIDADE)

* **[Ticket: DAUDITPROJ-785]** Realizada a implementaçao de exportaçao da filial no excel

Arquivos: RM.Fop.Auditoria.IService.dll; RM.Fop.Auditoria.Server.dll

### Rotina: CÁLCULO

* **[Ticket: DRHCALCRM-12424]** Ajuste para obter colunas CODEVENTODEPARAPROVENTO, CODEVENTODEPARADESCONTO da tabela PFFINANC via WebServices.

Arquivo: RM.Fop.Envelope.Data.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: DRHROTRM-19156]** Ao realizar a substituição de um chefe/supervisor via MDI e não informar data fim: \* Substituição ocorre corretamente.

Arquivo: RM.Fop.ChefeSupervisor.Data.dll

### Rotina: EVENTOS - EVENTOS

* **[Ticket: 26274251 / DRHROTRM-16824]** Inclusão do processo para converter os evento do de/para de férias do parametrizador

Arquivo: RM.Fop.Esocial.Data.dll

### Rotina: FÓRMULAS

* **[Ticket: DRHCALCRM-12360]** Melhoria na fórmula MVRUBRICA, retornando valores da competência anterior.

Arquivos: RM.Fop.Calc.Calculos.dll; RM.Fop.Calc.CalculosBase.dll; RM.Fop.Calc.Formulas.dll

### Rotina: MARCAÇÃO

* **[Ticket: 27018954 / DRHCALCRM-11894]** Implementada melhoria no cadastro de férias via RM (MDI), permitindo o cadastramento de férias partidas para solicitações em status de aprovação pelo gestor e/ou pelo DP.

Arquivos: RM.Fop.FuFerias.Intf.dll; RM.Fop.FuFerias.Data.dll

### Rotina: PORTAL WEB - SUBORDINADOS (LAB.01.213)

* **[Ticket: 28874108 / DRHHCM-17635]** Ajuste na visualização de subordinados de outras coligadas utilizando chefe/supervisor

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: SEGURANÇA - PERMISSÕES DE ACESSO

* **[Ticket: 28841622 / DRHROTRM-19094]** Acesso a Menus: Não esta exibindo os itens 01.01.01.23 até 01.01.01.85

Arquivo: RM.Fop.Menu.dll

## 12.1.2602.171

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 27673487 / DRHMEURH-22231]** Ajuste na exibição das filiais na requisição de aumento de quadro com hierarquia por posição.

Arquivo: RM.Fop.Rest.Server.dll

### Rotina: CHEFES E SUP. - CHEFES E SUPERVISORES

* **[Ticket: DRHHCM-17676]** Ajuste na permissão de visualização de subordinados de outras coligadas utilizando chefe/supervisor

Arquivo: RM.Fop.Funcionario.Server.dll

### Rotina: IMPORTAÇÃO - IMPORTAÇÃO DO EMPRÉSTIMO CONSIGNADO FEBRABAN

* **[Ticket: 28161952 / DRHCALCRM-12245]** Inserido ServiceContract na interface IFopParamData.

Arquivo: RM.Fop.Averbacao.Intf.dll

* **[Ticket: 28161952 / DRHCALCRM-12245]** Ajuste na importação Credito do trabalhador, para atualizar Últ. Competência importada.

Arquivos: RM.Fop.Averbacao.Data.dll; RM.Fop.Parametros.Form.dll; RM.Fop.Averbacao.Intf.dll

### Rotina: LANÇAMENTOS - EXECUTA RECÁLCULO

* **[Ticket: DRHCALCRM-12380]** Lançamento de empréstimo crédito do trabalhador pelo Gerenciador de Movimento deve ter as mesmas validações do grupo de eventos.

Arquivos: RM.Fop.Calc.CalculosBase.dll; RM.Fop.Calc.Calculos.dll

### Rotina: RELAT. - RELATÓRIO CONFERÊNCIA INSS PATRONAL

* **[Ticket: DRHROTRM-18559]** fix: caminho das rotas

Arquivos: RM.Fop.Integracao.Form.dll; RM.Fop.Esocial.Form.dll; RM.Fop.Lib.Server.dll

* **[Ticket: DRHROTRM-18559]** fix: ajuste rota FGTS Digital e retificação anterior 1210

Arquivo: RM.Fop.Esocial.Form.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 28937871 / DRHROTRM-19141]** Ajuste no relatório de conferência S-5002 para funcionários demitidos com diferença de férias pagas posterior a rescisão

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.172

### Rotina: CADASTRO

* **[Ticket: 28236123 / DRHROTRM-18982]** Ajuste para considerar corretamente a competência atual e competência futura no processo de liberação de competência

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: ENVIO DE DADOS PARA A AHGORA

* **[Ticket: DRHROTRM-19085]** Integração com Ahgora ativa e realização de substituição de chefe / supervisor via portal (antigo):\* Gera gatilho dos subordinados.

Arquivos: RM.Fop.Funcionario.Server.dll; RM.Fop.Lib.Intf.dll; RM.Fop.Lib.Server.dll; RM.Fop.Substituto.Data.dll

### Rotina: RELAT. - RELATÓRIO DADOS COMPLEMENTARES IRRF

* **[Ticket: 29056761 / DRHROTRM-19194]** Ajuste no relatório de conferência S-5002 no mapeamento do código de cálculo 464 (INSS de Diferença de 13º Salário RRA)

Arquivo: RM.Fop.Esocial.Data.dll

## 12.1.2602.173

### Rotina: AUDITORIA DE FOLHA (ANALISE DE CONFORMIDADE)

* **[Ticket: DAUDITPROJ-812]** Documentação das APIS

Arquivo: RM.Fop.Auditoria.Api.dll

### Rotina: EVENTOS PERIÓDICOS

* **[Ticket: 28107467 / DRHROTRM-19045]** Ajuste no evento S-1200 retroativo ao buscar as informaçõe de múltiplos vinculos

Arquivos: RM.Fop.Utils.Intf.dll; RM.Fop.Dominio.dll; RM.Fop.Utils.Server.dll

### Rotina: GERAÇÃO DOS ENCARGOS

* **[Ticket: 28110709 / DRHCALCRM-12230]** Na geração do encargo tipo R estava sendo duplicado o valor do código de cálculo 415 referente a base de férias

Arquivos: RM.Fop.Dominio.dll; RM.Fop.Calc.Calculos.dll

### Rotina: REGISTRO PRELIMINAR

* **[Ticket: DRHROTRM-19295]** Atualização interna para qualidade de software

Arquivo: Fop/fop-e2e

### Rotina: S-2206 - ALT. CONTRATO TRABALHO

* **[Ticket: 28103523 / DRHROTRM-18885]** Ajuste no evento S-2206 ao calcular o campo indRetif

Arquivo: RM.Fop.Common.Data.dll

## 12.1.2602.174

### Rotina: CADASTRO

* **[Ticket: 28236123 / DRHROTRM-18982]** Ajuste para considerar corretamente a competência atual e competência futura no processo de liberação de competência

Arquivo: RM.Fop.Rotinas.Data.dll

### Rotina: MIDDLEWARE - GERAL/ OUTROS

* **[Ticket: 29243912 / DRHROTRM-19301]** Liberação do conversor de eventos do parametrizador somente para clientes piloto

Arquivo: RM.Fop.Menu.dll

## 12.1.2602.175

### Rotina: COMPLEMENTAR

* **[Ticket: 28936250 / DRHCALCRM-12436]** Na retificação da rescisão o provento obrigatório pago na rescisão original está sendo consdirado duas vezes na insuficiência de saldo

Arquivo: RM.Fop.Calc.Calculos.dll

### Rotina: S-1010 - RUBRICAS

* **[Ticket: 26023454 / DRHROTRM-16904]** Liberação do processo para converter os evento do de/para de férias do parametrizador

Arquivos: RM.Fop.FuFerias.Data.dll; RM.Fop.Evento.Data.dll; RM.Fop.Evento.Form.dll; RM.Fop.Funcionario.Data.dll; RM.Fop.Envelope.Data.dll; RM.Fop.Parametros.Form.dll; RM.Fop.Dominio.dll; RM.Fop.Importacao.Data.dll; RM.FopFolha.dll; RM.Fop.Menu.dll; RM.Fop.Esocial.Form.dll

## 12.1.2602.176

### Rotina: FILA DE EVENTOS

* **[Ticket: DRHROTRM-18400]** Ajuste na validação de eventos com de/para para eventos com código de cálculo 420

Arquivos: RM.Fop.Evento.Data.dll; RM.Fop.Esocial.Form.dll

# TOTVS Framework

## 12.1.2602.100

### Rotina: CONTRATO DE VENDA

* **[Ticket: DFRWFOUNDATION-29232]** Ajuste para que seja possível mandar um saveRecord aplicar a segurança de campos na MDI.

Arquivos: RM.Lib.Server.dll; RM.Lib.dll

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-25622]** Alteração para melhoria da funcionalidade e evitar uso de forma indevida

Arquivo: RM.Host.ServiceManager.exe

## 12.1.2602.105

### Rotina: PROTOCOLO SAML (INT.09)

* **[Ticket: 26591804 / DFRWFOUNDATION-29435]** Inclusão do decode do body da requisição na resposta do SAML

Arquivo: RM.Lib.WinForms.dll

## 12.1.2602.106

### Rotina: GLOBAIS

* **[Ticket: 25054735 / DFRWFOUNDATION-27790]** Ajuste na MDI, ao bloquear por inatividade.

Arquivo: RM.Lib.WinForms.dll

## 12.1.2602.107

### Rotina: Sem Rotina Específica

* **[Ticket: 26497228 / DFRWFOUNDATION-29378]** Alteração para melhoria da funcionalidade de identificação da Base de Dados e do DataBaseId que deve manter a configuração do SmartLink após atualização de Patch

Arquivos: RM.Lib.WinForms.dll; RM.Con.SmartLink.Service.dll; RM.Con.SmartLink.Server.dll; RM.Lib.SmartLink.dll; RM.Lib.dll

### Rotina: LANÇAMENTO DE HORÁRIOS

* **[Ticket: 25585321 / DFRWFOUNDATION-29307]** Correção do parse de enum do tipo flag na execução de uma tarefa de leitura de parâmetros

Arquivos: RM.Lib.Workflow.Activities.dll; Frw/workflow-service-core

## 12.1.2602.108

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-89]** Deploy base temp, importação de arquivos fiscais e contábeis

Arquivos: RM.Glb.Processos.Server.dll; RM.Glb.Processos.Intf.dll; RM.Glb.Utils.Server.dll

## 12.1.2602.110

### Rotina: CONTROLADOR

* **[Ticket: DFRWFOUNDATION-29557]** Ajuste para que o JobServer distribua os job´s sem precisar passar por todos os job´s da fila

Arquivo: RM.Lib.Jobs.Server.dll

### Rotina: SAML

* **[Ticket: DFRWFOUNDATION-29536]** Inclusão de logs ao autenticar um usuário no sistema

Arquivos: RM.Lib.WinForms.dll; RM.Lib.Server.dll

## 12.1.2602.111

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4637]** Atualizando para a versão 19.24.0

Arquivo: Frw/smart-x-rm-ui

* **[Ticket: DFRWTOOLS-4637]** Melhorias na tela de diagnóstico da integração com o SmartLink

Arquivos: RM.Glb.SmartX.SmartLink.Diagnostics.dll; RM.Glb.SmartXClient.Cadastros.dll

### Rotina: TGM

* **[Ticket: DFRWTOOLS-4758]** Criação de WhiteList para execução da integração com SmartLink

Arquivo: RM.Lib.Server.dll

## 12.1.2602.119

### Rotina: CONTEXTO

* **[Ticket: 26040397 / DFRWFOUNDATION-29676]** Inclusão da validação do campo de imagem antes do cast e inclusão de log quando a imagem estiver nula

Arquivo: RM.Lib.dll

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-89]** Combo de seleção de coligadas origem

Arquivos: RM.Glb.Processos.Form.dll; RM.Glb.Processos.Server.dll; RM.Glb.Processos.Intf.dll

## 12.1.2602.120

### Rotina: PARAMETRIZADOR DE PRODUTO

* **[Ticket: DFRWFOUNDATION-29583]** Refatoração da mensagem de alerta quando um XML de parâmetro estiver incorreto

Arquivo: RM.Lib.Params.Server.dll

## 12.1.2602.123

### Rotina: GLOBAIS

* **[Ticket: DFRWTOOLS-4885]** Mensagem de informação do motivo da coleta de dados do perfil profissional.

Arquivo: RM.Glb.SmartX.Cadastros.dll

## 12.1.2602.125

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-89]** Alteração do parâmetro controle de transação para false. Assim no novo wizard será por registro.

Arquivo: RM.Glb.Processos.Server.dll

### Rotina: FERRAMENTAS DE ANÁLISE

* **[Ticket: DFRWBI-15577]** Integração do TOTVS Identity com o Smart View via RM

Arquivo: RM.Lib.Foundation.Api.dll

### Rotina: GLOBAIS

* **[Ticket: DFRWTOOLS-4915]** Desativação do Sync de perfil profissional

Arquivo: RM.exe

### Rotina: OAUTH

* **[Ticket: DFRWFOUNDATION-29246]** Serviços para login com OIDC.

Arquivos: RM.Lib.Communication.dll; RM.Lib.Foundation.Api.dll; RM.Lib.Data.dll; RM.Glb.Api.dll; RM.Lib.Server.dll; RM.Lib.dll; RM.Lib.Api.dll; RM.Lib.Utils.dll; RM.Lib.SmartLink.dll; RM.Lib.Api.Server.dll

* **[Ticket: DFRWFOUNDATION-29246]** Ajustes na tela de enviar url de redirecionamento.

Arquivos: RM.Lib.SmartX.Cadastros.dll; RM.Lib.Data.dll; RM.Lib.Client.dll

* **[Ticket: DFRWFOUNDATION-29246]** Adicionando projeto do SmartX

Arquivos: RM.Lib.SmartXClient.Cadastros.Action.dll; RM.Lib.SmartX.Cadastros.dll

* **[Ticket: DFRWFOUNDATION-29246]** Ajuste para que seja possível carregar a DLL RM.Lib.SmartX.Cadastros pois ela está sendo criada na Lib com as rotinas de OIDC

Arquivo: Frw/smart-x-rm

### Rotina: PROCESSO CUSTOMIZADO (BSO)

* **[Ticket: 27119854 / DFRWFOUNDATION-29840]** Remoção da validação da fonte de login Fluig

Arquivo: RM.Lib.Server.dll

### Rotina: USUÁRIOS

* **[Ticket: 26775100 / DFRWFOUNDATION-29599]** Alteração para melhoria na mensagem de retorno ao realizar tentativa de alteração de senha.

Arquivos: RM.Lib.WinForms.dll; RM.Lib.dll; RM.Lib.Server.dll

## 12.1.2602.126

### Rotina: OAUTH

* **[Ticket: DFRWFOUNDATION-29246]** Descendo alterações de redirecionamento de URLS do login OIDC

Arquivo: RM.Lib.Data.dll

### Rotina: USUÁRIOS

* **[Ticket: 26775100 / DFRWFOUNDATION-29599]** Removendo tracklog do Principal

Arquivo: RM.Lib.dll

* **[Ticket: 27117448 / DFRWFOUNDATION-29857]** Melhoria na autenticação do usuário

Arquivo: RM.Lib.Server.dll

## 12.1.2602.127

### Rotina: BASE ACELERADORA

* **[Ticket: RMARQIA-226]** Otimização do processo de cópia de dados fiscais para possibilitar o Cadastro de caminhos de arquivos fiscais e contábeis

Arquivos: RM.Glb.Cadastros.Form.dll; RM.Glb.Cadastros.Intf.dll; RM.Glb.Cadastros.Data.dll; RM.Glb.Menu.dll; RM.Glb.Processos.Server.dll

## 12.1.2602.129

### Rotina: MONITOR

* **[Ticket: DFRWFOUNDATION-29735]** Melhoria na validação de latência.

Arquivo: RM.Lib.dll

### Rotina: SEGURANÇA - PERFIS

* **[Ticket: 25984889 / DFRWFOUNDATION-29453]** Ajuste na rotina de exibição de perfis vinculados a um usuario

Arquivo: RM.Glb.Utils.Client.dll

## 12.1.2602.130

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-29643]** Melhoria no carregamento dos ícones de segmentos e de módulos do menu.

Arquivo: RM.exe

### Rotina: INSTALAÇÃO/ATUALIZAÇÃO

* **[Ticket: DFRWTOOLS-4949]** Melhoria na integração com o Credential Helper

Arquivo: RM.Lib.dll

## 12.1.2602.131

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-29699]** Aprimorado o tratamento de mensagens na atividade Filtrar DataSet da fórmula visual.

Arquivos: RM.Lib.Workflow.Activities.dll; Frw/workflow-service-core

### Rotina: TIPOS DE DADOS (MTD.00014)

* **[Ticket: 25124583 / DFRWFOUNDATION-27965]** 27965 - Metadados-Filtro na visão utilizando campo do tipo TIME (hora)

Arquivo: RM.Lib.dll

## 12.1.2602.132

### Rotina: CÓPIA DE DADOS

* **[Ticket: RMARQIA-328]** Novo wizard abrir a tela de customização de parâmetros

Arquivos: RM.Glb.Processos.Form.dll; RM.Glb.Processos.Intf.dll; RM.Glb.Processos.Server.dll

### Rotina: LOGIN RM.EXE

* **[Ticket: DFRWFOUNDATION-29885]** 27965 - Melhoria nas funcionalidades de alteração dos dados de segurança

Arquivos: RM.Glb.Seguranca.Server.dll; RM.Lib.Server.dll

## 12.1.2602.136

### Rotina: OAUTH

* **[Ticket: DFRWFOUNDATION-29645]** Descendo Processo de sincronismo de URLs

Arquivos: RM.Lib.Client.dll; RM.Lib.SmartXClient.Cadastros.Action.dll; RM.Lib.SmartX.Cadastros.dll; RM.Lib.Server.dll; RM.Lib.WinForms.dll

### Rotina: PARÂMETROS

* **[Ticket: 26145516 / DFRWFOUNDATION-29199]** Melhorada a performance na inicialização da action de perfil.

Arquivo: RM.Glb.Seguranca.Form.dll

## 12.1.2602.137

### Rotina: CONFIG GLOBAL

* **[Ticket: DFRWFOUNDATION-29855]** Habilitar OIDC parâmetros globais

Arquivos: RM.Glb.Cadastros.Server.dll; RM.Glb.Api.dll; RM.Glb.Cadastros.Intf.dll; RM.Lib.dll; RM.Glb.Cadastros.Form.dll; RM.Lib.Server.dll

* **[Ticket: DFRWFOUNDATION-29855]** Permissão supervisor para habilitar OIDC parâmetros globais

Arquivo: RM.Glb.Api.dll

### Rotina: GLOBAIS

* **[Ticket: 27297492 / DFRWFOUNDATION-29993]** Alteração da mensagem de duplicidade de chaves no XML de parâmetros

Arquivo: RM.Lib.Params.Server.dll

* **[Ticket: 27297492 / DFRWFOUNDATION-29993]** Alteração da forma como o XML de parâmetros customizados é carregado

Arquivo: RM.Lib.Params.Server.dll

## 12.1.2602.140

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-30107]** Atualização de Certificado de Assinatura

Arquivos: RM.Lib.dll; RM.exe

## 12.1.2602.141

### Rotina: PERFIS

* **[Ticket: 27583637 / DFRWFOUNDATION-30191]** Ajuste em acesso a aba Acesso a Menus

Arquivos: RM.Glb.Seguranca.Form.dll; RM.Lib.Server.dll

## 12.1.2602.143

### Rotina: LAYOUT

* **[Ticket: 27118546 / DFRWFOUNDATION-29831]** Ajustado o comportamento da pesquisa em visões com campos calculados, garantindo seu funcionamento adequado.

Arquivo: RM.Lib.WinForms.dll

## 12.1.2602.144

### Rotina: GRID

* **[Ticket: 26910755 / DFRWFOUNDATION-29713]** Ajustado o comportamento da aba Janelas Anexas para que seja exibida corretamente após realizar logoff e novo login no sistema.

Arquivo: RM.exe

## 12.1.2602.145

### Rotina: FORMULÁRIO: APRESENTAÇÃO (MTD.00002)

* **[Ticket: 26968425 / DFRWFOUNDATION-29711]** Ajustado o processo de validação na criação de formulários de metadados cuja estrutura do modelo de negócio utiliza DataServer.

Arquivo: RM.Glb.Metadata.Form.dll

## 12.1.2602.151

### Rotina: Sem Rotina Específica

* **[Ticket: 27898710 / DFRWFOUNDATION-30370]** Ajustes no carregamento dos artefatos SmartX.

Arquivo: Frw/smart-x-rm

## 12.1.2602.152

### Rotina: LOGIN RM.EXE

* **[Ticket: DFRWFOUNDATION-30439]** Removendo botão de suporte do Formulário de Login

Arquivo: RM.Lib.WinForms.dll

## 12.1.2602.153

### Rotina: LOGIN RM.EXE

* **[Ticket: 26429709 / DFRWFOUNDATION-29350]** Ajustado o comportamento da tela de desconexão do sistema para que as opções de login de aplicativos externos também sejam exibidas nesse contexto.

Arquivo: RM.Lib.WinForms.dll

## 12.1.2602.154

### Rotina: AUTO SCRIPT

* **[Ticket: 24544604 / DFRWFOUNDATION-29494]** Inclusão da validação do caracter especial utilizado pelo RM para não gerar logs ao buscar o nome das tabelas

Arquivo: RM.Lib.Server.dll

## 12.1.2602.155

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-30524]** Melhoria na tela de liberação de período

Arquivo: RM.Lib.WinForms.dll

## 12.1.2602.158

### Rotina: GLOBAIS

* **[Ticket: DFRWBI-15435]** Réplica Correção ao atualizar token

Arquivo: RM.Lib.WinForms.Chromium.dll

## 12.1.2602.162

### Rotina: IDENTITY RM: APICATIVOS RM (INT.11)

* **[Ticket: 28458856 / DFRWFOUNDATION-30535]** Ajuste para que seja possível ativar uma coligada quando a mesma estiver com o sincronismo incompleto no Identity

Arquivo: RM.Lib.Communication.Server.dll

## 12.1.2602.167

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWTOOLS-4994]** Réplica para versão de mercado de todas as Melhorias no DataSharing

Arquivo: RM.Lib.AITools.SmartLink.Service.dll

## 12.1.2602.170

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-30432]** Criação de um serviço que retorne o tenantId

Arquivos: RM.Lib.Server.dll; RM.Lib.SmartLink.dll; RM.Con.SmartLink.Server.dll

## 12.1.2602.171

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-29547]** Colocando Log de execução de action como habilitado por padrão no sistema.

Arquivo: RM.Lib.WinForms.dll

## 12.1.2602.172

### Rotina: ACESSO A MENUS

* **[Ticket: DFRWFOUNDATION-30747]** Definindo permissão ao item de Menu do Login OIDC

Arquivo: RM.Lib.Client.dll

## 12.1.2602.176

### Rotina: Sem Rotina Específica

* **[Ticket: DFRWFOUNDATION-30890]** Ajuste para que a flag OIDC\_ENABLED não seja setada no processamento da mensagem ErpUserEvent

Arquivo: RM.Lib.Server.dll

# TOTVS Gerador de Relatórios

## 12.1.2602.133

### Rotina: GERAÇÃO DE RELATÓRIO (RPT.00005)

* **[Ticket: 25873173 / DFRWBI-15385]** Bloqueio de campos acessíveis para edição de usuário com restrição no perfil

Arquivo: RM.Rpt.Reports.Form.dll

## 12.1.2602.145

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 25582450 / DFRWBI-15357]** Réplica Correção de memória Leak do RM ao exibir relatório no RM Reports.

Arquivos: RM.Rpt.Lib.Client.dll; RM.Rpt.Executor.Client.dll

# TOTVS Gerador de saídas

## 12.1.2602.125

### Rotina: GLOBAIS

* **[Ticket: DFRWFOUNDATION-29478]** EntryPoint no processo de geração de layout de saídas

Arquivos: RM.Gen.Engine.Server.dll; RM.Gen.Engine.Intf.dll

# TOTVS Gestão Bibliotecária

## 12.1.2602.124

### Rotina: Sem Rotina Específica

* **[Ticket: DEDUCAPCOM-10380]** Melhoria na portal de pesquisa publica

Arquivos: RM.Bib.API.dll; RM.Bib.Lib.Intf.dll

## 12.1.2602.129

### Rotina: RESERVAS

* **[Ticket: 26633343 / DEDUCAPCOM-10379]** Feito ajuste na consulta de empréstimo para considerar o usuário correto da biblioteca, com base no usuário logado.

Arquivo: RM.Bib.Processos.Data.dll

## 12.1.2602.159

### Rotina: RESERVAS

* **[Ticket: DEDUCAPCOM-10411]** Adequação de segurança na reserva de publicações.

Arquivos: RM.Bib.Rest.Server.dll; RM.Bib.API.dll; RM.Bib.Processos.Data.dll

### Rotina: TAXAS DA BIBLIOTECA

* **[Ticket: DEDUCAPCOM-10412]** Ajustes internos nas APIs da Biblioteca para tratamento de melhorias preventiva para a parte de segurança

Arquivos: FrameHTML/RM.Bib.WebAPI.dll

## 12.1.2602.161

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8556]** Otimização no processo de movimentações financeiras das disciplinas para a geração de lançamento

Arquivos: RM.Bib.dll; RM.Bib.Facade.Intf.dll; RM.Bib.Facade.dll

### Rotina: TAXAS DA BIBLIOTECA

* **[Ticket: DEDUCAPCOM-10412]** Ajustes internos nas APIs da Biblioteca para tratamento de melhorias preventiva para a parte de segurança

Arquivo: RM.Bib.Rest.Server.dll

## 12.1.2602.163

### Rotina: PESQUISA SIMPLES

* **[Ticket: 27887776 / DEDUCAPCOM-10633]** Ajustes na visibilidades dos campos na biblioteca

Arquivos: RM.Bib.Lib.Intf.dll; RM.Bib.API.dll

## 12.1.2602.171

### Rotina: VISUALIZACÃO DE BOLETOS

* **[Ticket: 27430783 / DEDUCAPCOM-10839]** Ajuste para o correto carregamento do relatório de pagamento de taxas da biblioteca no portal do aluno.

Arquivo: RM.Bib.Utils.Server.dll

# TOTVS Gestão Compras e Faturamento

## 12.1.2602.100

### Rotina: ARRENDAMENTO MERCANTIL

* **[Ticket: 26121576 / DRMMATERIAIS-8759]** Ajuste para previsão financeira de contrato de arrendamento ser do tipo a pagar

Arquivos: RM.Ctr.Contrato.Api.dll; RM.Ctr.Contrato.Domain.Server.dll

### Rotina: DEMAIS PROCESSOS

* **[Ticket: 26149229 / DRMMATERIAIS-8909]** Melhoria para melhor performance da tela de Movimento durante a navegação entre campos da tela.

Arquivos: RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.IService.dll; RM.Mov.Movimento.Data.dll

* **[Ticket: 26468225 / DRMMATERIAIS-8925]** Ajuste no carregamento dos registros no lookup de CEI

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: MANUTENÇÃO DE CONTRATO

* **[Ticket: DRMMATERIAIS-8235]** Melhorias no processo de contabilização no processo de reajuste

Arquivo: RM.Ctr.Contrato.Domain.Server.dll

## 12.1.2602.101

### Rotina: DEMAIS PROCESSOS

* **[Ticket: 26271316 / DRMMATERIAIS-8682]** Melhoria para que o processo de exclusão de movimento ocorra corretamente em movimentos que possuem vinculos com Processos Judiciais.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: MANUTENÇÃO DE CONTRATO

* **[Ticket: DRMMATERIAIS-8238]** Melhorias no processo de cópia de contrato

Arquivos: RM.Ctr.Contrato.Domain.Server.dll; RM.Ctr.Contrato.Domain.Core.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - ECF (RM LI)

* **[Ticket: DMONTRIBRM-3120]** Realizado o ajuste na lógica para colocar máscara em CNPJ alfanumérico

Arquivo: RM.Mov.TOTVSColab.Service.dll

### Rotina: TIPO DE MOVIMENTO

* **[Ticket: 26314138 / DRMMATERIAIS-8825]** Aumento do limite de caracteres da chave de acesso para 50.

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Form.dll; RM.Mov.CupomFiscal.Intf.dll; RM.Mov.Movimento.Intf.dll; RM.Mov.CTe.Service.dll

## 12.1.2602.104

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DMOTORFISCALRM-145]** Ajustado importacao do Xml via TPF de NFe com dados de IBS/CBS

Arquivos: RM.Mov.Integracoes.Intf.dll; RM.Mov.Integracoes.Service.dll

### Rotina: INCLUSÃO

* **[Ticket: 26323442 / DRMMATERIAIS-8728]** Implementação de cache para ganho de performance.

Arquivos: RM.Mov.Facade.Intf.dll; RM.Mov.Parametros.Intf.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Utils.Intf.dll

## 12.1.2602.105

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: 26464212 / DRMMATERIAIS-8864]** Implementação de melhorias diversas no processo de exclusão de movimentos, visando otimizar a performance.

Arquivos: RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.IService.dll; RM.Mov.Movimento.Service.dll

## 12.1.2602.106

### Rotina: NF-E - CADASTRO

* **[Ticket: DOCELETRONICOS-523]** Ajuste no tamanho maximo do campo: PROTOCOLOAUTNFE

Arquivos: RM.Mov.CTe.Form.dll; RM.Mov.CTe.Intf.dll

## 12.1.2602.107

### Rotina: APROVAÇÃO POR WORKFLOW

* **[Ticket: 26544595 / DRMMATERIAIS-8928]** Ajuste na aprovação por workflow

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Data.dll

### Rotina: INCLUSÃO

* **[Ticket: 26229349 / DOCELETRONICOS-456]** Ajustes visuais para formulários

Arquivo: RM.Mov.CTe.Form.dll

## 12.1.2602.108

### Rotina: REGISTRAR ORÇAMENTO

* **[Ticket: 26217172 / DRMMATERIAIS-8927]** Melhoria na performance ao abir a tela de Registrar Orçamento de Cotação.

Arquivo: RM.Cmp.Cotacao.Data.dll

## 12.1.2602.110

### Rotina: INTEGRAÇÃO CONTÁBIL

* **[Ticket: 25633647 / DRMMATERIAIS-9045]** Melhoria no processo de cancelamento de movimento com contabilização

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: MEDIÇÃO DE CONTRATO

* **[Ticket: DRMMATERIAIS-8614]** Ajuste no aditivo de quantidade relacionado a parcelas inativas

Arquivo: RM.Ctr.Contrato.Domain.Server.dll

## 12.1.2602.111

### Rotina: INTEGRAÇÃO CONTÁBIL

* **[Ticket: DRMMATERIAIS-9029]** Disponibilizado fracionamento de JOB no processo Contabilizar Movimento.

Arquivos: RM.Mov.Processos.Intf.dll; RM.Mov.Processos.Data.dll; RM.Mov.Processos.Form.dll; RM.Mov.Movimento.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DRMMATERIAIS-9053]** Adição de campos do tipo"Compra Governamental" na tela de tributos

Arquivos: RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.IService.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Intf.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Api.dll

## 12.1.2602.112

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-8971]** Inclusão do campo data de retorno no item do movimento e Tipo de Operação no movimento

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.IService.dll; RM.Mov.Movimento.Intf.dll

## 12.1.2602.113

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-8971]** Inclusão do campo data de retorno no item do movimento e Tipo de Operação no movimento

Arquivos: RM.Mov.Movimento.Intf.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Consts.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.IService.dll

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: 26643199 / DRMMATERIAIS-9069]** Melhoria na performance no faturamento/recebimento de movimento na cópia de naturezas realizada no movimento de destino.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DRMMATERIAIS-9053]** Adição de campos do tipo"Compra Governamental" na tela de tributos IBS/CBS

Arquivos: RM.Mov.Movimento.Intf.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Data.dll

## 12.1.2602.114

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-8971]** Inclusão do campo data de retorno no item do movimento e Tipo de Operação no movimento

Arquivos: RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Api.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.IService.dll

### Rotina: INCLUSÃO MOVIMENTO A PARTIR DE XML

* **[Ticket: 26589789 / DOCELETRONICOS-949]** Ajuste na validação dos tributos no processo de inclusão de movimento via arquivo XML.

Arquivo: RM.Mov.Movimento.Data.dll

* **[Ticket: 26589789 / DOCELETRONICOS-949]** Ajuste na busca dos tributos no processo de inclusão de movimento via arquivo XML.

Arquivo: RM.Mov.Movimento.Data.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DRMMATERIAIS-9053]** Adição de defensivo na API para campos do tipo"Compra Governamental" de tributos IBS/CBS

Arquivos: RM.Mov.Movimento.Intf.dll; RM.Mov.Api.dll

* **[Ticket: DRMMATERIAIS-9053]** Adição de campos do tipo"Compra Governamental" de tributos IBS/CBS

Arquivo: RM.Mov.Movimento.Data.dll

## 12.1.2602.116

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-9064]** Implementação do processo de fracionamento de JOBs para estorno de contabilização.

Arquivos: RM.Mov.Processos.Data.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Processos.Form.dll; RM.Mov.Processos.Intf.dll

### Rotina: FATURAMENTO DE CONTRATO

* **[Ticket: 26454830 / DRMMATERIAIS-9028]** Ajuste no processo de Faturamento

Arquivo: RM.Ctr.Contrato.Domain.Server.dll

## 12.1.2602.117

### Rotina: CONFIGURAÇÃO

* **[Ticket: DRMMATERIAIS-8899]** Atualização de versão do Painel do movimento

Arquivo: Cmp/portaldofornecedor

### Rotina: CÓPIA A PARTIR DE OUTRO MOVIMENTO

* **[Ticket: 26846312 / DRMMATERIAIS-9180]** Melhoria na inclusão de Movimento para permitir 150 caracteres no Nome do Destinatário do Serviço.

Arquivo: RM.Mov.Movimento.Intf.dll

### Rotina: DEMAIS CADASTROS

* **[Ticket: 23739897 / DRMMATERIAIS-6585]** Ajuste na cópia de motivo

Arquivos: RM.Cmp.Cadastros.Data.dll; RM.Cmp.Cadastros.Intf.dll

### Rotina: GERAR QRCODE

* **[Ticket: 26829546 / FINANCEIRO01-27420]** Ajustes para que seja incluído o log da sessão de caixa corretamente

Arquivo: Fin/portalfinanceiro

### Rotina: INCLUSÃO MOVIMENTO A PARTIR DE XML

* **[Ticket: 24626353 / DOCELETRONICOS-86]** CTe - atalho para tradução de XML

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: MANUTENÇÃO DE CONTRATO

* **[Ticket: DRMMATERIAIS-8283]** Integração de RM reports com o TAE nas actions de movimento e contrato

Arquivos: RM.Mov.Movimento.Service.dll; RM.Ctr.Contrato.Form.dll; RM.Mov.Consts.dll; RM.Mov.Movimento.IService.dll; RM.Mov.Movimento.Form.dll

* **[Ticket: 26532819 / DRMMATERIAIS-9152]** Melhoria relacionada a consulta de centro de custo nos lookups do contrato 2.0

Arquivo: RM.Ctr.Contrato.Domain.Core.dll

### Rotina: TIPO DE MOVIMENTO

* **[Ticket: 26804516 / DRMMATERIAIS-9181]** Ajuste na atualização dos parâmetros opcionais do movimento

Arquivo: RM.Mov.Parametros.Data.dll

## 12.1.2602.119

### Rotina: MOVIMENTO (RT)

* **[Ticket: 26449133 / DRMMATERIAIS-9115]** Melhoria relacionada à definição da regra tributária de movimentação origem educacional

Arquivo: RM.Mov.Movimento.Service.dll

## 12.1.2602.121

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: 26988539 / DRMMATERIAIS-9319]** Melhoria no cache ao atualizar parâmetros de movimento

Arquivos: RM.Mov.Parametros.Data.dll; RM.Mov.Parametros.Intf.dll

## 12.1.2602.124

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DRMMATERIAIS-9293]** Criação do parâmetro tipo de movimento - Agronegócio

Arquivos: RM.Mov.Parametros.Form.dll; RM.Mov.Parametros.Intf.dll; RM.Mov.Parametros.Data.dll

## 12.1.2602.125

### Rotina: DEMAIS PROCESSOS

* **[Ticket: 23664352 / DRMMATERIAIS-6718]** Melhoria relacionada à aplicação de segurança de campo nas informações de pagamento do movimento.

Arquivo: RM.Mov.Movimento.Data.dll

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: 26988539 / DRMMATERIAIS-9319]** Melhoria no cache ao atualizar parâmetros de movimento

Arquivos: RM.Mov.Parametros.Data.dll; RM.Mov.Parametros.Intf.dll; RM.Mov.Facade.Intf.dll

## 12.1.2602.126

### Rotina: NF-E - ENVIO

* **[Ticket: DMONTRIBRM-3741]** Alterar a visibilidade e domínio do campo Tipo de Operação com Entes Governamentais

Arquivos: RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Form.dll

## 12.1.2602.129

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DRMMATERIAIS-9295]** Inclusão do campo de valor e percentual de retorno (ISS) no movimento e item

Arquivos: RM.Mov.Movimento.IService.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Formula.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Intf.dll; RM.Mov.CopiaMovimento.Service.dll

### Rotina: DEMAIS CADASTROS

* **[Ticket: 24240632 / DRMMATERIAIS-6952]** Melhoria na visualização e navegação das permissões do usuário por tipo de movimento

Arquivos: RM.Mov.TipoMovimento.Form.dll; RM.Mov.Movimento.Form.dll

### Rotina: DEMAIS PROCESSOS

* **[Ticket: 26734117 / DRMMATERIAIS-9198]** Ajuste na configuração de permissão de acesso a campos

Arquivos: RM.Mov.Movimento.Intf.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Form.dll

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: DRMMATERIAIS-9535]** Melhoria relacionada a seleção de regra tributária aplicada aos itens de movimento

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Form.dll

## 12.1.2602.131

### Rotina: DEMAIS PROCESSOS

* **[Ticket: 26149229 / DRMMATERIAIS-9179]** Melhoria na tela de Movimento para melhoria de performance.

Arquivos: RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Intf.dll

## 12.1.2602.132

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DRMMATERIAIS-9292]** Adicionando aba de Agronegocio no movimento

Arquivos: RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.IService.dll; RM.Mov.Lib.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Service.dll; RM.Mov.CopiaMovimento.Service.dll; RM.Mov.Movimento.Intf.dll

### Rotina: DEMAIS PROCESSOS

* **[Ticket: 26734117 / DRMMATERIAIS-9198]** Melhoria no processo de configuração de acesso nos campos de trbituos

Arquivos: RM.Mov.Movimento.Intf.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Data.dll

## 12.1.2602.133

### Rotina: ANEXOS

* **[Ticket: DRMMATERIAIS-9645]** Adicionando parâmetros Tipo de Nota de Débito/Crédito

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: 25218352 / DRMMATERIAIS-8994]** Ajuste no preenchimento default de natureza de operação para movimentos que utilizam CTRC

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: TIPO DE MOVIMENTO

* **[Ticket: DRMMATERIAIS-9352]** Adicionando parâmetros Tipo de Nota de Débito/Crédito

Arquivos: RM.Mov.Consts.dll; RM.Mov.Parametros.Form.dll; RM.Mov.Parametros.Data.dll; RM.Mov.Parametros.Intf.dll

## 12.1.2602.135

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: 27012412 / DRMMATERIAIS-9375]** Ajuste no faturamento de movimento

Arquivos: RM.Mov.CopiaMovimento.Service.dll; RM.Mov.Movimento.Service.dll

## 12.1.2602.136

### Rotina: CT-E (RT)

* **[Ticket: 26625971 / DOCELETRONICOS-1312]** Grupo IBS/CBS não deve ser preenchido para o CST informado

Arquivo: RM.Mov.CTe.Service.dll

### Rotina: INCLUSÃO MOVIMENTO A PARTIR DE XML

* **[Ticket: 26907994 / DOCELETRONICOS-1230]** Ajuste na criação de movimento a partir de xml de NFS-e.

Arquivo: RM.Mov.Movimento.Data.dll

### Rotina: NOTA FISCAL DE COMUNICAÇÃO ELETRÔNICA

* **[Ticket: DMONTRIBRM-3842]** Ajustes referente a obsolescência programada

Arquivo: RM.Mov.Movimento.Data.dll

## 12.1.2602.137

### Rotina: CADASTROS DE VALORES ORÇADOS

* **[Ticket: 26524730 / DRMMATERIAIS-9068]** Ajuste na consistência de preenchimento do campo tipo de orçamento durante a importação

Arquivos: RM.Mov.Orcamento.Service.dll; RM.Mov.Orcamento.Data.dll

### Rotina: NF-E - ENVIO

* **[Ticket: DMOTORFISCALRM-517]** Implementação para que o processo de associação de notas seja possivel para todos os tipos de documentos.

Arquivos: RM.Mov.Movimento.Data.dll; RM.Mov.Parametros.Form.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Lib.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DMOTORFISCALRM-383]** Escrituração - % redução aliquota compra governamental

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.Facade.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Intf.dll

### Rotina: PROCESSO PRODUTIVO SIMPLES

* **[Ticket: DRMMATERIAIS-8510]** Ajuste na classificação de componentes ao faturar movimento de estrutura

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Data.dll

## 12.1.2602.140

### Rotina: NFS-E - CADASTRO

* **[Ticket: DMOTORFISCALRM-534]** Implementação CTe - NT 2025.001 – Versão 1.14 - Compra Governamental

Arquivos: RM.Mov.CTe.Service.dll; RM.Mov.CTe.Intf.dll

## 12.1.2602.141

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-9386]** Melhoria de performance na exclusão de movimentos

Arquivo: RM.Mov.Movimento.Service.dll

## 12.1.2602.142

### Rotina: CT-E - ENVIO

* **[Ticket: DMOTORFISCALRM-533]** Implementação CTeOS - NT 2025.001 – Versão 1.14 - Compra Governamental

Arquivos: RM.Mov.CTe.Intf.dll; RM.Mov.CTe.Service.dll

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-9386]** Melhoria de performance na exclusão de movimentos

Arquivo: RM.Mov.Movimento.Service.dll

## 12.1.2602.144

### Rotina: INCLUSÃO

* **[Ticket: 27717526 / DRMMATERIAIS-9798]** Melhorias no Movimento para correto posicionamento dos detalhes de Tributo do Movimento.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: INTEGRAÇÃO CONTÁBIL

* **[Ticket: DRMMATERIAIS-9807]** Criação cas funções de fórmula "GRAVARCACHE" E "LERCACHE"

Arquivo: RM.Mov.Formula.dll

### Rotina: QUADRO COMPARATIVO

* **[Ticket: 26539696 / DRMMATERIAIS-9140]** Melhorias no Quadro comparativo para informar cores com relação ao status dos itens do Quadro

Arquivo: RM.Cmp.Cotacao.Form.dll

### Rotina: TIPO DE MOVIMENTO

* **[Ticket: DRMMATERIAIS-9680]** Parâmetro para seleção do tipo de movimento a ser gerado na automatização de movimentos do tipo nota de débito do tipo multa e juros.

Arquivos: RM.Mov.Parametros.Intf.dll; RM.Mov.Parametros.Data.dll; RM.Mov.Parametros.Form.dll

## 12.1.2602.145

### Rotina: INCLUSÃO

* **[Ticket: DMONTRIBRM-3953]** [MOV | TRIBUTOS] Adição de lookup do beneficiário da COSIRF

Arquivos: RM.Mov.Movimento.Intf.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Api.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Form.dll; RM.Mov.Movimento.IService.dll

* **[Ticket: DMONTRIBRM-3953]** [MOV | TRIBUTOS] Correção keyfields do lookup

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: NF-E - CONSULTA AUTORIZAÇÃO

* **[Ticket: 27959907 / DMOTORFISCALRM-680]** Escrituração CBS/IBS - Compra governamental

Arquivo: RM.Mov.Movimento.Form.dll

## 12.1.2602.147

### Rotina: MOVIMENTO (RT)

* **[Ticket: DRMMATERIAIS-9584]** Novo motivo de referencia - Nota de Débito - Multas e Juros

Arquivos: RM.Mov.Parametros.Data.dll; RM.Mov.CopiaMovimento.Service.dll; RM.Mov.Parametros.Form.dll; RM.Mov.Consts.dll; RM.Mov.Processos.Form.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Form.dll

## 12.1.2602.149

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: 27638637 / DRMMATERIAIS-9769]** Melhoria relacionada a tela de movimento, ao visualizar e usar o OK para fechar a tela, poderia entrar em alteração e atualizar dados de último usuário a alterar o movimento sem que nenhuma alteração tivesse sido de fato realizada.

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: INCLUSÃO

* **[Ticket: DMONTRIBRM-3953]** [MOV | TRIBUTOS] Ajuste do LkpBenef - COSIRF no item do movimento

Arquivo: RM.Mov.Movimento.Form.dll

## 12.1.2602.150

### Rotina: DEMAIS CADASTROS

* **[Ticket: DRMMATERIAIS-9815]** Melhorias na API do Portal do Fornecedor

Arquivo: RM.Cmp.Api.dll

### Rotina: DEMAIS PROCESSOS

* **[Ticket: DRMMATERIAIS-9808]** Melhoria de performance na exclusão de movimentos

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSÃO

* **[Ticket: 28053449 / DRMMATERIAIS-9922]** Melhoria relacionada a tela de movimento, na exibição dos campos da aba de NFe estadual

Arquivo: RM.Mov.Movimento.Form.dll

### Rotina: MOVIMENTO (RT)

* **[Ticket: DRMMATERIAIS-9584]** Ajuste na parametrizaão - ND Multa e Juros

Arquivo: RM.Mov.Parametros.Data.dll

### Rotina: PORTAL

* **[Ticket: DRMMATERIAIS-9356]** Ajustes internos nas telas de contrato

Arquivo: Ctr/contrato-front

* **[Ticket: DRMMATERIAIS-9356]** Ajustes internos do portal do fornecedor

Arquivo: Cmp/portaldofornecedor

## 12.1.2602.151

### Rotina: INTEGRAÇÃO CONTÁBIL

* **[Ticket: 26595342 / DRMMATERIAIS-9268]** Melhoria relacionada ao cálculo do valor do movimento criado por cópia por referência, onde a quantidade é zero e preço editado. Agora o valor é calculado e definido para o movimento ao chamar o cálculo de valor dentro do item do movimento.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: MOVIMENTO (RT)

* **[Ticket: DRMMATERIAIS-9887]** Evolução do Motivo de Referência: Nota de Débito - Juros e Multa, para copiar CFOP

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.CopiaMovimento.Service.dll

## 12.1.2602.152

### Rotina: NFS-E - ENVIO

* **[Ticket: DRMMATERIAIS-9734]** Criação de Serviço para atualização de valores em Movimentos de Nota Fiscal de Serviço após a autorização do mesmo.

Arquivos: RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.IService.dll; RM.Mov.Utils.Server.dll

## 12.1.2602.153

### Rotina: ESCRITURAÇÃO (RM LI)

* **[Ticket: DMOTORFISCALRM-644]** Foi realizada uma melhoria no processo de estorno de Lançamentos Fiscais com foco em reduzir os travamentos de banco de dados (deadlocks) observados durante o processamento de lotes com grande volume de registros.

Arquivo: RM.Mov.Movimento.Service.dll

### Rotina: INCLUSÃO MOVIMENTO A PARTIR DE XML

* **[Ticket: 26972762 / DOCELETRONICOS-1335]** Ajustes para tradução de XML

Arquivo: RM.Mov.Integracoes.Service.dll

### Rotina: PORTAL

* **[Ticket: DRMMATERIAIS-9982]** Melhorias na API do Portal do Fornecedor

Arquivo: RM.Cmp.Api.dll

* **[Ticket: DRMMATERIAIS-9982]** Implementação de segurança nas APIS

Arquivo: Cmp/portaldofornecedor

## 12.1.2602.154

### Rotina: MOVIMENTO (RT)

* **[Ticket: DRMMATERIAIS-9735]** Criação de campos para exibição de valores em Movimentos de Nota Fiscal de Serviço após a autorização do mesmo.

Arquivos: RM.Mov.Movimento.Data.dll; RM.Mov.Movimento.Intf.dll; RM.Mov.Movimento.Service.dll; RM.Mov.Movimento.Form.dll

## 12.1.2602.157

### Rotina: Sem Rotina Específica

* **[Ticket: DMONTRIBRM-3958]** [TRB Movimento] Defensivo de visibilidade para o campo Beneficiario no tributo do movimento

Arquivo: RM.Mov.Movimento.Form.dll

## 12.1.2602.162

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DMONTRIBRM-4114]** [BP-e] Adição do tipo BP-e TM no movimento, escrituração/lanc. e SPED D100

Arquivo: RM.Mov.Consts.dll

## 12.1.2602.167

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1551]** Melhoria para correta inclusão do campo Alíquota no serviço de atualização da NFS-e

Arquivo: RM.Mov.Utils.Server.dll

## 12.1.2602.170

### Rotina: ASSISTENTE COTAÇÃO

* **[Ticket: 27239238 / DRMMATERIAIS-9534]** Melhoria relacionada a importação de planilha de orçamento/negociação com planilha em caminho compartilhado rede.

Arquivos: RM.Cmp.Lib.dll; RM.Cmp.Cotacao.Form.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 27334251 / DRMMATERIAIS-10085]** Melhoria para correta inclusão do campo Alíquota no serviço de atualização da NFS-e

Arquivo: RM.Mov.Movimento.Service.dll

## 12.1.2602.171

### Rotina: TRANSAÇÕES (CARTÃO DE CRÉDITO, CYBERSOURCE)

* **[Ticket: FINANCEIRO01-27950]** Desativado pagamento de dois cartões

Arquivo: Fin/checkout

## 12.1.2602.174

### Rotina: INCLUSÃO

* **[Ticket: 29020485 / DRMMATERIAIS-10286]** Ajuste na parametrização de cache

Arquivo: RM.Mov.Movimento.Data.dll

# TOTVS Gestão Contábil

## 12.1.2602.101

### Rotina: GERAR SPED CONTÁBIL (RM CTB)

* **[Ticket: CONTROLADORIA01-13550]** Performance SPED Contábil - melhoria aplicada

Arquivo: RM.Ctb.Sped.Service.dll

## 12.1.2602.102

### Rotina: BALANCETE (RM CTB)

* **[Ticket: 26011194 / CONTROLADORIA01-14466]** Melhoria em qualidade de código dos relatórios Balancete, Razão e Retrospectiva

Arquivo: RM.Ctb.Relatorios.Data.dll

## 12.1.2602.111

### Rotina: AGRUPAMENTO DE LANÇAMENTO CONTÁBEIS (RM CTB)

* **[Ticket: 25466450 / CONTROLADORIA01-14496]** Agrupamento - melhorias em código

Arquivo: RM.Ctb.Lan.Service.dll

* **[Ticket: 25466450 / CONTROLADORIA01-14496]** Melhoria de performance em agrupamento com mais de mil partidas.

Arquivo: RM.Ctb.Lan.Service.dll

## 12.1.2602.115

### Rotina: COPIAR CENTRO DE CUSTO ENTRE COLIGADAS (RM CTB)

* **[Ticket: CONTROLADORIA01-14535]** Correção do processo de cópia de centro de custo.

Arquivos: RM.Ctb.Processos.Data.dll; RM.Ctb.Parametros.Data.dll; RM.Ctb.Parametros.Intf.dll

## 12.1.2602.120

### Rotina: BALANCETE (RM CTB)

* **[Ticket: 26971246 / CONTROLADORIA01-14574]** Relatórios - melhorias em qualidade de código

Arquivos: RM.Ctb.Relatorios.Data.dll; RM.Ctb.Relatorios.Intf.dll; RM.Ctb.Relatorios.Form.dll

## 12.1.2602.124

### Rotina: COPIAR CONTAS CONTÁBEIS ENTRE COLIGADAS (RM CTB)

* **[Ticket: 26738928 / CONTROLADORIA01-14552]** Perfomance do processo de rastreabilidade melhorada.

Arquivos: RM.Ctb.Sped.Form.dll; RM.Ctb.Sped.Data.dll; RM.Ctb.ConsisteLancamento.Service.dll

## 12.1.2602.135

### Rotina: APURAÇÃO DE RESULTADO DO EXERCÍCIO (RM CTB)

* **[Ticket: CONTROLADORIA01-14518]** Transferencia dos Grupos Contábeis

Arquivo: RM.Ctb.Lan.Service.dll

## 12.1.2602.142

### Rotina: APURAÇÃO DE RESULTADO DO EXERCÍCIO (RM CTB)

* **[Ticket: CONTROLADORIA01-14687]** Melhorias em qualidade de código

Arquivo: RM.Ctb.Lan.Service.dll

## 12.1.2602.144

### Rotina: TOTVS GESTÃO CONTÁBIL (RM CTB)

* **[Ticket: 25030138 / CONTROLADORIA01-13996]** Fluxo de Aprovação - Permitida a exclusão de lançamentos integrados ao lote zero caso usuário seja aprovador.

Arquivo: RM.Ctb.Lan.Service.dll

## 12.1.2602.145

### Rotina: APURAÇÃO DE RESULTADO DO EXERCÍCIO (RM CTB)

* **[Ticket: CONTROLADORIA01-14687]** Melhoria em qualidade de código

Arquivo: RM.Ctb.Lan.Service.dll

## 12.1.2602.153

### Rotina: Sem Rotina Específica

* **[Ticket: CONTROLADORIA01-14686]** Conciliação Contábil - melhorias em validações

Arquivo: RM.Ctb.Lan.Form.dll

### Rotina: APURAÇÃO DE RESULTADO DO EXERCÍCIO (RM CTB)

* **[Ticket: 28263466 / CONTROLADORIA01-14739]** Melhorias em qualidade de código

Arquivo: RM.Ctb.Lan.Service.dll

### Rotina: BALANCETE (RM CTB)

* **[Ticket: 27629946 / CONTROLADORIA01-14653]** Melhorias de performance nos relatórios gerenciais

Arquivo: RM.Ctb.Relatorios.Service.dll

## 12.1.2602.157

### Rotina: BALANCETE (RM CTB)

* **[Ticket: 27176532 / CONTROLADORIA01-14638]** Correção do parametro interno devido atualização da versão do smart-view.

Arquivos: RM.Ctb.NativeProvider.Service.dll; RM.Ctb.Relatorios.Form.dll

## 12.1.2602.167

### Rotina: RM CONECTOR (RM CTB)

* **[Ticket: 26627547 / CONTROLADORIA01-14721]** Remoção da rotina quee validava se a conta parelela exisitia nas contas contábeis globais.

Arquivo: RM.Ctb.Contas.Data.dll

# TOTVS Gestão de Estoques e contratos

## 12.1.2602.100

### Rotina: CADASTRO DE INVENTÁRIO

* **[Ticket: DRMMATERIAIS-8902]** Melhorias no filtro de produto ao cadastrar inventário

Arquivos: RM.Est.Inventario.Intf.dll; RM.Est.Inventario.Data.dll; RM.Est.Inventario.Form.dll

## 12.1.2602.104

### Rotina: INCLUSÃO

* **[Ticket: 26323442 / DRMMATERIAIS-8728]** Implementação de cache para ganho de performance.

Arquivo: RM.Est.Lib.dll

## 12.1.2602.110

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 26501300 / DRMMATERIAIS-8926]** Ajuste no menu de acesso do perfil de usuário

Arquivos: RM.Est.dll; RM.Est.Server.dll; RM.Est.Menu.dll

## 12.1.2602.114

### Rotina: ANEXOS DO PRODUTO

* **[Ticket: 24789432 / DRMMATERIAIS-7519]** Melhoria para gestão correta do idnetificador de Lote d eProduto no Cadastro de Lotes

Arquivo: RM.Est.Produto.Data.dll

## 12.1.2602.117

### Rotina: CONFIGURAÇÃO

* **[Ticket: DRMMATERIAIS-8899]** Atualização de versão do Painel do movimento

Arquivo: Est/estoque-front

* **[Ticket: 26243890 / DRMMATERIAIS-9002]** Alteração gerenciador de colunas

Arquivo: Est/estoque-front

* **[Ticket: 26243890 / DRMMATERIAIS-9002]** Alteração abas filtros e abas do tipo de movimentos

Arquivo: Est/estoque-front

### Rotina: DEMAIS CADASTROS

* **[Ticket: 25064935 / DRMMATERIAIS-7788]** Melhoria para não exibir o menu de Tabelas de Classificação quando não estiver parametrizado nos parâmetros de Tabelas

Arquivo: RM.Est.Cadastros.Form.dll

## 12.1.2602.123

### Rotina: CADASTRO DE INVENTÁRIO

* **[Ticket: 25466993 / DRMMATERIAIS-8227]** Melhoria no processo de inclusão de inventários para quando se incluem endereçamentos de locais de estoque distintos.

Arquivos: RM.Est.Inventario.Data.dll; RM.Est.Inventario.Intf.dll; RM.Est.Inventario.Form.dll

## 12.1.2602.125

### Rotina: INTEGRAÇÃO COM O NUCLEUS ( TOTVS GESTÃO DE ESTOQUE, COMPRAS E FATURAMENTO )

* **[Ticket: 26376014 / DRMMATERIAIS-9395]** Ajuste na validação do preenchimento do local de estoque durante a baixa de estoque

Arquivo: RM.Est.Baixa.Service.dll

## 12.1.2602.130

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 26263855 / DRMMATERIAIS-9066]** Melhoria no processo de regeração de Saldos e Custos para correto controle de Saldo de Números de Série em Estoque com Terceiros quando o item passa por Processos de Manutenção.

Arquivo: RM.Est.Estoque.Service.dll

## 12.1.2602.145

### Rotina: UTILITÁRIOS - DUPLICAÇÕES (RM LI)

* **[Ticket: DMOTORFISCALRM-576]** Ajuste na cópia de unidade de medida multicoligada.

Arquivos: RM.Est.Cadastros.Data.dll; RM.Est.Cadastros.Form.dll

* **[Ticket: DMOTORFISCALRM-576]** Cópia de Unidade de Medidas.

Arquivos: RM.Est.Cadastros.Data.dll; RM.Est.Cadastros.Form.dll

## 12.1.2602.150

### Rotina: PORTAL

* **[Ticket: DRMMATERIAIS-9356]** Ajustes internos no painel do movimento

Arquivo: Est/estoque-front

## 12.1.2602.162

### Rotina: GERAL - TABELAS PRODUTOS

* **[Ticket: DRMMATERIAIS-10042]** Ajuste na cópia de parâmetro de produto

Arquivo: RM.Est.Processos.Data.dll

## 12.1.2602.170

### Rotina: DEMAIS CADASTROS

* **[Ticket: DRMMATERIAIS-10223]** Remoção banner aviso reforma tributária

Arquivos: RM.Est.Utils.Form.dll; RM.Est.dll

# TOTVS Gestão de Pessoas

## 12.1.2602.101

### Rotina: ALTERAÇÃO DE DADOS FUNCIONAIS

* **[Ticket: DRHHCM-16782]** Limpar filtro de consulta de requisitantes nas requisições.

Arquivo: RM.Rhu.Requisicao.Form.dll

### Rotina: MEU PONTO - ESPELHO DO PONTO

* **[Ticket: 26332613 / DRHMEURH-20879]** Ajuste na exibição do espelho de ponto | MeuRH

Arquivo: Rh/Portais

## 12.1.2602.104

### Rotina: USO DE DADOS PESSOAIS

* **[Ticket: DRHCONS-8856]** Ajuste nos termos de Opt-out

Arquivo: Rh/Portais

## 12.1.2602.106

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26633658 / DRHMEURH-20987]** Criação de parâmetro para ignorar validação de Data Prevista no avanço de requisições | Meu RH

Arquivos: RM.Rhu.Parametros.Form.dll; RM.Rhu.Parametros.Intf.dll; RM.Fop.Rest.Server.dll

### Rotina: PORTAL WEB - SUBORDINADOS (LAB.01.213)

* **[Ticket: DRHHCM-17030]** Ajuste na visualização de subordinados de supervisores

Arquivos: RM.Rhu.NovaHierarquia.Service.dll; RM.Rhu.Hierarquia.IService.dll; RM.Rhu.Hierarquia.Service.dll; RM.Fop.Funcionario.Server.dll

## 12.1.2602.107

### Rotina: PROCESSOS TRABALHISTAS

* **[Ticket: DRHSSTPT-1252]** Adequações do CNPJ alfanumérico para o processo trabalhista smartview

Arquivo: RM.Rhu.Api.dll

## 12.1.2602.110

### Rotina: QUIRONS

* **[Ticket: 26144347 / DRHSSTPT-1710]** Correção na obtenção dos dados da entidade de Pessoa para integração com o Quirons

Arquivo: RM.Rhu.Pessoa.Data.dll

## 12.1.2602.111

### Rotina: MEU PONTO - VER RESUMO

* **[Ticket: DRHMEURH-20899]** Ajuste para a correta exibição de horário contiguo no Meu RH

Arquivo: Rh/Portais

### Rotina: MEU RH - GESTÃO DE FÉRIAS EQUIPE

* **[Ticket: 26733916 / DRHMEURH-21109]** Ajuste na solicitação de férias para permitir salvar corretamente

Arquivo: Rh/Portais

### Rotina: MEU RH - RELATÓRIOS

* **[Ticket: 26100388 / DRHMEURH-20897]** Ajuste para realizar download de relatórios corretamente no Android

Arquivo: Rh/Portais

## 12.1.2602.112

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26459872 / DRHMEURH-20885]** Ajuste na mensagem de validação de salário na requisição de substituição

Arquivo: Rh/Portais

## 12.1.2602.113

### Rotina: PROCESSOS TRABALHISTAS

* **[Ticket: 26814483 / DRHSSTPT-1846]** Alteração na API de versão do leiaute do Processo Trabalhista

Arquivo: RM.Rhu.Api.dll

## 12.1.2602.114

### Rotina: MINHAS SOLICITAÇÕES

* **[Ticket: DRHCONS-8918]** Alteração Status e Tootip - Minhas Solicitações

Arquivo: Rh/Portais

### Rotina: PERFIL DO COLABORADOR

* **[Ticket: 25637558 / DRHMEURH-20125]** Ajuste de mensagem indevida: Chapa do seu usuário não foi identificada. Entre em contato com o suporte

Arquivo: Rh/Portais

* **[Ticket: 26702265 / DRHMEURH-21177]** Ajuste para permitir edição de dados no Perfil do colaborador

Arquivo: Rh/Portais

## 12.1.2602.116

### Rotina: ALT. CAD. - ALTERAÇÃO CAMPOS DO CADASTRO

* **[Ticket: DRHROTRM-15753]** fix: filtro de busca do candidato

Arquivos: RM.Rhu.Lib.Intf.dll; RM.Rhu.Pessoa.Data.dll; RM.Rhu.Lib.WinForms.dll

* **[Ticket: DRHROTRM-15753]** feat: retornar registro preliminar dentro do cadastro do ATS

Arquivos: RM.Rhu.Pessoa.Data.dll; RM.Rhu.Lib.Intf.dll; RM.Rhu.Lib.WinForms.dll

* **[Ticket: DRHROTRM-15753]** fix: retornar código de vaga

Arquivos: RM.Rhu.Pessoa.Data.dll; RM.Rhu.Lib.Intf.dll; RM.Rhu.Lib.WinForms.dll

* **[Ticket: DRHROTRM-15753]** fix: validar código de vaga para o registro preliminar, data de admissão e grid selecionada

Arquivos: RM.Rhu.Lib.Intf.dll; RM.Rhu.Lib.WinForms.dll

### Rotina: CADASTRO

* **[Ticket: 26653913 / DRHHCM-17102]** Ajuste nos campos complementares do cadastro de pessoa

Arquivo: RM.Rhu.Lib.WinForms.dll

## 12.1.2602.119

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26343462 / DRHMEURH-20756]** Permitir desabilitar justificativa na requisição de desligamento

Arquivo: Rh/Portais

### Rotina: RELÓGIO / BATIDA POR GEOLOCALIZAÇÃO

* **[Ticket: 26533997 / DRHMEURH-21322]** Ajuste para retornar timezone corretamente na batida de ponto

Arquivo: Rh/Portais

## 12.1.2602.124

### Rotina: NOVA SOLICITAÇÃO

* **[Ticket: DRHCONS-8969]** Disponibilizado melhorias referentes as issues: DRHCONS-8871, DRHCONS-8924 e DRHCONS-8929

Arquivo: Rh/Portais

## 12.1.2602.127

### Rotina: ARQUIVOS ANEXOS

* **[Ticket: 26826394 / DRHHCM-17151]** Atualizar lista de extensões permitidas no cadastro de anexos do candidatos, igual ao Banco de talentos

Arquivo: RM.Rhu.Pessoa.Form.dll

### Rotina: HIERARQUIA / POSIÇÃO

* **[Ticket: DRHHCM-16984]** Implementação de envio da alteração do chefe da hierarquia para Aghora

Arquivos: RM.Fop.Funcionario.Intf.dll; RM.Rhu.Hierarquia.IService.dll; RM.Rhu.NovaHierarquia.Service.dll; RM.Rhu.NovaHierarquia.Data.dll; RM.Fop.Funcionario.Server.dll; RM.Rhu.Hierarquia.Service.dll; RM.Rhu.Facade.dll

### Rotina: VISUALIZAR AFASTAMENTOS

* **[Ticket: DRHMEURH-21101]** Bloquear reenvio de atestado Colaborador e Gestor

Arquivo: Rh/Portais

## 12.1.2602.129

### Rotina: ANIVERSARIANTES DO TIME

* **[Ticket: 26815896 / DRHMEURH-21343]** Ajuste na conversão de data de aniversariante

Arquivo: Rh/Portais

### Rotina: VISUALIZAR AFASTAMENTOS

* **[Ticket: 26882486 / DRHMEURH-21321]** Ajuste na exibição de afastamentos sem data fim

Arquivo: Rh/Portais

## 12.1.2602.130

### Rotina: MEU RH - AJUSTAR SOLICITAÇÃO DE FÉRIAS

* **[Ticket: DRHMEURH-21262]** Ajuste na rotina de férias para a correta utilização

Arquivo: Rh/Portais

## 12.1.2602.131

### Rotina: Sem Rotina Específica

* **[Ticket: DRHCONS-8869]** Adicionado logo dos parceiros nos cards de propostas e padronizado as telas de contratos e conta bancária para o padrão MeuRH

Arquivo: Rh/Portais

### Rotina: BANCO DE TALENTOS

* **[Ticket: DRHHCM-17261]** Ajuste de seguranca metodo subareaconhecimento

Arquivo: RM.Rhu.Curriculo.Server.dll

### Rotina: INTEGRAÇÃO

* **[Ticket: DRHSSTPT-1921]** Ajuste no processo de Troca chapa do funcionário para geração de mensagem de integração com o Quírons

Arquivos: RM.Rhu.Pessoa.Data.dll; RM.Rhu.Integracao.Intf.dll; RM.Rhu.Integracao.Server.dll; RM.Fop.Funcionario.Server.dll; RM.Rhu.Integracao.Services.dll

### Rotina: MINHA EQUIPE

* **[Ticket: 26987070 / DRHMEURH-21370]** Ajuste na solicitação de abono e sobreaviso

Arquivo: Rh/Portais

## 12.1.2602.133

### Rotina: Sem Rotina Específica

* **[Ticket: 26285184 / DRHMEURH-21344]** Ajuste no retorno de campos com caracteres especiais na requisição de transferência

Arquivo: Rh/Portais

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: DRHMEURH-21263]** Ajuste na visualização e edição das requisições de transferência para correto funcionamento em matrículas com caracteres especiais

Arquivo: Rh/Portais

### Rotina: SEÇÕES

* **[Ticket: 24215136 / DRHROTRM-14494]** feat(ATS): adequar validação de CNPJ para formato alfanumérico

Arquivo: RM.Rhu.Lib.WinForms.dll

## 12.1.2602.134

### Rotina: SUBSTITUIÇÃO

* **[Ticket: 27103273 / DRHHCM-17224]** Refatoração da Lógica de Aprovação: Requisições de Substituição (Portal/Meu RH)

Arquivos: RM.Rhu.Requisicao.Server.dll; RM.Rhu.NovaHierarquia.Service.dll

## 12.1.2602.135

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 26987674 / DRHMEURH-21477]** Ajuste na requisição de transferência, quando a edição acontecer com tabela salarial, para considerar corretamente os dados.

Arquivo: Rh/Portais

## 12.1.2602.136

### Rotina: Sem Rotina Específica

* **[Ticket: DRHSSTPT-1848]** Liberação das adequações para atender à NT 06/2026 do Processo Trabalhista

Arquivo: RM.Rhu.Api.dll

### Rotina: SOLICITAÇÃO DE FÉRIAS

* **[Ticket: 27062943 / DRHMEURH-21456]** Ajuste para permitir alterar dias de férias através das setas de navegação

Arquivo: Rh/Portais

* **[Ticket: 27079476 / DRHMEURH-21487]** Exibir afastamento e adiantamento 13º conforme parametrização na finalização das férias

Arquivo: Rh/Portais

## 12.1.2602.139

### Rotina: MINHAS SOLICITAÇÕES

* **[Ticket: DRHCONS-9057]** Adicionado controle de versionamento de termo de opt-in

Arquivo: Rh/Portais

## 12.1.2602.141

### Rotina: GESTÃO DE PESSOAS X QUIRONS (NG)

* **[Ticket: 26818872 / DRHSSTPT-1898]** Ajuste na geração do valor da chave primária da fila de mensagens para integração com o Quírons

Arquivo: RM.Rhu.Integracao.Server.dll

## 12.1.2602.142

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: 27144005 / DRHMEURH-21641]** Ajuste na visualização de tabelas salariais na requisição de transferência com alteração de função, para considerar a coligada selecionada no Meu RH

Arquivo: Rh/Portais

### Rotina: AVALIAÇÃO DE CONHECIMENTO

* **[Ticket: 26453477 / DRHHCM-17064]** Ajuste na avaliação de conhecimento das turmas

Arquivos: RM.Rhu.Turmas.Data.dll; RM.Rhu.Turmas.Intf.dll

## 12.1.2602.143

### Rotina: SOLICITAÇÃO DE FÉRIAS

* **[Ticket: 27333175 / DRHMEURH-21676]** Ajuste na venda de férias através da navegação por setas

Arquivo: Rh/Portais

## 12.1.2602.144

### Rotina: PERFIL DO COLABORADOR

* **[Ticket: DRHMEURH-21269]** Ajuste na visualização de dados de perfil para o correto funcionamento com diversas matrículas

Arquivo: Rh/Portais

### Rotina: PORTAL - REQUISIÇÕES

* **[Ticket: 26624781 / DRHHCM-17107]** Portal RH - Requisição de Transferência com Alteração de dados - Msg: Não existe vaga e/ou verba disponível conforme o controle de lotação

Arquivos: Portal Corpore.Net

### Rotina: PRÉ-ATESTADO

* **[Ticket: 26414739 / DRHHCM-17340]** Ajuste na busca dos chefes diretos na hierarquia por posição

Arquivo: RM.Rhu.NovaHierarquia.Service.dll

## 12.1.2602.145

### Rotina: AUMENTO DE QUADRO

* **[Ticket: 26697177 / DRHHCM-17115]** Ajuste na visualização da hierarquia requisitante na requisição de aumento de quadro

Arquivo: RM.Rhu.Requisicao.Form.dll

### Rotina: BANCO DE DADOS PLATAFORMA CONSIGNADO

* **[Ticket: DRHCONS-9032]** Ajuste no delay do retorno de envio da solicitação

Arquivo: Rh/Portais

### Rotina: PESSOAS

* **[Ticket: DRHHCM-17388]** Ajuste na visualização do menu Papéis no Corpore

Arquivo: RM.Rhu.Lib.WinForms.dll

### Rotina: VISUALIZAR OCORRÊNCIAS

* **[Ticket: 27316751 / DRHMEURH-21642]** Ajuste na exibição de registros na rotina de ocorrências | MeuRH

Arquivo: Rh/Portais

## 12.1.2602.146

### Rotina: ALTERAÇÃO DE DADOS FUNCIONAIS

* **[Ticket: 26865733 / DRHHCM-17496]** Ajuste na inserção de aumento salarial com progressão

Arquivo: RM.Rhu.Requisicao.Form.dll

## 12.1.2602.150

### Rotina: HIERARQUIA / POSIÇÃO

* **[Ticket: 27895816 / DRHHCM-17457]** Ajuste na visualização da distribuição por lotação

Arquivo: RM.Rhu.ControleDeLotacao.Data.dll

## 12.1.2602.157

### Rotina: APP MEU RH - REQUISIÇÕES

* **[Ticket: DRHMEURH-21212]** Ajuste na validação de férias para permitir alteração da data fim e salvamento do registro durante inclusão de licença maternidade.

Arquivo: RM.Rhu.Requisicao.Server.dll

* **[Ticket: DRHMEURH-21212]** Na requisição geral foi implementado a seleção de até 4 arquivos

Arquivo: Rh/Portais

### Rotina: NOVA SOLICITAÇÃO

* **[Ticket: DRHCONS-9021]** ajuste no filtro de simulações por quantidade de parcelas

Arquivo: Rh/Portais

* **[Ticket: DRHCONS-9021]** Implementação do Refresh nas telas de simulações e solicitações

Arquivo: Rh/Portais

## 12.1.2602.158

### Rotina: CONFIGURAÇÃO

* **[Ticket: DRHMEURH-21882]** Melhorias na validação de dados do colaborador

Arquivo: Rh/Portais

* **[Ticket: DRHMEURH-22239]** Ajuste em arquivos de tradução

Arquivo: Rh/Portais

## 12.1.2602.159

### Rotina: CONFIGURAÇÃO

* **[Ticket: DRHMEURH-21882]** Inclusão de melhorias estruturais nos processos

Arquivo: Rh/Portais

## 12.1.2602.162

### Rotina: Sem Rotina Específica

* **[Ticket: DRHCONS-9188]** remoção de spinner no refresh

Arquivo: Rh/Portais

* **[Ticket: DRHCONS-9188]** ajuste para ocultar contador de refresh quando lista de simulações ou solicitações estiver vazia

Arquivo: Rh/Portais

* **[Ticket: DRHCONS-9188]** ocultado contador de refresh das telas com status diferente de 'em andamento'

Arquivo: Rh/Portais

## 12.1.2602.163

### Rotina: MEU RH - GESTÃO DE FÉRIAS EQUIPE

* **[Ticket: 27983136 / DRHHCM-17527]** Ajuste na validação da visualização de dados com hierarquia

Arquivos: RM.Rhu.Hierarquia.IService.dll; RM.Rhu.NovaHierarquia.Service.dll; RM.Fop.FuFerias.Data.dll; RM.Fop.Funcionario.Server.dll; RM.Rhu.Hierarquia.Service.dll

## 12.1.2602.170

### Rotina: INTEGRAÇÃO

* **[Ticket: 28082295 / DRHSSTPT-2215]** Adequação da mensagem de pessoa para integração com o Quírons a fim de adicionar os campos de função, seção e departamento.

Arquivo: RM.Rhu.Integracao.Server.dll

## 12.1.2602.171

### Rotina: CHEFES E SUP. - EXTERNOS

* **[Ticket: 27103069 / DRHHCM-17309]** Ajuste no consumo do dataserver de externo

Arquivo: RM.Rhu.Cadastros.Data.dll

## 12.1.2602.174

### Rotina: CONFIGURAÇÃO

* **[Ticket: 28274894 / DRHMEURH-22106]** Ajuste escala no layout do container

Arquivo: Rh/Portais

# TOTVS Gestão do Relacionamento com o Cliente

## 12.1.2602.101

### Rotina: ENVIO DE E-MAILS (CRM.321455)

* **[Ticket: 26464193 / TOPEXECONTROL01-30459]** Ajuste para que a discussão do atendimento seja atualizada automaticamente com o texto inserido pelo processo de envio de email sobre o atendimento

Arquivo: RM.CRM.Atendimento.Data.dll

## 12.1.2602.123

### Rotina: APROVAÇÃO/REPROVAÇÃO

* **[Ticket: 26507731 / TOPEXECONTROL01-30503]** Ajuste para que avanço de etapas no app de atendimentos criados numa coligada diferente da do atendente resposável possa ser aprovado normalmente.

Arquivo: RM.CRM.Api.dll

## 12.1.2602.125

### Rotina: ETAPAS

* **[Ticket: 24295130 / TOPEXECONTROL01-30140]** Ajuste ao buscar o status que é inserido no texto da discussão ao avançar etapa usando a fórmula AVANCARETAPAATENDIMENTO, em alguns casos, estava sendo usado a status do fluxo de outro tipo de atendimento

Arquivo: RM.CRM.TipoAtendimento.Data.dll

## 12.1.2602.126

### Rotina: DADOS PARA APROVAÇÃO

* **[Ticket: TOPEXECONTROL01-30428]** App Minhas Aprovações - Inclusão de arquivos anexos

Arquivos: RM.CRM.Api.dll; RM.CRM.Atendimento.Data.dll; RM.CRM.Facade.dll; RM.CRM.Atendimento.Intf.dll

## 12.1.2602.141

### Rotina: BANCO DE DADOS (BSO)

* **[Ticket: 27187269 / TOPEXECONTROL01-30755]** Ajuste ao editar horário dos apontamentos.

Arquivo: RM.CRM.Apontamento.Data.dll

## 12.1.2602.145

### Rotina: PARÂMETROS

* **[Ticket: 27239837 / TOPEXECONTROL01-30746]** Ajustes no apontamento automático para usar informações referentes a etapa e atendimento.

Arquivo: RM.CRM.Apontamento.Data.dll

## 12.1.2602.150

### Rotina: BANCO DE DADOS (BSO)

* **[Ticket: 25298062 / TOPEXECONTROL01-30147]** Ajuste quando a pesquisa de satisfação tivesse um parâmetro associado a um sentença sql (lookup) e tivesse a flag exigido marcada.

Arquivos: App\_Web\_crmpesquisasatisfacaowebform.ascx.a44db591.dll; RM.CRM.Lib.WebForm.dll

## 12.1.2602.151

### Rotina: PARÂMETROS

* **[Ticket: 27239837 / TOPEXECONTROL01-30746]** Ajustes no apontamento automático para respeitar as regras de criação e edição de atendimentos.

Arquivos: RM.CRM.Apontamento.Data.dll; RM.CRM.Atendimento.Form.dll

## 12.1.2602.164

### Rotina: CLASSIFICAÇÃO (CRM.321432)

* **[Ticket: TOPEXECONTROL01-31068]** Ajustes no cadastro de grupo de emails

Arquivo: RM.CRM.Cadastros.Form.dll

# TOTVS Gestão Financeira

## 12.1.2602.100

### Rotina: TRANSAÇÕES (CARTÃO DE CRÉDITO, CYBERSOURCE)

* **[Ticket: FINANCEIRO01-27325]** Tratamento do novo status Authorized\_Pending\_Review retornado pela GetNet

Arquivos: RM.Fin.Integracoes.Service.dll; RM.Fin.Parametros.Intf.dll

* **[Ticket: 26354797 / FINANCEIRO01-27287]** Ajustes na cast de data realizado em consulta sql para considerar apenas a parte de data sem tempo.

Arquivo: RM.Fin.Integracoes.Service.dll

## 12.1.2602.101

### Rotina: REGISTRO ONLINE

* **[Ticket: DRMGR-4583]** Melhoria no processo de cancelamento de registro online do banco b.Uni/Autbank

Arquivos: RM.Fin.Integracoes.Service.dll; RM.Fin.Integracoes.IService.dll; RM.Fin.Boleto.Service.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Criação do objeto de negócio para informe de rendimentos (lançamentos fiscais/financeiros referentes aos eventos 4010 e 4020 já autorizados, no período de um ano)

Arquivos: RM.Fin.Lan.IService.dll; RM.Fin.Lan.Service.dll

## 12.1.2602.102

### Rotina: BORDERÔ DE NEGATIVAÇÃO/TERCERIZÇÃO

* **[Ticket: 25863387 / FINANCEIRO01-27041]** Melhoria no processo de inclusão de bordero.

Arquivo: RM.Fin.Contrato.Data.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Seleção do código de receita nas consultas do informe de rendimentos da REINF

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Lan.IService.dll

## 12.1.2602.105

### Rotina: INTEGRAÇÃO PROTHEUS - BAIXA DE TÍTULO A RECEBER

* **[Ticket: 26035028 / DRMGR-4460]** Melhoria no processo de envio de data de compensação para Protheus, quando boleto possui mais de um lançamento

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.106

### Rotina: LANÇAMENTO - BAIXA - CRÉDITOS/DEVOLUÇÕES VINCULADOS

* **[Ticket: 26557055 / DRMGR-4596]** Ajuste no proceso de baixa em bases oracle

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.107

### Rotina: CONCILIAÇÃO BANCÁRIA - EFETUAR CONCILIAÇÃO AUTOMÁTICA

* **[Ticket: DRMGR-4578]** Processo de conciliação automática após importação

Arquivos: RM.Fin.Extrato.IService.dll; RM.Fin.Extrato.Service.dll; RM.Fin.Banco.Data.dll; RM.Fin.Banco.Service.dll; RM.Fin.Banco.Form.dll; RM.Fin.Banco.IService.dll; RM.Fin.Banco.Intf.dll

### Rotina: LANÇAMENTO - BAIXA - CRÉDITOS/DEVOLUÇÕES VINCULADOS

* **[Ticket: 26269790 / DRMGR-4562]** Ajuste na baixa com vínculo de devolução e recebimento de cheque de lançamento a receber

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: FINANCEIRO01-27349]** Cadastro Cliente/Fornecedor, adição de opção "Distrito Federal" no campo Orgão Público

Arquivo: RM.Fin.Lib.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Correção no agrupamento de lançamentos fiscais e financeiros, por cod receita e soma de valores quando há IR e outras retenções nos lançamentos

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.110

### Rotina: BAIXAS REALIZADAS - CONSULTA|EXCLUSÃO

* **[Ticket: DRMGR-4567]** Criação do serviço Para Retornar Informações (IBS & CBS) do Lançamento Baixado

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Lan.IService.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DRMGR-4400]** Melhora no processo de busca dos itens de planjeamento do fluxo de caixa

Arquivos: RM.Fin.PlanejamentoCaixa.Service.dll; RM.Fin.PlanejamentoCaixa.IService.dll

### Rotina: REGISTRO ONLINE

* **[Ticket: 26350024 / DRMGR-4650]** Ajuste no processo de Registro Online Santander V2 dos campos de data limite dos descontos

Arquivo: RM.Fin.Integracoes.Service.dll

## 12.1.2602.111

### Rotina: AJUSTE DE TRANSAÇÃO

* **[Ticket: 26778812 / DRMGR-4677]** Melhoria no processo de atualizar transação do boleto híbrido

Arquivo: RM.Fin.Integracoes.Service.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: 26723417 / DRMGR-4668]** Melhoria de desempenh na consulta de geração de REINF

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.112

### Rotina: BAIXAS REALIZADAS - ANEXO LANÇAMENTO

* **[Ticket: 26730612 / DRMGR-4660]** Ajuste na baixa de lançamentos vinculo de devolução

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: FSWBHPLATSEG-23291]** Ajuste no processo de inclusão de acordo financeiro.

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Lan.Data.dll

### Rotina: EFD PIS/COFINS - F100 (RM LI)

* **[Ticket: 24439616 / DRMGR-3893]** Melhoria no processo de busca dos extratos para geração da EFD.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO

* **[Ticket: FINANCEIRO01-27400]** Melhoria no processo de Acordo.

Arquivos: RM.Fin.Lan.Data.dll; RM.Fin.Lan.Service.dll

## 12.1.2602.113

### Rotina: Sem Rotina Específica

* **[Ticket: DMONTRIBRM-3132]** Valor duplicado - IRRF Retido

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 26424071 / DRMGR-4688]** Ajuste na baixa de lançamentos com tributos de retenção

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANÇAMENTO - CÁLCULO DO VALOR DAS RETENÇÕES

* **[Ticket: FINANCEIRO01-27361]** Criação da estrutura para chamada de serviços dos segmentos para obtenção dos dados tributários.

Arquivos: RM.Fin.Facade.dll; RM.Fin.Lan.IService.dll

## 12.1.2602.115

### Rotina: MÓDULO DE CAIXA 2.0

* **[Ticket: FINANCEIRO01-27428]** Melhorias para o recebimento com cartão da bandeira Baricompras e adquirente Vero no Módulo de Caixa.

Arquivos: RM.Fin.Lib.dll; RM.Fin.SessaoCaixa.Intf.dll

## 12.1.2602.116

### Rotina: BAIXAS REALIZADAS - ANEXO LANÇAMENTO

* **[Ticket: 25847654 / DRMGR-4351]** Melhoria no processo de tratamento de concorrência da baixa

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.117

### Rotina: Sem Rotina Específica

* **[Ticket: DRMGR-2699]** Melhoria no processo de leitura de arquivos OFX

Arquivos: RM.Fin.Banco.Intf.dll; RM.Fin.Banco.Data.dll

### Rotina: CONCILIAÇÃO BANCÁRIA - EFETUAR CONCILIAÇÃO AUTOMÁTICA

* **[Ticket: DRMGR-4578]** Melhoria no processo de conciliação e compensação automática após importação

Arquivos: RM.Fin.Banco.Service.dll; RM.Fin.Banco.Form.dll; RM.Fin.Banco.Data.dll

### Rotina: GERAR QRCODE

* **[Ticket: 26829546 / FINANCEIRO01-27420]** Melhoria para que seja incluído o log da sessão de caixa corretamente quando pagamento for com PIX.

Arquivos: RM.Fin.API.dll; RM.Fin.Lib.API.dll

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 26967443 / DRMGR-4739]** Ajuste na regra de valores de integração

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO

* **[Ticket: FINANCEIRO01-27452]** Correção no recebimento de borderos com mais de 1000 lançamentos

Arquivo: RM.Fin.Contrato.Service.dll

## 12.1.2602.118

### Rotina: REGISTRO ONLINE

* **[Ticket: DRMGR-4575]** Possibilidade da alteração da data de vencimento online Boleto Híbrido

Arquivos: RM.Fin.Boleto.Service.dll; RM.Fin.TechFin.Pagamento.IService.dll; RM.Fin.TechFin.Pagamento.Service.dll; RM.Fin.Lib.IService.dll

## 12.1.2602.120

### Rotina: CONCILIAÇÃO BANCÁRIA - EFETUAR CONCILIAÇÃO AUTOMÁTICA

* **[Ticket: DRMGR-4578]** Melhoria no processo de conciliação e compensação automática após importação

Arquivo: RM.Fin.Banco.Service.dll

## 12.1.2602.121

### Rotina: REGISTRO ONLINE

* **[Ticket: DRMGR-4729]** Melhoria na data de compesação do extrato quando ocorre o pagamento do boleto híbrido via código de barras

Arquivos: RM.Fin.Banco.Service.dll; RM.Fin.Lan.IService.dll; RM.Fin.Banco.Form.dll; RM.Fin.Integracoes.Service.dll; RM.Fin.Banco.Data.dll; RM.Fin.Lan.Service.dll

## 12.1.2602.124

### Rotina: BAIXAS REALIZADAS - CONSULTA|EXCLUSÃO

* **[Ticket: DRMGR-4690]** Mehoria na baixa de lançamentos a receber que possui IBS/CBS com demostrativo

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Lan.IService.dll

## 12.1.2602.125

### Rotina: BORDERÔ DE NEGATIVAÇÃO/TERCERIZÇÃO

* **[Ticket: 26403212 / FINANCEIRO01-27482]** Melhoria no processo de negativação.

Arquivo: RM.Fin.Contrato.Data.dll

### Rotina: GETNET/CIELO/REDE - CONCILIAÇÃO

* **[Ticket: FINANCEIRO01-27509]** Implementado versão 2 do download de arquivos skyline (cybersource), com funcionalidade de rententativa e time out configuravel. Melhorias visuais no formulário.

Arquivos: RM.Fin.Parametros.Intf.dll; RM.Fin.Lib.dll; RM.Fin.Integracoes.Data.dll; RM.Fin.Integracoes.Form.dll; RM.Fin.Parametros.Data.dll; RM.Fin.Parametros.Form.dll

### Rotina: LANÇAMENTO - CÁLCULO DE IRRF/INSS

* **[Ticket: FINANCEIRO01-27546]** Criação de Parametro Controle Tributario e Ajuste nova Lei de Dividendos.

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Parametros.Data.dll; RM.Fin.Parametros.Intf.dll; RM.Fin.Parametros.Form.dll

### Rotina: REGISTRO ONLINE

* **[Ticket: DRMGR-3755]** Melhoria no processo de boleto híbrido para garantir unicidade do registro do boleto.

Arquivos: RM.Fin.TechFin.Pagamento.IService.dll; RM.Fin.Integracoes.Service.dll; RM.Fin.Pagamento.Facade.dll

* **[Ticket: DRMGR-4781]** Melhoria no processo de gravação de dados do registro do boleto híbrido

Arquivos: RM.Fin.Boleto.Service.dll; RM.Fin.Integracoes.Service.dll

## 12.1.2602.127

### Rotina: CONTA/CAIXA - INCLUSÃO|ALTERAÇÃO|EXCLUSÃO

* **[Ticket: DRMGR-3090]** Ajustes realizados nos campos de saldo do form de inclusão de Conta/Caixa, corrigindo a navegação invertida via teclado

Arquivo: RM.Fin.ContaCaixa.Form.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: FINANCEIRO01-26779]** Ajuste testes TestFlow.

Arquivo: RM.Fin.Contrato.Data.dll

## 12.1.2602.128

### Rotina: CONTA/CAIXA - INCLUSÃO|ALTERAÇÃO|EXCLUSÃO

* **[Ticket: DRMGR-3090]** Melhoria na navegação por foco (Tab) no fom de criação de Conta/Caixa

Arquivo: RM.Fin.ContaCaixa.Form.dll

## 12.1.2602.129

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 26844472 / DRMGR-4709]** Criação de uma API para possibilitar criar o QRCodePix do boleto

Arquivos: RM.Fin.API.dll; RM.Fin.Integracoes.Intf.dll; RM.Fin.Integracoes.Data.dll; RM.Fin.Lib.API.dll

* **[Ticket: 26812378 / FINANCEIRO01-27545]** Melhoria no cadastro de Cliente/Fornecedor

Arquivos: RM.Fin.CliFor.Service.dll; RM.Fin.Facade.dll

### Rotina: REGISTRO ONLINE

* **[Ticket: 26897825 / DRMGR-4794]** Adiciona campos no JSON de registro online de boleto Sicredi

Arquivo: RM.Fin.Integracoes.Service.dll

## 12.1.2602.130

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 27173161 / DRMGR-4818]** Ajuste para cancelar o registro do boleto híbrido e atualizar o status CNAB do lançamento.

Arquivo: RM.Fin.Integracoes.Service.dll

* **[Ticket: 27173161 / DRMGR-4818]** Melhoria no processo de boleto híbrido para garantir unicidade do registro do boleto.

Arquivo: RM.Fin.Integracoes.Service.dll

### Rotina: LANÇAMENTO - ALTERAÇÃO

* **[Ticket: FINANCEIRO01-27697]** Ajustes alteração de lançamento para tributação de pessoa física.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: LANÇAMENTO - CÁLCULO DO VALOR DAS RETENÇÕES

* **[Ticket: FINANCEIRO01-27427]** Alterado serviço de cadastro de lançamentos para poder permitir a inclusão de tributos IBS e CBS para pessoa física.

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Lib.dll; RM.Fin.Banco.Data.dll

## 12.1.2602.131

### Rotina: GETNET/CIELO/REDE - CONCILIAÇÃO

* **[Ticket: FINANCEIRO01-27509]** Ajustado formato de nome dos arquivos de conciliação da cybersource.

Arquivo: RM.Fin.Integracoes.Data.dll

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 25936929 / DRMGR-4590]** Melhoria no processo de baixa de boleto parcial do TCGI através do retorno bancário

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.133

### Rotina: CONCILIAÇÃO BANCÁRIA - IMPORTAÇÃO DE ARQUIVO DE RECONCILIAÇÃO

* **[Ticket: DRMGR-4833]** Ajuste na importação em lote de arquivos de conciliação via recorrência

Arquivos: RM.Fin.Banco.Data.dll; RM.Fin.Banco.Form.dll

### Rotina: LANÇAMENTO - ALTERAÇÃO

* **[Ticket: FINANCEIRO01-27697]** Ajuste no serviço de alteração de lançamentos para não considerar alteração de tributos para lançamentos que não tenham tributos.

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.135

### Rotina: SERVIÇO DE CONTABILIZAÇÃO

* **[Ticket: 27165594 / DRMGR-4840]** Melhoria no processo de contabilização na baixa utilizando os novos tributos IBS e CBS para lançamentos a pagar

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.137

### Rotina: CONCILIAÇÃO BANCÁRIA - IMPORTAÇÃO OFX

* **[Ticket: 26975473 / DRMGR-4884]** Ajuste ao recuperar a Conta Caixa não encontrada no processo de conciliação em lote, pois alguns bancos como por exemplo o Banco Itaú, estão enviando o código da agencia bancaria na mesma tag da conta corrente

Arquivo: RM.Fin.Banco.Data.dll

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 27156560 / DRMGR-4813]** Otimização em tratamento de mensagem na baixa do lançamento gerado por acordo

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.139

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 27156560 / DRMGR-4813]** Otimização em tratamento de mensagem na baixa do lançamento gerado por acordo

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.141

### Rotina: ATUALIZAR TRANSAÇÃO BOLETO HÍBRIDO (BAIXA RM)

* **[Ticket: DRMGR-4955]** Melhoria na data de contabilização da baixa de um boleto híbrido quando sistema configurado para "Comp. Cheque"

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO

* **[Ticket: 27116434 / FINANCEIRO01-27544]** Melhorias no processo de retorno do pagamento para que o processo execute com sucesso.

Arquivo: RM.Fin.Contrato.Service.dll

## 12.1.2602.142

### Rotina: CONCILIAÇÃO BANCÁRIA - INCLUIR EXTRATO CORRESPONDENTE

* **[Ticket: 27480072 / DRMGR-4951]** Ajuste ao incluir extrato correspondente com numero de documento excedendo o limite do tamanho máximo parametrizado

Arquivo: RM.Fin.Extrato.Form.dll

## 12.1.2602.144

### Rotina: APLICAÇÃO FINANCEIRA - ENCERRAMENTOS DE PERÍODO

* **[Ticket: 25949044 / FINANCEIRO01-27479]** Ajuste na regra para definição se irá gerar ir come cotas.

Arquivo: RM.Fin.AplicacaoFinanceira.Server.dll

### Rotina: CRÉDITO/DÉBITO - BAIXA DE LANÇAMENTO VIA CARTÃO

* **[Ticket: FINANCEIRO01-27560]** Criação de formulário de cadastro de URL Segura para CyberSource V2

Arquivos: RM.Fin.Lib.dll; RM.Fin.dll; RM.Fin.Parametros.Form.dll; RM.Fin.Parametros.Intf.dll; RM.Fin.Parametros.Data.dll

* **[Ticket: FINANCEIRO01-27560]** Formulário de cadastro de URL Segura da CyberSource

Arquivo: RM.Fin.Parametros.Form.dll

## 12.1.2602.145

### Rotina: APURAÇÃO DE COMPETÊNCIA

* **[Ticket: TINPAD001-22282]** Melhoria no cálculo do liquido para cria opções para apuração de competência

Arquivo: RM.Fin.Lib.dll

### Rotina: CONCILIAÇÃO BANCÁRIA - INCLUIR EXTRATO CORRESPONDENTE

* **[Ticket: 27480072 / DRMGR-4951]** Ajuste ao incluir extrato correspondente com numero de documento excedendo o limite do tamanho máximo parametrizado.

Arquivo: RM.Fin.Extrato.Form.dll

### Rotina: GERAÇÃO DE FLUXO DE CAIXA

* **[Ticket: 23547628 / DRMGR-3557]** Melhoria no proceso de geração do fluxo de caixa

Arquivos: RM.Fin.PlanejamentoCaixa.Service.dll; RM.Fin.PlanejamentoCaixa.Form.dll; RM.Fin.Parametros.Intf.dll

### Rotina: INCLUSÃO

* **[Ticket: DMONTRIBRM-3953]** [MOV | TRIBUTOS] Adição do mapeamento de FK entre as tabelas TTRBMOV e FCFO

Arquivo: RM.Fin.CliFor.Service.dll

### Rotina: TRANSAÇÕES (RAAS, SHIPAY,PIX)

* **[Ticket: 27093618 / DRMGR-4780]** Correção de fuso horário em data de pagamento

Arquivo: RM.Fin.Integracoes.Service.dll

## 12.1.2602.150

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: DRMGR-4753]** Criação do serviço de busca de informações para NF-e de Débito do tipo Multa e Juros

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Lan.IService.dll

## 12.1.2602.151

### Rotina: BOLETO - INCLUSÃO DE LANÇAMENTO EM BOLETO

* **[Ticket: DRMGR-5020]** Ajuste para travar o cancelamento de remessa, para boletos registrados com boleto hibrido

Arquivo: RM.Fin.Boleto.Service.dll

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 27336205 / DRMGR-4970]** Ajuste ao inserir histório de alterações

Arquivos: RM.Fin.Entities.dll; RM.Fin.HistoricoLan.Service.dll

### Rotina: REGISTRAR BOLETO HÍBRIDO

* **[Ticket: DRMGR-5021]** Ajuste do boleto híbrido para impressão de boletos registrados

Arquivo: RM.Fin.Lan.Form.dll

* **[Ticket: 28238007 / DRMGR-5027]** Ajuste do status CNAB ao realizar o registro do boleto hibrido

Arquivo: RM.Fin.Integracoes.Service.dll

## 12.1.2602.152

### Rotina: ATUALIZAR TRANSAÇÃO BOLETO HÍBRIDO (BAIXA RM)

* **[Ticket: 28246446 / DRMGR-5029]** Melhoria no processo de integração com boleto híbrido

Arquivo: RM.Fin.Integracoes.Service.dll

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25955]** Disponibilizando serviço de inclusão de boleto multi-coligada

Arquivos: RM.Fin.Boleto.Service.dll; RM.Fin.Boleto.IService.dll

### Rotina: PROPOSTA

* **[Ticket: 27484812 / DRMGR-5035]** Melhoria no processo de exclusão de lançamentos com integração de boleto híbrido

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.153

### Rotina: REGISTRAR BOLETO HÍBRIDO

* **[Ticket: DRMGR-5033]** Melhoria no processo de registro de boleto híbrido referente ao valor do boleto parametrizado no convênio

Arquivos: RM.Fin.Integracoes.Service.dll; RM.Fin.Boleto.Service.dll; RM.Fin.Boleto.IService.dll

## 12.1.2602.154

### Rotina: FICHA FINANCEIRA

* **[Ticket: 26349534 / FINANCEIRO01-27713]** Ajuste na ficha financeira.

Arquivo: RM.Fin.HistoricoLan.Service.dll

## 12.1.2602.155

### Rotina: FICHA FINANCEIRA

* **[Ticket: FINANCEIRO01-27860]** Ajuste na ficha financeira.

Arquivo: RM.Fin.HistoricoLan.Service.dll

### Rotina: LANÇAMENTO - BAIXA - CANCELAMENTO

* **[Ticket: DRMGR-4755]** Novos bloqueios para cancelamento/estorno de baixa e lançamento

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Utils.Server.dll

## 12.1.2602.158

### Rotina: TRANSAÇÕES (CARTÃO DE CRÉDITO, CYBERSOURCE)

* **[Ticket: FINANCEIRO01-27743]** Novo fluxo de conciliação

Arquivo: RM.Fin.Integracoes.Data.dll

## 12.1.2602.163

### Rotina: CONTA/CAIXA - INCLUSÃO|ALTERAÇÃO|EXCLUSÃO

* **[Ticket: 28076327 / DRMGR-5059]** Ajuste na importação de Conciliação em Lote

Arquivos: RM.Fin.Banco.Intf.dll; RM.Fin.Banco.Data.dll

### Rotina: FICHA FINANCEIRA

* **[Ticket: 26349534 / FINANCEIRO01-27713]** Ajuste no calculo do valor liquido da ficha financeira.

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.165

### Rotina: CONCILIAÇÃO BANCÁRIA - IMPORTAÇÃO OFX

* **[Ticket: 26975473 / DRMGR-5091]** Ajuste na importação de Conciliação em Lote

Arquivo: RM.Fin.Banco.Data.dll

### Rotina: TRANSAÇÕES (CARTÃO DE CRÉDITO, CYBERSOURCE)

* **[Ticket: FINANCEIRO01-27769]** Consistência numero parcelas em boletos do educacional no pagamento pelo portal checkout

Arquivos: RM.Fin.Integracoes.Data.dll; RM.Fin.Integracoes.IService.dll; RM.Fin.Integracoes.Intf.dll; RM.Fin.Integracoes.Service.dll; RM.Fin.Integracoes.Form.dll

## 12.1.2602.170

### Rotina: ACORDO - ALTERAÇÃO|EXCLUSÃO

* **[Ticket: FINANCEIRO01-27943]** Melhoria no processo de acordo com inclusão ponto de plugin

Arquivos: RM.Fin.Customizacao.Intf.dll; RM.Fin.Lan.Service.dll

### Rotina: CONCILIAÇÃO BANCÁRIA - IMPORTAÇÃO DE ARQUIVO DE RECONCILIAÇÃO

* **[Ticket: DRMGR-5149]** Melhoria no tratamento do código de agência e conta para os cenários onde a informação chega vazia.

Arquivo: RM.Fin.Banco.Data.dll

### Rotina: CONCILIAÇÃO BANCÁRIA - INCLUIR EXTRATO CORRESPONDENTE

* **[Ticket: 27480072 / DRMGR-5118]** Melhoria no tratamento do campo Número do Documento para cenários onde o arquivo de conciliação conter esse campo com valores que extrapolam o limite parametrizado no sistema e a inclusão do Extrato Correspondente foi utilizada com a opção de informar os dados apenas uma vez.

Arquivo: RM.Fin.Banco.Form.dll

### Rotina: REGISTRO ONLINE

* **[Ticket: 28490854 / DRMGR-5171]** Melhoria mensagem do registro online do banco Daycoval

Arquivo: RM.Fin.Integracoes.Intf.dll

### Rotina: TRANSAÇÕES (CARTÃO DE CRÉDITO, CYBERSOURCE)

* **[Ticket: FINANCEIRO01-27950]** Desativação de opção de pagamento com dois cartões

Arquivo: RM.Fin.Parametros.Form.dll

## 12.1.2602.171

### Rotina: EXTRATO DE CAIXA - VISÃO

* **[Ticket: 28320758 / DRMGR-5090]** Ajuste para obteção do convênio vinculado a conta caixa escolhido pelo usuário do sistema

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: TRANSAÇÕES (CARTÃO DE CRÉDITO, CYBERSOURCE)

* **[Ticket: FINANCEIRO01-27975]** Melhoria no arredondamento da taxa de cartão.

Arquivo: RM.Fin.Lan.Service.dll

## 12.1.2602.174

### Rotina: POSIÇÃO FINANCEIRA

* **[Ticket: 28858426 / FINANCEIRO01-27981]** Evolução na visão da Posição Financeira para tratar os casos com e sem IBS e CBS informado no histórico de lançamentos.

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: RETORNO

* **[Ticket: 27668510 / FINANCEIRO01-27757]** Melhoria no processo de Retorno de Pagamento

Arquivo: RM.Fin.Contrato.Service.dll

## 12.1.2602.175

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 27406908 / FINANCEIRO01-27738]** Buscar Nome Fantasia de Coligada e informar no Merchant Descriptor

Arquivo: RM.Fin.Integracoes.Service.dll

### Rotina: EXTRATO DE CAIXA - VISÃO

* **[Ticket: 28320758 / DRMGR-5090]** Ajuste na escolha de convênio da conta caixa no processo de Extrato de Caixa

Arquivo: RM.Fin.Lan.Service.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: 28683784 / TINPAD001-22591]** Melhoria no processo de baixa do financeiro para identificar o tipo de baixa e uma fórmula pra identificar a origem do processo que chamou a fórmulaNova Função de Fórmula pra identificar a origem do processo do Liquido que chamou a fórmulaMelhoria no processo da apuração de competência para não chamar a validação da competência quando for baixa de borderô

Arquivos: RM.Fin.Lan.Service.dll; RM.Fin.Facade.dll; RM.Fin.Lib.dll; RM.Fin.Formula.dll

# TOTVS Gestão Fiscal

## 12.1.2602.100

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DMOTORFISCALRM-114]** Habilitado o envio de NFS-e quando o tomador não é identificado !

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: INCLUSÃO

* **[Ticket: 26229349 / DOCELETRONICOS-456]** Ajustes para chaves de acesso

Arquivo: RM.Fis.NFe.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2050 (RM LI)

* **[Ticket: DMOTORFISCALRM-246]** Ajuste no preenchimento do grupo de Emitente conforme Filial SCP

Arquivos: RM.Fis.NFe.Service.dll; RM.Fis.Contextos.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3252]** Ajuste do campo Número NBS do cadastro de Classificação Fiscal de Bens e Serviços

Arquivo: RM.Fis.Cadastros.Form.dll

* **[Ticket: DMONTRIBRM-3252]** Permite o processo de importação da tabela de CST/cClassTrib seja executado quando há somente licença do TOTVS Gestão de Compras, Estoque e Faturamento

Arquivo: RM.Fis.Cadastros.Form.dll

### Rotina: PARAMETRIZAÇÃO GERAL (RT)

* **[Ticket: 26526639 / DMOTORFISCALRM-244]** Cadastro de lançamentos fiscais - Situação tributária

Arquivos: RM.Fis.LancFiscal.Intf.dll; RM.Fis.LancFiscal.Form.dll

## 12.1.2602.101

### Rotina: CADASTRO - REGRAS TRIBUTÁRIAS (RT)

* **[Ticket: DMONTRIBRM-3229]** [Regras Tributárias - Cópia] Ajuste na cópia de RT entre coligadas para incluir a regra global "Classificação de Bens e Serviços" e impedir a cópia da regra "Empresa/Filial".

Arquivo: RM.Fis.NaturezaOper.Data.dll

### Rotina: CADASTROS - CONTABILIDADE - EVENTOS TRIBUTÁRIOS (RM LI)

* **[Ticket: 26423133 / DMONTRIBRM-3265]** Ajuste na busca a forma de tributação na cópia de tributação

Arquivo: RM.Fis.RegrasTributarias.Form.dll

### Rotina: IMG (ÍNDICE MATURIDADE DE GESTÃO)

* **[Ticket: DOCELETRONICOS-684]** Ajuste na geração da tag: cIndicadorOperacao ao enviar NFS-e utilizando o TPF.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DOCELETRONICOS-684]** Ajuste na Geração das Tags referêntes a Reforma, integração TSS

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-214]** Ajuste no cadastro de Tributo inserindo informações de Alíquota de Presuncao

Arquivos: RM.Fis.Tributo.Intf.dll; RM.Fis.Tributo.Data.dll; RM.Fis.Tributo.Form.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Criação do objeto de negócio para informe de rendimentos (lançamentos fiscais/financeiros referentes aos eventos 4010 e 4020 já autorizados, no período de um ano)

Arquivos: RM.Fis.RotinasFiscais.IService.dll; RM.Fis.Contextos.Service.dll; RM.Fis.NativeProvider.Service.dll; RM.Fis.Contextos.IService.dll; RM.Fis.Facade.dll; RM.Fis.RotinasFiscais.Api.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: TIPO DE MOVIMENTO

* **[Ticket: 26314138 / DRMMATERIAIS-8825]** Aumento do limite de caracteres da chave de acesso para 50.

Arquivo: RM.Fis.Lib.dll

## 12.1.2602.102

### Rotina: NF-E - ENVIO

* **[Ticket: DOCELETRONICOS-363]** Form para envio de evento de Prorrogação de Remessa para NF-e.

Arquivos: RM.Fis.NFe.Form.dll; RM.Fis.NFe.Intf.dll; RM.Fis.NFe.Data.dll; RM.Fis.Lib.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-774]** Geração do totTrib na NFSe Nacional para casos onde não há valores

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Seleção do código de receita nas consultas do informe de rendimentos da REINF

Arquivos: RM.Fis.NativeProvider.Service.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Contextos.Service.dll; RM.Fis.Contextos.IService.dll; RM.Fis.RotinasFiscais.IService.dll; RM.Fis.Facade.dll

## 12.1.2602.103

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: 23167754 / DMONTRIBRM-2965]** (CIAP) - Alteração no cálculo de valores para lançamentos com mais de um item

Arquivo: RM.Fis.NativeProvider.Service.dll

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Correção nos dados da filial para o cabeçalho do relatório

Arquivo: RM.Fis.NativeProvider.Service.dll

## 12.1.2602.104

### Rotina: INCLUSÃO

* **[Ticket: 26323442 / DRMMATERIAIS-8728]** Implementação de cache para ganho de performance.

Arquivos: RM.Fis.RotinasFiscais.Data.dll; RM.Fis.Facade.dll; RM.Fis.Parametros.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3252]** [SV | CIAP] Permite a geração de qualquer tipo de bem, e não apenas Imobilizado Individual

Arquivo: RM.Fis.NativeProvider.Service.dll

### Rotina: PARAMETRIZAÇÃO GERAL (RT)

* **[Ticket: DOCELETRONICOS-773]** Ajuste na Geração do Grupo PIS/COFINS nota Nacional

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Correção na data do fato gerador

Arquivos: RM.Fis.RotinasFiscais.IService.dll; RM.Fis.NativeProvider.Service.dll

## 12.1.2602.105

### Rotina: NF-E - CADASTRO

* **[Ticket: DOCELETRONICOS-523]** Ajuste no tamanho maximo do campo: PROTOCOLOAUTNFE

Arquivo: RM.Fis.NFe.Intf.dll

## 12.1.2602.106

### Rotina: NF-E - CADASTRO

* **[Ticket: DOCELETRONICOS-523]** Ajuste no tamanho maximo do campo: PROTOCOLOAUTNFE

Arquivos: RM.Doc.NFCom.Form.dll; RM.Doc.NFCom.Intf.dll

### Rotina: NFS-E - CADASTRO

* **[Ticket: 26058387 / DOCELETRONICOS-587]** NFSe Nacional - ajuste para busca de código de serviço

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.107

### Rotina: CADASTROS - NATUREZA DE OPERAÇÃO (RM LI)

* **[Ticket: DMONTRIBRM-3345]** [Cópia de CFOP - Aceleradores com IA] Adicionada lógica para setar o exercício fiscal com base na data corrente quando o contexto estiver vazio, especifico para cópias originadas pelos Aceleradores com IA.

Arquivo: RM.Fis.NaturezaOper.Data.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: 26641703 / DOCELETRONICOS-844]** NFSe Nacional - ajuste para endereço exterior

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Correção no agrupamento de lançamentos fiscais e financeiros, por cod receita e soma de valores quando há IR e outras retenções nos lançamentos

Arquivos: RM.Fis.RotinasFiscais.IService.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.NativeProvider.Service.dll

## 12.1.2602.108

### Rotina: NFS-E - ENVIO

* **[Ticket: DMOTORFISCALRM-366]** Ajuste no cadastro de Tributo inserindo informações de Alíquota de Presuncao

Arquivos: RM.Fis.Cadastros.Form.dll; RM.Fis.Cadastros.Data.dll; RM.Fis.Cadastros.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - MUNICIPAIS (RM LI)

* **[Ticket: 26435851 / DMONTRIBRM-3359]** DESBH - Campo 8 - AJuste para tipo de recolhimento invalido para o motivo de não retenção informado

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.109

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: DMONTRIBRM-3182]** [SV | REINF] Passa a agrupar os lançamentos de origem por cod receita e nat rendimento, quando for gerar o informe de rendimentos

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.110

### Rotina: SPED FISCAL - D100 (RM LI)

* **[Ticket: 26178352 / DMONTRIBRM-3300]** [SPED FISCAL] Não gera valor de ICMS para o registro D730 quando o tipo de ICMS é "Outros"

Arquivo: RM.Fis.Sped.Server.dll

## 12.1.2602.111

### Rotina: NFCOM (RT)

* **[Ticket: 26507087 / DOCELETRONICOS-892]** NFCOM - Gerar campo vTotDFe

Arquivo: RM.Doc.NFCom.Service.dll

### Rotina: NF-E - ENVIO

* **[Ticket: DOCELETRONICOS-365]** Criação do XML do evento de prorrogação de remessa

Arquivos: RM.Fis.NFe.Intf.dll; RM.Fis.NFe.Data.dll; RM.Fis.NFe.Form.dll

* **[Ticket: DOCELETRONICOS-365]** Ajuste do campo quantidade prorrogada no envio do evento de prorrogação de remessa

Arquivos: RM.Fis.NFe.Form.dll; RM.Fis.NFe.Intf.dll

* **[Ticket: DOCELETRONICOS-770]** Consulta dos eventos de prorrogação de remessa.

Arquivos: RM.Fis.NFe.Service.dll; RM.Fis.NFe.Form.dll; RM.Fis.NFe.Data.dll; RM.Fis.NFe.IService.dll

### Rotina: NFS-E - CONSULTA AUTORIZAÇÃO/CANCELAMENTO

* **[Ticket: DOCELETRONICOS-748]** Inclusão de possibilidade de informar um valor para a tag cObra a partir de um campo complementar do Projeto, quando não for estado do Rio de Janeiro.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-971]** Ajuste nos totatlizadores do IBS e CBS.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: 26374436 / DMONTRIBRM-3502]** [Informe de Rendimentos REINF] Adicionada variavel para Valor do IRRFIMPORT e ordenação po data

Arquivos: RM.Fis.RotinasFiscais.IService.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.NativeProvider.Service.dll

## 12.1.2602.112

### Rotina: NFS-E (RT)

* **[Ticket: DOCELETRONICOS-617]** Incluir dados de imóvel no xml único

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DOCELETRONICOS-912]** Gerar o grupo Dest (Destinatário) para o layout unico do TSS.

Arquivo: RM.Fis.NFe.Service.dll

## 12.1.2602.113

### Rotina: NFS-E - ENVIO

* **[Ticket: DMOTORFISCALRM-364]** Alterado NFS-e Modelo Nacional a tag tpEnteGov (Tipo de Ente Governamental)

Arquivo: RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DMOTORFISCALRM-364]** NFS-e Modelo Nacional – Gerar a tag tpEnteGov (Tipo de Ente Governamental)

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS-E (RT)

* **[Ticket: DOCELETRONICOS-912]** Gerar o grupo Dest (Destinatário) para o layout unico do TSS.

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3009]** [EFD 1400 - Parâmetro de Processo] Adicionado novo parametro de processo para contemplar quais CFOPs devem ser consideradas no calculo da geração do registro 1400 anual da EFD

Arquivos: RM.Fis.ParProcessos.Intf.dll; RM.Fis.ParProcessos.Server.dll; RM.Fis.ParProcessos.Data.dll; RM.Fis.Lib.dll; RM.Fis.ParProcessos.Form.dll

## 12.1.2602.114

### Rotina: Sem Rotina Específica

* **[Ticket: DMONTRIBRM-3132]** [SV | REINF] Correção na seleção das informações da fonte pagadora

Arquivo: RM.Fis.NativeProvider.Service.dll

### Rotina: NF-E - IMPORTAÇÃO DE DANFE

* **[Ticket: DOCELETRONICOS-482]** Alterações internas sem mudanças de comportamento

Arquivos: RM.Fis.Parametros.Data.dll; RM.Fis.Customizacao.Intf.dll; RM.Fis.PeriodoFiscal.IService.dll; RM.Fis.IService.dll

* **[Ticket: DOCELETRONICOS-482]** Importação de NFe via xml - Ajuste na mensagem de inconsistência do processo não fracionado

Arquivo: RM.Doc.MonitorArquivos.Data.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DMOTORFISCALRM-362]** Alteração no XML de NFS-e Nacional, inserindo a TAG TpOper.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DMOTORFISCALRM-364]** NFS-e Modelo Nacional – Tag tpEnteGov (Tipo de Ente Governamental)

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.116

### Rotina: CADASTROS - PROCESSOS - CÓPIAS (RM LI)

* **[Ticket: DMONTRIBRM-3228]** Inclusão da Importação da tabela de CST /cClassTrib via arquivo JSON

Arquivos: RM.Fis.Cadastros.Services.dll; RM.Fis.Cadastros.Intf.dll; RM.Fis.NaturezaOper.Form.dll; RM.Fis.Cadastros.Data.dll; RM.Fis.Cadastros.Form.dll; RM.Fis.Cadastros.IService.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-936]** NFS-e - Gerar a tag "regApTribSN" para o TSS no layot unico.

Arquivos: RM.Fis.Lib.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3591]** [SPED Fiscal - Parametrização de Rotinas] Adição do campo para geração do registro 1400 anual e Código do item IPM

Arquivo: RM.Fis.Sped.Form.dll

## 12.1.2602.117

### Rotina: NF-E - CONSULTAR EVENTO

* **[Ticket: 26955944 / DOCELETRONICOS-1116]** Ajsute no evento de prorrogação de remessa quanto a produto global.

Arquivo: RM.Fis.NFe.Data.dll

### Rotina: NF-E - ENVIO

* **[Ticket: DOCELETRONICOS-884]** Evento de cancelamento de prorrogação de remessa e testes unitários

Arquivos: RM.Fis.NFe.Form.dll; RM.Fis.Lib.dll; RM.Fis.NFe.Service.dll; RM.Fis.NFe.Data.dll; RM.Fis.NFe.IService.dll; RM.Fis.NFe.Intf.dll

### Rotina: NOTA FISCAL DE COMUNICAÇÃO ELETRÔNICA

* **[Ticket: 26654357 / DOCELETRONICOS-951]** Implementação do Processo Substituição da NFcom (Envio/Consulta)

Arquivos: RM.Doc.NFCom.Intf.dll; RM.Doc.NFCom.IService.dll; RM.Doc.NFCom.Service.dll

* **[Ticket: DOCELETRONICOS-1117]** DANFECOM - melhoria para validação de permissão

Arquivo: RM.Doc.NFCom.Form.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-3107]** Bugfix (Reinf) - Defensivo para os campos INDPRESTSRV e TPPRJ

Arquivo: RM.Fis.Contextos.Service.dll

* **[Ticket: DMONTRIBRM-3107]** (Reinf) - Alteração nos campo TTPRJ e INDPRESTSRV

Arquivo: RM.Fis.Contextos.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2020 (RM LI)

* **[Ticket: DMONTRIBRM-3646]** [NFe] Geração do grupo Guia de Trânsito - agropecuario

Arquivos: RM.Fis.NFe.Service.dll; RM.Fis.NFe.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3010]** [EFD 1400 - Parâmetro de Processo] Adicionado processo de inclusão de múltiplas naturezas para contemplar quais CFOPs devem ser consideradas no calculo da geração do registro 1400 anual da EFD

Arquivos: RM.Fis.Contextos.IService.dll; RM.Fis.ParProcessos.Data.dll; RM.Fis.ParProcessos.Intf.dll; RM.Fis.ParProcessos.Form.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADA/SAÍDA (RM LI)

* **[Ticket: 26720290 / DMOTORFISCALRM-439]** Ajustes no componente lookup do cadastro de CEI

Arquivo: RM.Fis.LancFiscal.Form.dll

### Rotina: TRANSMISSÃO - NFSE

* **[Ticket: 25642118 / DOCELETRONICOS-1105]** Ajuste no Envio da NFS-e quando e criada uma uma Nova Filial (Regime Especial de Tributação)

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.119

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-216]** Criando campos da majoração do lucro presumido no periodo de apuração.

Arquivos: RM.Fis.ApuracaoTrb.Data.dll; RM.Fis.ApuracaoTrb.IService.dll; RM.Fis.ApuracaoTrb.Service.dll; RM.Fis.ApuracaoTrb.Form.dll; RM.Fis.ApuracaoTrb.Intf.dll

* **[Ticket: DMOTORFISCALRM-216]** Alterando TabIndex, formatação de botoes e label do limite disponivel do periodo.

Arquivos: RM.Fis.ApuracaoTrb.Form.dll; RM.Fis.ApuracaoTrb.Intf.dll

* **[Ticket: DMOTORFISCALRM-216]** Ajuste no defensivo, visibilidade do gp da majoracao

Arquivo: RM.Fis.ApuracaoTrb.Form.dll

## 12.1.2602.120

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: 26999093 / DMONTRIBRM-3676]** Bugfix (Reinf) - Duplicidade no informe de rendimentos

Arquivo: RM.Fis.Contextos.Service.dll

## 12.1.2602.123

### Rotina: CADASTROS - FILIAL (RM LI)

* **[Ticket: DOCELETRONICOS-1171]** Correção de alguns warnings

Arquivos: RM.Fis.NFe.Intf.dll; RM.Fis.NFe.IService.dll; RM.Fis.Tributo.IService.dll; RM.Fis.Contextos.Service.dll; RM.Fis.Cadastros.IService.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DOCELETRONICOS-1164]** NFSe - grupo do benefício municipal

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Utils.Server.dll; RM.Fis.Utils.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3012]** Sped Fiscal - Inclusão da Geração do Registro 1400 Anual - Não gerar registro para valor zero

Arquivos: RM.Fis.Lib.dll; RM.Fis.Sped.Server.dll

## 12.1.2602.124

### Rotina: CADASTRO - TRIBUTOS IBS, CBC E IS (RT)

* **[Ticket: DMOTORFISCALRM-488]** Tags TipoOperacao, Tipo de ente Governamental e Percentual Redutor aplicadas nos layout Unico TSS e TPF

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DMOTORFISCALRM-488]** Tags TipoOperacao, Tipo de ente Governamental e Percentual Redutor aplicadas nos layout Unico TSS e TPF - Melhorias

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DOCELETRONICOS-1164]** NFSe - geração do grupo BM

Arquivos: RM.Fis.Enderecos.Form.dll; RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.Enderecos.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: NF-E - ENVIO

* **[Ticket: 21731430 / DOCELETRONICOS-647]** Considerar CFOP interestadual no preenchimento do percentual de diferimento

Arquivo: RM.Fis.Tributo.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DMOTORFISCALRM-363]** Integração de TAG no xml para Grupos de NFS-e referencias;

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

* **[Ticket: DOCELETRONICOS-935]** NFSe - geração da tag regApTribSN no layout nacional

Arquivo: RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DOCELETRONICOS-994]** Grupo PIS e COFINS no Layout único do TSS

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DOCELETRONICOS-1151]** Implementação da Tag Imunidade layout TSS

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

* **[Ticket: DMONTRIBRM-3012]** Sped Fiscal - Inclusão da Geração do Registro 1400 Anual - Não gerar registro para valor zero

Arquivo: RM.Fis.Sped.Server.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-217]** Evolução: implementado calculo dos valores do IRPJ/CSLL para lucro presumido com majoração no encerramento do periodo.

Arquivos: RM.Fis.RegrasTributarias.Data.dll; RM.Fis.RegrasTributarias.Form.dll; RM.Fis.RegrasTributarias.Intf.dll; RM.Fis.RegrasTributarias.Service.dll; RM.Fis.ApuracaoTrb.Service.dll; RM.Fis.RegrasTributarias.IService.dll

### Rotina: PARAMETRIZAÇÃO GERAL (RT)

* **[Ticket: DMOTORFISCALRM-489]** Criação de TAG de NFSe Referenciadas para as notas Layout TSS

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

## 12.1.2602.125

### Rotina: NF-E - ENVIO

* **[Ticket: DMONTRIBRM-3716]** Implementação do grupo gCompraGov à NFe

Arquivos: RM.Fis.NFe.Service.dll; RM.Fis.NFe.Intf.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: 26106509 / DOCELETRONICOS-752]** NFSe - considerar se o estado não é nacional para a geração do grupo comExt

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADA/SAÍDA (RM LI)

* **[Ticket: 26859550 / DMOTORFISCALRM-477]** Resolução do não salvamento da aliquota e valor de retanção na memória de cálculo

Arquivo: RM.Fis.LancFiscal.Data.dll

### Rotina: PARAMETRIZAÇÃO GERAL (RT)

* **[Ticket: DOCELETRONICOS-956]** Ajustes para NFSE NT007 para TPF

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: TOTVS INTELIGÊNCIA TRIBUTÁRIA

* **[Ticket: DMONTRIBRM-3585]** Melhoria de segurança

Arquivo: Fis/monitor-tributario-front

## 12.1.2602.126

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1249]** Geração do grupo totTrib para o TSS

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 26766929 / DRMMATERIAIS-9320]** Ajuste no cache de parâmetros movimento

Arquivo: RM.Fis.Facade.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-478]** Evolução: Ajustado simulação do evento tributário para exibir log se a empresa não ultrapassar o limite anual, mas teve majoração em algum trimestre, o sistema mostra o valor recolhido a mais, permitindo que o usuário solicite restituição ou compensação, conforme a legislação. O cálculo e a visualização foram ajustados para garantir transparência e facilitar o acompanhamento dessas regras.

Arquivos: RM.Fis.ApuracaoTrb.Service.dll; RM.Fis.RegrasTributarias.Service.dll

### Rotina: TOTVS INTELIGÊNCIA TRIBUTÁRIA

* **[Ticket: DMONTRIBRM-3585]** Melhoria de segurança

Arquivo: Fis/monitor-tributario-front

## 12.1.2602.127

### Rotina: CADASTRO - REGRAS TRIBUTÁRIAS (RT)

* **[Ticket: DMONTRIBRM-3783]** Remove a abertura automática do TOTVS Inteligência Tributária

Arquivo: RM.Fis.dll

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1249]** Geração do grupo totTrib para o TSS

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: FATURAMENTO/RECEBIMENTO

* **[Ticket: DRMMATERIAIS-9378]** Implementação de verificação de parametro "TAMANHO\_FRACIONAMENTO" para definir tamanho da fração na geração de lançamentos com consulta à prefeitura

Arquivos: RM.Fis.RotinasFiscais.IService.dll; RM.Fis.RotinasFiscais.Data.dll

### Rotina: NF-E - ENVIO

* **[Ticket: DMONTRIBRM-3717]** NF-e -Geração da tag tpOperGov - Tipo de Operação com Entes Governamentais

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: DMONTRIBRM-3722]** Grupo de tributo da NFe quando há compras governamentais

Arquivos: RM.Fis.NFe.Intf.dll; RM.Fis.NFe.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3725]** Fix - Informação do órgão público propagada a partir das informações do destinatário da nota

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: PARAMETRIZAÇÃO GERAL (RT)

* **[Ticket: DMOTORFISCALRM-489]** Geração de Grupo de NFSe Referenciadas para TPF.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: 27037466 / DMONTRIBRM-3723]** [Informe de Rendimentos] Ajuste no Codigo da Receita para pegar o Codigo Oficial e não a chave.

Arquivo: RM.Fis.NativeProvider.Service.dll

## 12.1.2602.128

### Rotina: NF-E - ENVIO

* **[Ticket: DMONTRIBRM-3717]** NF-e -Geração da tag tpOperGov - Tipo de Operação com Entes Governamentais

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: 27037466 / DMONTRIBRM-3723]** [Informe de Rendimentos] Ajuste no Codigo da Receita para pegar o Codigo Oficial e não a chave.

Arquivo: RM.Fis.NativeProvider.Service.dll

## 12.1.2602.129

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1298]** NFSe - ajustes para grupo piscofins TSS

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: 27115751 / DOCELETRONICOS-1218]** ENVIO DE NOTAS COM DIFERENTES LOCALIDADES

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.130

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1289]** RT: NFS-e Layout TSS - Atualizar Grupo identificacao

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Cadastros.Services.dll

* **[Ticket: DOCELETRONICOS-1291]** NFS-e Layout TSS - Grupo Prestador

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DOCELETRONICOS-1298]** NFSe - ajuste para o grupo totTrib para TSS

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-935]** NFSe - geração da tag regApTribSN no layout nacional

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS-E (RT)

* **[Ticket: DOCELETRONICOS-1235]** Implementação para gerar o Grupo de IBS/CBS quando for Bolsa 100%

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3725]** NF-e -Geração da tag tpOperGov - Tipo de Operação com Entes Governamentais

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.131

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1387]** Implementação do CNAE a partir do cadastro de tributos do produto por municipio

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Cadastros.Form.dll; RM.Fis.Cadastros.Intf.dll; RM.Fis.RotinasFiscais.Intf.dll

* **[Ticket: DOCELETRONICOS-1292]** RT: NFS-e Layout TSS - Grupo Tomador

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: NFS-E - SUBSTITUIR

* **[Ticket: 26949990 / DOCELETRONICOS-1143]** Padronização da informação exibida no log de processos, de acordo com status retornado da NFS-e.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3725]** NF-e -Geração da tag tpOperGov - Tipo de Operação com Entes Governamentais

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.132

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1387]** Implementação do CNAE a partir do cadastro de tributos do produto por municipio

Arquivos: RM.Fis.Cadastros.Intf.dll; RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3725]** NF-e - Ajuste referência de objeto

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: DMONTRIBRM-3725]** Inclue o grupo de redução de alíquota quando há compra governamental, mesmo quando não há redução de alíquota no CST / cClassTrib

Arquivo: RM.Fis.NFe.Service.dll

## 12.1.2602.133

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1293]** NFSe - geração de novas tags para o grupo serviço TSS

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DOCELETRONICOS-1296]** NFSe - geração do grupo piscofinsApu para o TSS

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: NFS-E (RT)

* **[Ticket: DOCELETRONICOS-1237]** Implementação para gerar o Grupo de IBS/CBS quando for Bolsa 100%

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3725]** NF-e - Grupo Compra Gevernamental

Arquivo: RM.Fis.NFe.Service.dll

## 12.1.2602.134

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1311]** Alteração para enviar o numeroArt e o CIB no XML do TSS

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: NFS-E - CONSULTA AUTORIZAÇÃO/CANCELAMENTO

* **[Ticket: 27327411 / DOCELETRONICOS-1455]** Implementação da tag pDR (Percentual de dedução) do grupo vDedRed para NFS-e layout Nacional.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.135

### Rotina: CADASTROS - PROCESSOS - CÓPIAS (RM LI)

* **[Ticket: DMONTRIBRM-3747]** Muda o estilo do dropdown para lista do evento e origem e mostra o código da natureza ao invés do ID na tela de filtro de eventos da REINF

Arquivo: RM.Fis.ParProcessos.Form.dll

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1297]** RT: NFS-e Layout TSS - Grupo valores

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO IRPJ E CSLL (RM LI)

* **[Ticket: DMOTORFISCALRM-216]** Corrigindo posição dos campos de receitas no CSLL

Arquivo: RM.Fis.ApuracaoTrb.Form.dll

## 12.1.2602.136

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3707]** Inclusão do campo CEBAS

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.Filial.Intf.dll; RM.Fis.Filial.Data.dll; RM.Fis.Lib.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Filial.Form.dll

* **[Ticket: DMONTRIBRM-3707]** Criação do Item "Retorno às atividades de empresas inativas"

Arquivo: RM.Fis.Lib.dll

### Rotina: SCHEMA - NFSE

* **[Ticket: 27241674 / DOCELETRONICOS-1499]** Liberação do Cadastro de Rotinas do Fiscal para clientes com Licença Quarteto

Arquivo: RM.Fis.Cadastros.Form.dll

## 12.1.2602.137

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: 26975113 / DOCELETRONICOS-1464]** NFSe Nacional - ajuste na geração da tag vServ

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DMOTORFISCALRM-383]** Escrituração - % redução aliquota compra governamental

Arquivos: RM.Fis.Tributo.IService.dll; RM.Fis.Tributo.Service.dll

* **[Ticket: DOCELETRONICOS-937]** NFSe - preenchimento do campo regimeTribSN para o TPF

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: NOTA FISCAL DE COMUNICAÇÃO ELETRÔNICA

* **[Ticket: DMONTRIBRM-3841]** Criação dos grupos gCompraGov e gTribCompraGov

Arquivos: RM.Doc.Utils.Intf.dll; RM.Doc.NFCom.Service.dll; RM.Doc.NFCom.Intf.dll; RM.Doc.Utils.Service.dll; RM.Doc.NFCom.IService.dll

## 12.1.2602.139

### Rotina: OBJETOS DE NEGÓCIO - SMART VIEW

* **[Ticket: DMOTORFISCALRM-514]** Apuração CBS/IBS - Objeto de negócio de lançamentos CBS/IBS

Arquivo: RM.Fis.NativeProvider.Service.dll

## 12.1.2602.140

### Rotina: EMISSÃO

* **[Ticket: DOCELETRONICOS-1416]** Ajuste na atribuição do CNAE no Grupo de Item do Serviço Modelos TSS e TPF

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.141

### Rotina: Sem Rotina Específica

* **[Ticket: 27242890 / DOCELETRONICOS-1422]** NFSe Nacional - ajuste para tag dhEmi

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DOCELETRONICOS-546]** Gerar xml da NF-e - Produtos AGRO NF-e – v.1.06

Arquivos: RM.Fis.NFe.Service.dll; RM.Fis.NFe.Intf.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-883]** Gerar xml da NF-e - Produtos AGRO NF-e – v.1.06

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: OBJETOS GERENCIAIS - SMART VIEW

* **[Ticket: 27315479 / DMONTRIBRM-3885]** [SV | APURAÇÃO ICMS] Correção nos valores de crédito

Arquivo: RM.Fis.NativeProvider.Service.dll

## 12.1.2602.142

### Rotina: NFS-E (RT)

* **[Ticket: 27482859 / DOCELETRONICOS-1600]** Ajuste nos campos de código de município do grupo destinatário da NFS-e

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.144

### Rotina: NF-E (RT)

* **[Ticket: 27225987 / DOCELETRONICOS-1496]** Considerar a tabela de CST / cClassTrib para gerar o grupo de IBSCBS no envio de NF-e.

Arquivo: RM.Fis.NFe.Service.dll

* **[Ticket: 27467906 / DOCELETRONICOS-1609]** Ajuste para não ocorrer duplicidade dos tributos IBS/CBS ao gerar o Grupo de Compra Governamental

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3959]** Implementação da tela de Destinatários das Deduções ECF

Arquivos: RM.Fis.RegrasTributarias.Form.dll; RM.Fis.Menu.dll; RM.Fis.RegrasTributarias.Intf.dll; RM.Fis.RegrasTributarias.Data.dll

## 12.1.2602.145

### Rotina: NF-E - CONSULTA AUTORIZAÇÃO

* **[Ticket: 27932842 / DOCELETRONICOS-1655]** Mudança de Status NFE

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - SPED FISCAL (RM LI)

* **[Ticket: DMONTRIBRM-3708]** [ECF - Y730] - Adição do registro Y730

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: UTILITÁRIOS - DUPLICAÇÕES (RM LI)

* **[Ticket: DMOTORFISCALRM-593]** Ajuste no processo de cópia para base aceleradora onde seleciona mais de uma coligada de destino, pois o cadastro e global.

Arquivos: RM.Fis.Cadastros.Data.dll; RM.Fis.Cadastros.Form.dll

## 12.1.2602.146

### Rotina: ESCRITURAÇÃO (RM LI)

* **[Ticket: DMONTRIBRM-3956]** REINF - 4020 COSIRF passa a considerar o código da receita na geração das tags

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

## 12.1.2602.147

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1554]** Escrituração de movimentos com NFS-e - Simplificar NFS-e

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

## 12.1.2602.148

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1665]** Criação de parametros para permitir a escolha entre a perspectiva de incidencia ou emitente, referente aos codigos de tributação do serviço.

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

## 12.1.2602.149

### Rotina: ESCRITURAÇÃO (RM LI)

* **[Ticket: DMOTORFISCALRM-643]** Foi realizada uma melhoria no processo de estorno/exclusão de Lançamentos Fiscais com foco em reduzir os travamentos de banco de dados (deadlocks) observados durante o processamento de lotes com grande volume de registros.

Arquivo: RM.Fis.LancFiscal.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1658]** Ajuste do sub grupo: pTotTrib do grupo: tcTotTrib para gerar quando tipo de movimento estiver parametrizado para "lei da transparencia". para o layout TSS.

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.150

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1554]** Escrituração de movimentos com NFS-e - Simplificar NFS-e

Arquivo: RM.Fis.EscrituracaoFiscal.Service.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADA/SAÍDA (RM LI)

* **[Ticket: DMOTORFISCALRM-599]** Criação de Campos no Lançamento Fiscal com defensivo.

Arquivos: RM.Fis.LancFiscal.Form.dll; RM.Fis.LancFiscal.Data.dll; RM.Fis.LancFiscal.IService.dll; RM.Fis.LancFiscal.Intf.dll; RM.Fis.LancFiscal.Service.dll

## 12.1.2602.151

### Rotina: ESCRITURAÇÃO (RM LI)

* **[Ticket: DMOTORFISCALRM-641]** Estorno escrituração - Melhoria performance

Arquivos: RM.Fis.EscrituracaoFiscal.Service.dll; RM.Fis.LancFiscal.Service.dll

### Rotina: NFTS

* **[Ticket: 27117575 / DOCELETRONICOS-1654]** Inserido na NFTS Webservice a flexibilidade que havia na rotina NFTS pelo gerador de saídas. Caso não possua modelo de documento preenchido o sistema se comporta como antes

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADA/SAÍDA (RM LI)

* **[Ticket: DMOTORFISCALRM-599]** Ajuste nos valores do ComboBox

Arquivo: RM.Fis.LancFiscal.Form.dll

* **[Ticket: DMOTORFISCALRM-599]** Ajuste em evento de troca de informação nos combos box

Arquivo: RM.Fis.LancFiscal.Form.dll

### Rotina: TOTVS INTELIGÊNCIA TRIBUTÁRIA

* **[Ticket: DMONTRIBRM-3854]** Melhoria de segurança

Arquivo: Fis/monitor-tributario-front

* **[Ticket: DMONTRIBRM-3854]** Ampliançao da cobertura de teste

Arquivo: Fis/monitor-tributario-front

* **[Ticket: DMONTRIBRM-3854]** Atualização do angular

Arquivo: Fis/monitor-tributario-front

* **[Ticket: DMONTRIBRM-3854]** Correção de estilo css

Arquivo: Fis/monitor-tributario-front

## 12.1.2602.152

### Rotina: CADASTRO - TRIBUTOS IBS, CBC E IS (RT)

* **[Ticket: DMOTORFISCALRM-690]** Revisão do cálculo da vTribCBS em Operações de Compra Governamental com Valor Diferido

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NFC-E - ENVIO

* **[Ticket: 27465359 / DOCELETRONICOS-1751]** Ajuste na montagem do grupo Compra Gov para tomador não identificado.

Arquivo: RM.Fis.NFe.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1665]** Ajuste na regra de visibilidade dos campos da perspectiva do emitente.

Arquivo: RM.Fis.Cadastros.Form.dll

* **[Ticket: DOCELETRONICOS-1665]** Criação de parametros para permitir a escolha entre a perspectiva de incidencia ou emitente, referente aos codigos de tributação do serviço.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Enderecos.Form.dll; RM.Fis.Cadastros.Intf.dll; RM.Fis.Cadastros.Form.dll; RM.Fis.Enderecos.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF (RM LI)

* **[Ticket: DMONTRIBRM-3957]** [REINF] Múltiplos beneficiários COSIRF

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Contextos.Service.dll; RM.Fis.Contextos.IService.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADA/SAÍDA (RM LI)

* **[Ticket: DMOTORFISCALRM-599]** Ajuste em ComboBox com regras de negocio.

Arquivo: RM.Fis.LancFiscal.Form.dll

### Rotina: RELATÓRIOS FISCAIS (RM LI)

* **[Ticket: 27342669 / DMONTRIBRM-4025]** [MENU | RELATÓRIOS] Chama a visão web para o menu de relatórios fiscais. Não filtra mais apenas por recursos do módulo fiscal

Arquivos: RM.Fis.Relatorios.Form.dll; RM.Fis.Menu.dll

## 12.1.2602.153

### Rotina: INCLUSÃO MOVIMENTO A PARTIR DE XML

* **[Ticket: 26972762 / DOCELETRONICOS-1335]** Ajustes para tradução de XML

Arquivos: RM.Fis.NaturezaOper.IService.dll; RM.Fis.Enderecos.Service.dll; RM.Fis.Tributo.Service.dll; RM.Fis.NaturezaOper.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1667]** Tributos por Município - novos campos para a atualização em lote

Arquivos: RM.Fis.Cadastros.Form.dll; RM.Fis.Cadastros.Intf.dll; RM.Fis.Cadastros.Data.dll

## 12.1.2602.155

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1668]** XML da NFS-e Layouts TSS, TPF e Nacional - NFS-e Evolução no código do serviço para considerar a perspectiva de tributação.

Arquivos: RM.Fis.RotinasFiscais.Intf.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DOCELETRONICOS-1798]** NFS-e - Layout Nacional - Consistencia para gerar o grupo de Benefício Municipal - tribMun/BM

Arquivos: RM.Fis.Enderecos.Form.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBJETOS DE NEGÓCIO - SMART VIEW

* **[Ticket: DMOTORFISCALRM-515]** Melhorias e criação do objeto gerencial para Visão de dados IBSCBS no SmartView

Arquivo: RM.Fis.NativeProvider.Service.dll

## 12.1.2602.157

### Rotina: Sem Rotina Específica

* **[Ticket: DOCELETRONICOS-1775]** Ajuste na tag CTribNac no envio de NFS-e utilizando o layout TSS

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: ESCRITURAÇÃO (RM LI)

* **[Ticket: DMOTORFISCALRM-764]** Correção ao tentar estornar lotes que possuem lançamentos de INSS.

Arquivo: RM.Fis.LancFiscal.Service.dll

## 12.1.2602.158

### Rotina: CADASTROS - PROCESSOS - CÓPIAS (RM LI)

* **[Ticket: 27351002 / DMONTRIBRM-3980]** Trata a cópia do cadastro de Código de Ajuste entre Coligadas

Arquivo: RM.Fis.NaturezaOper.Data.dll

## 12.1.2602.159

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1551]** NFSe TPF - ajuste para tags de pis cofins considerando o parâmetro da NT007

Arquivo: RM.Fis.RotinasFiscais.Service.dll

## 12.1.2602.162

### Rotina: CUSTOMIZAÇÕES / ESPECÍFICOS

* **[Ticket: DMONTRIBRM-4114]** [BP-e] Adição do tipo BP-e TM no movimento, escrituração/lanc. e SPED D100

Arquivos: RM.Fis.Sped.Engine.dll; RM.Fis.Lib.dll; RM.Fis.Sped.Server.dll; RM.Fis.EscrituracaoFiscal.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-4100]** Criação do objeto de negócio para Danfe NFS-e

Arquivo: RM.Doc.NativeProvider.Service.dll

## 12.1.2602.165

### Rotina: Sem Rotina Específica

* **[Ticket: DOCELETRONICOS-1775]** Ajuste nos codigos de tributação com base na perspectiva

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: 28271479 / DOCELETRONICOS-1834]** Melhoria na identação de conteúdos exibidos no xml

Arquivos: RM.Fis.Utils.Server.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - ENTRADA/SAÍDA (RM LI)

* **[Ticket: DMOTORFISCALRM-600]** Escrituração de Finalidade e Tipo (Débito/Crédito)

Arquivos: RM.Fis.Contextos.IService.dll; RM.Fis.Contextos.Service.dll; RM.Fis.EscrituracaoFiscal.Service.dll; RM.Fis.EscrituracaoFiscal.Intf.dll

## 12.1.2602.166

### Rotina: Sem Rotina Específica

* **[Ticket: 28673670 / DOCELETRONICOS-1959]** Sel Nat - ajustes para busca de dados

Arquivos: RM.Fis.NaturezaOper.IService.dll; RM.Fis.NaturezaOper.Service.dll; RM.Fis.Tributo.Service.dll

## 12.1.2602.167

### Rotina: DEMAIS PROCESSOS

* **[Ticket: 28546277 / DOCELETRONICOS-1941]** Sel Nat - ajuste para informações padrão

Arquivo: RM.Fis.NaturezaOper.IService.dll

### Rotina: NF-E - ENVIO

* **[Ticket: DMOTORFISCALRM-597]** Emissão de NFe de Débito (geração das tags tpNfDebito e finNFe com tipo debito e credito)

Arquivos: RM.Fis.NFe.Service.dll; RM.Fis.Utils.Intf.dll; RM.Fis.Facade.dll; RM.Fis.NFe.Intf.dll; RM.Fis.Lib.dll

* **[Ticket: DMOTORFISCALRM-597]** Emissão de NFe de Débito (Tipo Pagamento Antecipado)

Arquivos: RM.Fis.NFe.Service.dll; RM.Fis.Lib.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-4100]** Criação dos grupos Prestador, Tomador, Destinatário e Intermediário no objeto de negócio para Danfe NFS-e

Arquivo: RM.Doc.NativeProvider.Service.dll

* **[Ticket: DMONTRIBRM-4102]** DANFSE - Implementação do Grupo Serviço

Arquivo: RM.Doc.NativeProvider.Service.dll

* **[Ticket: DMONTRIBRM-4106]** Criação dos grupos de Totais e Informações Complementares no objeto de negócio para Danfe NFS-e

Arquivo: RM.Doc.NativeProvider.Service.dll

### Rotina: OBRIGAÇÕES PRINCIPAIS - APURAÇÃO ICMS (RM LI)

* **[Ticket: 27356673 / DMOTORFISCALRM-768]** Período de Apuração - ICMS - saldo credor/devedor

Arquivo: RM.Fis.ApuracaoTrb.Service.dll

## 12.1.2602.168

### Rotina: NFS-E - CADASTRO

* **[Ticket: DOCELETRONICOS-1912]** Ajuste nos codigos de tributação com base na perspectiva

Arquivo: RM.Fis.RotinasFiscais.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: 27112630 / DOCELETRONICOS-1829]** Sel Nat - ajustes internos

Arquivos: RM.Fis.Tributo.Service.dll; RM.Fis.NaturezaOper.IService.dll; RM.Fis.NaturezaOper.Service.dll

### Rotina: NFS-E (RT)

* **[Ticket: 28459777 / DOCELETRONICOS-1854]** NFSe - ajustes para a geração do grupo de ibs/cbs para base zerada

Arquivos: RM.Fis.Utils.Intf.dll; RM.Fis.RotinasFiscais.Service.dll; RM.Fis.Utils.Server.dll

## 12.1.2602.169

### Rotina: Sem Rotina Específica

* **[Ticket: DMONTRIBRM-4306]** Acessa o recurso do smart view selecionado para visualização

Arquivo: Fis/monitor-tributario-front

## 12.1.2602.170

### Rotina: ESCRITURAÇÃO (RM LI)

* **[Ticket: 28938891 / DMONTRIBRM-4339]** [ESCRITURAÇÃO] COSIRF escriturado por beneficiário, código de receita e alíquota

Arquivos: RM.Fis.EscrituracaoFiscal.Service.dll; RM.Fis.LancFiscal.Service.dll

### Rotina: INTEGRAÇÃO CONTÁBIL

* **[Ticket: 28366204 / DMOTORFISCALRM-843]** Ajuste: Estorno de um lote de escrituração fiscal cujo lançamento possuía o campo "Indicador da Natureza de Frete" preenchido.

Arquivo: RM.Fis.LancFiscal.Service.dll

### Rotina: NF-E - ENVIO

* **[Ticket: DMOTORFISCALRM-759]** Emissão de NFe de Débito (Perda Em Estoque)

Arquivos: RM.Fis.NFe.Intf.dll; RM.Fis.NFe.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1551]** Implementação na Consulta de NFSe para atualizar os dados do Movimento 2.2.xx conforme retorno da Nota

Arquivos: RM.Fis.Facade.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: DOCELETRONICOS-1551]** Simplificação do Processo de Consulta, ajuste NFSe igual a zero

Arquivos: RM.Fis.EscrituracaoFiscal.Service.dll; RM.Fis.RotinasFiscais.Service.dll

* **[Ticket: 27112630 / DOCELETRONICOS-1829]** NFSe - grupo tcconstrciv deixa de ser gerado

Arquivos: RM.Fis.RotinasFiscais.Service.dll; RM.Fis.RotinasFiscais.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-4104]** [DANFSE | SV] Adição campos de valores IBS/CBS e demais retenções federais

Arquivo: RM.Doc.NativeProvider.Service.dll

* **[Ticket: DMONTRIBRM-4106]** Fallback dos campos do grupo Prestador

Arquivo: RM.Doc.NativeProvider.Service.dll

## 12.1.2602.171

### Rotina: CADASTROS - PRODUTOS/SERVIÇOS (RM LI)

* **[Ticket: DOCELETRONICOS-2015]** Aplicar Tributos ao Produto por Município

Arquivos: RM.Fis.Cadastros.Data.dll; RM.Fis.Cadastros.Form.dll; RM.Fis.Cadastros.Intf.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-4102]** DANFSe - correção nas tags vDR e vCalcReeRepRes

Arquivo: RM.Doc.NativeProvider.Service.dll

* **[Ticket: DMONTRIBRM-4108]** DANFSe para as versões de mercado

Arquivo: RM.Doc.NativeProvider.Service.dll

### Rotina: TOTVS INTELIGÊNCIA TRIBUTÁRIA

* **[Ticket: DMONTRIBRM-4350]** Melhoria de qualidade

Arquivo: Fis/monitor-tributario-front

## 12.1.2602.173

### Rotina: EMISSÃO

* **[Ticket: DMOTORFISCALRM-802]** Criação de XML para Eventos da NFe

Arquivos: RM.Fis.NFe.Intf.dll; RM.Fis.NFe.Form.dll; RM.Fis.NFe.Data.dll

* **[Ticket: DMOTORFISCALRM-808]** Ajustado processo para permitir o Envio de Cancelamento de Eventos Autorizados [110001].

Arquivo: RM.Fis.NFe.Data.dll

### Rotina: NF-E - ENVIO

* **[Ticket: DMOTORFISCALRM-781]** Emissão de NFe de Crédito. 03=Retorno por recusa total na entrega ou por não localização do destinatário na tentativa de entrega

Arquivos: RM.Fis.NFe.Intf.dll; RM.Fis.NFe.Service.dll

* **[Ticket: DMOTORFISCALRM-793]** Estrutura para criação dos eventos, Perda de Isenção/Credito Bens e Serviços/ Pagamento Antecipado

Arquivos: RM.Fis.NFe.Intf.dll; RM.Fis.NFe.IService.dll; RM.Fis.NFe.Form.dll; RM.Fis.NFe.Service.dll

### Rotina: NFS-E - ENVIO

* **[Ticket: DOCELETRONICOS-1555]** Ajuste para atualizar o movimento quando alterar o registro da NFS-e manualmente.

Arquivos: RM.Fis.RotinasFiscais.Data.dll; RM.Fis.RotinasFiscais.Service.dll

### Rotina: NOTA FISCAL DE COMUNICAÇÃO ELETRÔNICA

* **[Ticket: DOCELETRONICOS-1932]** Danfe Nfcom - campos do grupo retTrib adicionados ao objeto de negócio

Arquivo: RM.Doc.NativeProvider.Service.dll

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-4096]** Impressão da DANFSe para NFSe

Arquivo: RM.Fis.RotinasFiscais.Form.dll

* **[Ticket: DMONTRIBRM-4097]** Impressão da DANFSe para NFSe

Arquivos: RM.Doc.NFSe.IService.dll; RM.Doc.NFSe.Intf.dll; RM.Doc.NFSe.Form.dll; RM.Doc.NFSe.Data.dll; RM.Doc.NFSe.Service.dll

* **[Ticket: DMONTRIBRM-4109]** DANFSE - Inclusão do projeto RM.Doc.NativeProvider.TesteUnitario

Arquivo: RM.Doc.NativeProvider.Service.dll

## 12.1.2602.174

### Rotina: OBRIGAÇÕES ACESSÓRIAS - FEDERAIS - EFD REINF - R2010 (RM LI)

* **[Ticket: DMONTRIBRM-4097]** Correção para o processo de impressão da DANFS-e

Arquivos: RM.Doc.NFSe.Service.dll; RM.Doc.NFSe.Form.dll

# TOTVS Gestão Hospitalar

## 12.1.2602.100

### Rotina: Sem Rotina Específica

* **[Ticket: 26102465 / DSAUCLINICA-14146]** Ajuste no cálculo de quantidade e dosagem dos itens lançados no tipo de movimento Transcrição, na rotina de movimentação de estoque.

Arquivos: RM.Sau.Stock.Form.dll; RM.Sau.Stock.Server.dll

* **[Ticket: 26102465 / DSAUCLINICA-14146]** Ajuste no cálculo do valor unitário e do valor total dos itens lançados no tipo de movimento Transcrição, na rotina de movimentação de estoque.

Arquivos: RM.Sau.Stock.Server.dll; RM.Sau.Stock.Form.dll

* **[Ticket: 26168331 / DSAUGHUD-5010]** Na central de laudos em prontuário eletrônico ao Liberar um laudo com assinatura digital EvalTec foi incluido no rodape do laudo os dados da pessoa que assinou o laudo;

Arquivos: RM.Sau.UnidadeDiagnostico.Assinatura.Server.dll; RM.Sau.Pep.Server.dll; RM.Sau.Utils.Intf.dll; RM.Sau.UnidadeDiagnostico.Assinatura.Intf.dll; RM.Sau.Pep.Intf.dll

### Rotina: CADASTRO DE DENTES

* **[Ticket: DSAUGHPACDIG-1337]** adicionar status ao mapa facial

Arquivo: Sau/pep

### Rotina: FATURAMENTO TISS

* **[Ticket: DSAUGHFATF-25231]** Na rotina de faturamento eletrônico, quando informado uma competência diferente do mês atual, o sistema grava no campo data de geração da fatura, o ultimo dia do mês da competência informada.

Arquivos: RM.Sau.FaturamentoConvenio.Form.dll; RM.Sau.Sus.Form.dll; RM.Sau.Faturamento.Form.dll

### Rotina: FORMULÁRIO DINÂMICO

* **[Ticket: DSAUPEPCONV-22917]** Ajuste expedição de patch - Engenharia/SmartX

Arquivos: RM.Sau.SmartX.OrcamentoCliente.Objetos.Service.dll; RM.Sau.SmartX.CadastrosFat.Objetos.Service.dll; RM.Sau.SmartX.Cadastros.Objetos.Service.dll; RM.Sau.ActionsHub.Shared.dll; RM.Sau.SmartX.Paciente.Service.dll; RM.Sau.SmartX.OrcamentoCliente.Service.dll; RM.Sau.SmartX.Paciente.Objetos.Service.dll; RM.Sau.SmartX.Cadastros.Service.dll; RM.Sau.SmartX.CadastrosFat.Service.dll

* **[Ticket: DSAUPEPCONV-22917]** Ajuste na suspensão de formulários dinâmicos

Arquivos: RM.Sau.SmartX.Cadastros.Service.dll; RM.Sau.SmartX.Cadastros.Objetos.Service.dll

### Rotina: IDENTIFICAÇÃO / CABEÇALHO

* **[Ticket: DSAUPEPCONV-22946]** DSAUPEPCONV-22946 AUTOMAÇÃO TEST FLOW - PROJETO: 446143

Arquivo: Sau/pep-e2e

### Rotina: MEDICAMENTO

* **[Ticket: DSAUPEPCONV-22772]** DSAUPEPCONV-22772 AUTOMAÇÃO TEST FLOW - PROJETO: 462821

Arquivo: Sau/pep-e2e

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14195]** Ajuste na rotina de devolução da movimentação de estoque. Quando um kit for dispensado via painel de cirurgia e seus itens forem utilizados, caso seja necessário realizar a devolução, o sistema deverá permitir a inclusão e a devolução dos itens que fazem parte do kit e que estejam marcados como utilizados, através da rotina de devolução na movimentação de estoque.

Arquivos: RM.Sau.Stock.Form.dll; RM.Sau.Produto.Server.dll

### Rotina: ONCOLOGIA - TRATAMENTOS

* **[Ticket: DSAUGHNEXUS-759]** Painel de Oncologia - Ordenação por idade

Arquivo: Sau/pep

### Rotina: PROTOCOLOS ASSISTENCIAIS - FORMULÁRIO PEP

* **[Ticket: DSAUGHNEXUS-731]** Painel de Protocolos - Ordenação por idade

Arquivo: Sau/pep

## 12.1.2602.101

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUGHUD-5045]** tamanho correto de ícone

Arquivo: Sau/pep

* **[Ticket: DSAUGHUD-5063]** Incluido validação de status pendente na revisão de laudos na central de laudos no prontuário do paciente

Arquivo: Sau/pep

* **[Ticket: DSAUGHUD-5075]** Cadastro de conservantes da unidade de diagnóstico a permissão de edição não funcionava corretamente. Será necessário reconfigurar a permissão;

Arquivo: RM.Sau.Server.dll

* **[Ticket: DSAUGHASSIST-21004]** Ajuste ao salvar responsavel do paciente

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

* **[Ticket: DSAUGHUD-5032]** Ajuste no pedido de exame em unidade de diagnóstico na opção geração de exceção em anexos

Arquivo: RM.Sau.Utils.Intf.dll

* **[Ticket: DSAUGHUD-5033]** Ajuste da colunas de listagem para banco de dados Oracle no pedido de exame em unidade de diagnóstico

Arquivo: RM.Sau.UnidadeDiagnostico.Data.dll

* **[Ticket: DSAUGHUD-5043]** Ajuste na abertura de arquivos no pedido de exame em unidade de diagnóstico

Arquivo: RM.Sau.UnidadeDiagnostico.Form.dll

### Rotina: BUSCA , OPÇÕES AVANÇADAS OU OUTROS

* **[Ticket: DSAUPEPCONV-22982]** Ajuste na mensagem de notificação.

Arquivo: Sau/pep

### Rotina: CADASTRO DE DENTES

* **[Ticket: DSAUGHPACDIG-1337]** finalizar mapa facial

Arquivo: Sau/pep

### Rotina: CONTROLE DE GLOSAS

* **[Ticket: DSAUGHFATF-25298]** Ao importar o xml de DEMONSTRATIVO\_ANALISE\_CONTA, o sistema está alimentando o valor de glosa diferente do que consta no xml para uma das parciais. Trata-se de atendimento onde as duas parciais possuem o mesmo número de guia. Ao finalizar a importação o sistema apresenta crítica que não encontrou na conta item do arquivo, porém, o item existe normalmente.

Arquivo: RM.Sau.Tiss.Infraestrutura.Server.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-25359]** Efetuada revisão nas colunas das tabelas dos grupos de gasto ao efetuar estorno de itens na conta

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Faturamento.Server.dll

* **[Ticket: DSAUGHFATF-25359]** Efetuada revisão nas colunas de Data e Hora do lançamento do item de acordo com o grupo de gasto

Arquivos: RM.Sau.Autorizacao.Data.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Utils.Intf.dll

* **[Ticket: DSAUGHFATF-25306]** Ajuste na edição de honorários para não remover o mesmo da cobrança do pacote

Arquivo: RM.Sau.Faturamento.Form.dll

### Rotina: GESTÃO DE LEITOS - AGENDAMENTOS

* **[Ticket: 26433510 / DSAUGHFATF-25239]** Efetuada revisão na geração de guia ao lançar procedimentos na prescrição médica

Arquivos: RM.Sau.Pep.Server.dll; RM.Sau.Cadastros.Intf.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.Pep.Intf.dll; RM.Sau.Utils.Intf.dll; RM.Pep.SolicitacaoProcedimento.Server.dll; RM.Sau.Autorizacao.Data.dll; RM.Sau.Cadastros.Form.dll; RM.Pep.Prescricao.Server.dll; RM.Sau.Autorizacao.Intf.dll; RM.Pep.SolicitacaoProcedimento.Server.Negocio.dll

### Rotina: INTEGRAÇÕES LABORATORIAIS

* **[Ticket: DSAUGHUD-5035]** Tratativa para retornar mensagem url inválida no envio e cancelamento pedido de exame em unidade de diagnóstico com integração layout totvs

Arquivo: RM.Sau.Integracoes.Laboratorio.Server.dll

### Rotina: MANIPULAÇÃO DE MEDICAMENTOS - ESTOQUE MANIPULAÇÃO

* **[Ticket: DSAUCLINICA-14229]** Alteração integração OPUSPAC - Descrição do Produto | Quantidade

Arquivos: RM.Sau.Integracoes.Form.dll; RM.Sau.Produto.Server.dll; RM.Sau.ProductBarcode.Form.dll; RM.Sau.ProductBarcode.Intf.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-22831]** DSAUPEPCONV-22831 RÉPLICA para 12.1.2602 - [Mauá] - Parametrização - Aletas da prescrição médica

Arquivos: RM.Sau.Cadastros.Intf.dll; RM.Sau.Pep.Intf.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Data.dll

* **[Ticket: DSAUPEPCONV-22831]** DSAUPEPCONV-22831 RÉPLICA para 12.1.2602 - [Mauá

Arquivo: Sau/pep

* **[Ticket: DSAUPEPCONV-22896]** DSAUPEPCONV-22896 Checagem / Aprazamento. Horários

Arquivo: Sau/pep

* **[Ticket: 26492682 / DSAUPEPCONV-22922]** DSAUPEPCONV-22831 RÉPLICA para 12.1.2602 - [Mauá

Arquivo: Sau/pep

### Rotina: REGISTRO DE INFORMAÇÃO CIRURGICA - EDIÇÃO

* **[Ticket: DSAUGHFATF-25322]** Efetuada revisão na rotina de estorno de itens na elaboração de contas

Arquivo: RM.Sau.Utils.Intf.dll

## 12.1.2602.102

### Rotina: AUTORIZAÇÕES

* **[Ticket: 26249703 / DSAUGHFATF-25103]** Hash ao cancelar a Guia não esta valida

Arquivo: RM.Sau.Tiss.Application.Server.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-25305]** Na atualização de valores, não esta encontrando o produto quando cadastrado com o tipo Órtese,Prótese,Outros, apos a correção

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: FATURAMENTO IPERGS

* **[Ticket: DSAUGHFATF-25319]** Exigindo versão TISS para o Convênio Ipergs

Arquivo: RM.Sau.Utils.Intf.dll

## 12.1.2602.104

### Rotina: FATURAMENTO TISS

* **[Ticket: DSAUGHFATF-25263]** Vínculo de Pacote com Procedimento e Geração da Equipe no XML na TISS 3.00

Arquivos: RM.Sau.Ans.Sever.dll; RM.Sau.Autorizacao.Form.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Autorizacao.Intf.dll; RM.Sau.FaturamentoConvenio.Server.dll; RM.Sau.Autorizacao.Data.dll

### Rotina: PEDIDO DE EXAMES

* **[Ticket: DSAUGHUD-4461]** Na tela de atendimento de paciente foi implementado verificação para desconsiderar a validação de peso e altura do paciente se for efetuar um cancelamento de exame

Arquivos: RM.Sau.UnidadeDiagnostico.Server.dll; RM.Sau.UnidadeDiagnostico.Intf.dll; RM.Sau.RegistroAtendimento.Form.dll

### Rotina: REPROCESSAMENTO DE REPASSES

* **[Ticket: DSAUGHFATF-25303]** Efetuada revisão no cálculo dos valores lançados na divisão de repasse

Arquivo: RM.Sau.Faturamento.Form.dll

## 12.1.2602.105

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: 26539617 / DSAUGHFATF-25321]** Caso exista restrição de contrato para exigir liberação do convênio para determinado procedimento, o sistema só está permitindo encerrar a parcial se a quantidade informada na tela da guia estiver de "acordo" com a quantidade lançada na conta, mesmo sendo uma equipe.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: PAINEL DA FARMÁCIA

* **[Ticket: DSAUCLINICA-14260]** Correção ao associar dois perfis de usuário à um usuário, contendo a configuração marcada para visão por turno do painel de dispensação.

Arquivo: Sau/Sau-PortalFarmacia

### Rotina: REALIZAR CADASTRO DO PACIENTE

* **[Ticket: 26309475 / DSAUGHASSIST-21640]** Ajuste em uma integração interna

Arquivo: Sau/portalpaciente

* **[Ticket: 26309475 / DSAUGHASSIST-21640]** Ajuste em integrações internas

Arquivo: Sau/portalpaciente

## 12.1.2602.106

### Rotina: MEDICAMENTO

* **[Ticket: DSAUPEPCONV-22740]** Item Liberado com ressalva

Arquivo: Sau/pep

### Rotina: ONCOLOGIA - TRATAMENTOS

* **[Ticket: DSAUGHNEXUS-759]** Ajuste em sobreposição das opções no Painel de Oncologia

Arquivo: Sau/pep

### Rotina: OUTROS CADASTROS

* **[Ticket: DSAUGHFATF-25330]** Orçamento de Conta Particular Recepção. Incluir Kits de Lançamentos

Arquivos: RM.Sau.Faturamento.Server.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.Faturamento.Data.dll; RM.Sau.Faturamento.Intf.dll

### Rotina: PAINEL DE CIRURGIAS - EDIÇÃO

* **[Ticket: DSAUCLINICA-14164]** No Painel de Cirurgia, ao devolver um item pertencente ao Kit Pré montado, a movimentação de estoque gerado no BackOffice deverá ser o código descrito no parâmetro geral de estoque “Kit Pré Montado – Movimento (Devolução)”. Mesmo quando estiver marcado o parâmetro “Lança os itens do kit pré-montado na requisição”.

Arquivos: RM.Sau.Produto.Server.dll; RM.Sau.Stock.Server.dll

### Rotina: PAINEL DE DISPENSAÇÃO - VISÃO

* **[Ticket: 26453624 / DSAUCLINICA-14214]** Realizado ajuste na rotina de liberação de prescrições que contenham itens de uso coletivo. A partir desta atualização, ao liberar uma prescrição com item de uso coletivo desde que a unidade esteja configurada conforme documentação o item será automaticamente enviado à farmácia com o status Processado. Com isso, não haverá pendência para processamento na farmácia, sendo necessária apenas a checagem no prontuário eletrônico para que a cobrança seja efetivada na conta do paciente.

Arquivos: RM.Sau.Stock.Intf.dll; RM.Sau.Stock.Server.dll

### Rotina: PEDIDO DE EXAMES

* **[Ticket: DSAUGHUD-4767]** Na tela de pedido de exame em unidade de diagnóstico, quando houver integração, os campos de peso, altura, volume urinário e local de coleta não ficarão mais desabilitados

Arquivo: RM.Sau.UnidadeDiagnostico.Form.dll

### Rotina: PROTOCOLOS ASSISTENCIAIS - FORMULÁRIO PEP

* **[Ticket: DSAUGHNEXUS-731]** Ajuste em sobreposição das opções no Painel de Protocolos

Arquivo: Sau/pep

## 12.1.2602.107

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUPEPCONV-22865]** Informativo na solicitação de mat/med

Arquivo: Sau/pep

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21748]** Ajuste no assistente de agendamento para melhora de perfonemance e inteligencia na seleção de horarios

Arquivos: RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.UnidadeDiagnostico.Server.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Form.dll

### Rotina: AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-25419]** Remoção da validação de não poder existir guia de resumo com guia de prorrogação na mesma parcial

Arquivo: RM.Sau.AuthorizationGuide.Intf.dll

### Rotina: LIBERAÇÃO

* **[Ticket: DSAUPEPCONV-22741]** Obrigatoriedade de retorno Item Liberado com Ressalva

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Intf.dll; RM.Sau.Cadastros.Form.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: DSAUGHFATF-25411]** Efetuada revisão nos componentes de comunicação com a base de dados da tela de cadastro de unidades de atendimento

Arquivo: RM.Sau.Cadastros.Form.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-23005]** Unidade de Dosagem de material

Arquivos: RM.Sau.Stock.Intf.dll; RM.Sau.Stock.Server.dll; RM.Sau.Produto.Intf.dll

### Rotina: RECEPÇÃO

* **[Ticket: 26356423 / DSAUGHFATF-25240]** Ajuste para corrigir problemas de violação de chave estrangeira ao concluir atendimento particular no módulo de atendimento simplificado.

Arquivo: RM.Sau.Movimento.Service.dll

### Rotina: REGISTRO DE INFORMAÇÃO CIRURGICA - EDIÇÃO

* **[Ticket: DSAUGHFATF-25322]** Faturamento de exames cadastrados no Registro de Informações Cirúrgicas

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.RegistroInfCirurgia.Data.dll; RM.Sau.Faturamento.Server.dll

### Rotina: SOROS E COMPONENTES

* **[Ticket: DSAUPEPCONV-22779]** DSAUPEPCONV-22779 [ Mauá

Arquivo: Sau/pep

## 12.1.2602.108

### Rotina: ATENDIMENTO SIMPLIFICADO - CONCLUSÃO

* **[Ticket: 26271317 / DSAUGHUD-5028]** Na tela de pedido de exame em unidade de diagnóstico, quando houver integração shift, será enviado a descrição do material no xml da integração

Arquivo: RM.Sau.Integracoes.Server.dll

### Rotina: CÓPIA DE PRESCRIÇÃO

* **[Ticket: 26618761 / DSAUPEPCONV-23021]** DSAUPEPCONV-23021 Botão NOVO está desabilitado para fazer uma NOVA PRESCRIÇÃO

Arquivo: Sau/pep

### Rotina: PEDIDO DE EXAMES

* **[Ticket: DSAUGHUD-4461]** Implementado na tela de atendimento em pedido de exame para exibir o número do pedido e exame ao notificar obrigatoriedade de peso ou altura;

Arquivos: RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.UnidadeDiagnostico.Server.dll; RM.Sau.Parametros.Intf.dll; RM.Sau.UnidadeDiagnostico.Intf.dll

## 12.1.2602.109

### Rotina: PAINEL DE CIRURGIAS - EDIÇÃO

* **[Ticket: DSAUCLINICA-14198]** Alterado no painel de cirurgia, após ficar com a tela aberta por um período muito grande, ao clicar em “Devolver itens” apresentava mensagem e perdia os dados digitados.

Arquivo: RM.Sau.Stock.Form.dll

## 12.1.2602.110

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUGHFATF-25015]** Ajuste na tela de condições contratuais para que ao mudar a versão da TISS, o campo "Específico" seja reiniciado sem valor, evitando assim que fique configuração inválida, causando problemas ao buscar preços e ao efetuar outras validações.

Arquivo: RM.Sau.CadastrosFat.Form.dll

### Rotina: ALTA

* **[Ticket: DSAUGHASSIST-21621]** Inclusão do Número da declaração de óbito na alta

Arquivos: RM.Sau.Parametrizador.Data.dll; RM.Sau.Parametrizador.Form.dll; RM.Sau.RegistroAtendimento.Data.dll; RM.Sau.Parametrizador.Intf.dll; RM.Sau.Ans.Intf.dll; RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.Common.Intf.dll; RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.Parametros.Intf.dll

### Rotina: AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-25448]** Ajuste nos itens vinculados à uma guia excluída ou que a numeração foi alterada

Arquivos: RM.Sau.Faturamento.Server.dll; RM.Sau.AuthorizationGuide.Server.dll

* **[Ticket: DSAUGHFATF-25453]** Criação do cabeçalho da guia para itens com restrição de contrato

Arquivo: RM.Sau.AuthorizationGuide.Server.dll

### Rotina: AVALIAÇÕES COMPLEMENTARES

* **[Ticket: DSAUPEPCONV-22638]** Ajuste data e hora cronograma SAEP

Arquivo: Sau/pep

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-25230]** Adicionada rotina de guia/autorização como anexo na elaboração de contas

Arquivos: RM.Sau.AuthorizationGuide.Form.dll; RM.Sau.Faturamento.Form.dll

### Rotina: CENTRAL DE LAUDOS

* **[Ticket: DSAUGHUD-4808]** Ajuste na permissão de reconvocação de exame na central de laudos no prontuário eletrônico

Arquivo: RM.Sau.Api.dll

* **[Ticket: DSAUGHUD-5062]** Ajuste limpar campo medico responsável

Arquivo: Sau/pep

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: 26692662 / DSAUGHFATF-25466]** 'Habilitações Programa Agora tem Especialistas' na qual consta regras sobre a exigência do cadastro dessas habilitações. Em resumo a regra é o seguinte: Se o quinto dígito do número da AIH (não é procedimento) for 8, exemplo de numeração de AIH: 3525 8 76448530, a exigência do cadastro para essas habilitações deve ocorrer, porém, se for 1 por exemplo: 3525 1 76448530, mesmo sem o cadastro das habilitações a crítica não deve ocorrer (gentileza verificar a nota e a fim de também confirmarem sobre a regra à ser aplicada).Atualmente o RM exige o cadastro das habilitações (caso exista vínculo com o procedimento utilizado no SIGTAP) independente do quinto dígito do número da AIH.

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Sus.Server.dll

### Rotina: IDENTIFICAÇÃO / CABEÇALHO

* **[Ticket: DSAUPEPCONV-23019]** DSAUPEPCONV-23019 Refresh token já utilizado

Arquivo: Sau/pep

### Rotina: INTEGRAÇÕES LABORATORIAIS

* **[Ticket: DSAUGHUD-4838]** Bloquear reconvocação que já foi solicitada, e o laudo já está associado à reconvocação correspondente.

Arquivo: Sau/pep

### Rotina: MAPA DA AGENDA DE CIRURGIAS - MAPA

* **[Ticket: 26217658 / DSAUGHFATF-25227]** Efetuada revisão nos status que permitem cancelar um ahendamento cirúrgico

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.AgendaCirurgia.Form.dll; RM.Sau.AgendaAtendimento.Form.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-22896]** DSAUPEPCONV-22896 Checagem / Aprazamento. Horários

Arquivo: Sau/pep

## 12.1.2602.111

### Rotina: Sem Rotina Específica

* **[Ticket: 26591236 / DSAUPEPCONV-23157]** Ajuste para que a edição de uma seção de um formulário do protocolo assistencial atualize corretamente os perfis profissionais responsáveis

Arquivo: Sau/saude-front

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21841]** Inclusão do projetos de Agendamento de exame simplificado customizado

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.CadastrosFat.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.CadastrosFat.Data.dll

* **[Ticket: 26359657 / DSAUGHASSIST-21612]** Ajuste ao atualizar calendario de agendamentos

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: 26591688 / DSAUGHASSIST-21699]** Ajuste no tamanho do campo complemento e no salvamento do agendamento

Arquivos: RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.Paciente.Intf.dll

* **[Ticket: DSAUGHASSIST-21812]** Inclusão do projetos de Agendamento de exame simplificado customizado

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll

* **[Ticket: DSAUGHASSIST-21822]** [FEAT] DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivos: RM.Sau.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll; RM.Sau.Utils.Intf.dll

* **[Ticket: DSAUGHASSIST-21822]** DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivo: Sau/saude-front

### Rotina: CADASTROS

* **[Ticket: 26362239 / DSAUGHASSIST-21614]** Ajuste na criação do atendimento para agendamentos futuros com exames quando a opção de pré-registro estiver desligada

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: FATURAMENTO TISS

* **[Ticket: 26642435 / DSAUGHFATF-25428]** O campo CBOS no XML deve ser exibido conforme a ordem de prioridade definida na Regra de CBO.Caso não exista configuração na regra, deve ser utilizado o CBO cadastrado do prestador.Já o registro de CBO na Equipe SADT deve obedecer à seguinte ordem de busca:CBO informado no Honorário SADT;Caso não esteja preenchido, utilizar o CBO definido na Regra de CBO;Persistindo a ausência, utilizar o CBO do cadastro do prestador.

Arquivos: RM.Sau.FaturamentoConvenio.Intf.dll; RM.Sau.FaturamentoConvenio.Server.dll; RM.Sau.Ans.Sever.dll

### Rotina: INTERNAÇÃO

* **[Ticket: DSAUGHFATF-25500]** Ajuste na validação de restrições relacioanadas à diária no cadastro do RN

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Form.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-22817]** Painel de Dispensação quando solicitados pela enfermagem

Arquivo: RM.Sau.Produto.Server.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14235]** Realizado ajuste na rotina de validação de saldo durante o processo de devolução de itens na Movimentação de Estoque. No momento da validação de existência de requisição pendente para o item que está sendo devolvido, o sistema estava considerando indevidamente a própria requisição e o próprio item que o usuário estava adicionando, impactando o resultado da verificação.

Arquivos: RM.Sau.Stock.Server.dll; RM.Sau.Stock.Form.dll; RM.Sau.Stock.Data.dll; RM.Sau.Produto.Server.dll; RM.Sau.Produto.Intf.dll

### Rotina: PAINEL DE CIRURGIAS - EDIÇÃO

* **[Ticket: 26314266 / DSAUCLINICA-14171]** Ajuste na rotina de montagem de kit quando a origem for o Painel de Cirurgia: após a finalização do processo no painel, a montagem do kit passa a considerar também os itens devolvidos e os itens marcados como não utilizados, permitindo sua reutilização para montagem do kit.

Arquivos: RM.Sau.Stock.Server.dll; RM.Sau.Produto.Form.dll

### Rotina: PROTOCOLO TEV

* **[Ticket: 25913210 / DSAUPEPCONV-23149]** Abertura da modal do pin de assinatura ao concluir a seção

Arquivo: Sau/pep

### Rotina: RECEPÇÃO

* **[Ticket: 26549728 / DSAUGHASSIST-21728]** Ajuste realizado para altas de recem nascido morto

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.RegistroAtendimento.Data.dll

### Rotina: REGISTRO DE ATENDIMENTO

* **[Ticket: 26464559 / DSAUGHASSIST-21680]** Ajuste no carregamento de informações de agendamento no simplificado

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.RegistroAtendimento.Server.dll

### Rotina: REGISTRO E CONTROLE

* **[Ticket: DSAUGHASSIST-21566]** Migração da rotina de acerta leitos do delphi para .NET

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Cadastros.Server.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Intf.dll

## 12.1.2602.112

### Rotina: ACESSAR AS FUNCIONALIDADES DO PORTAL DO MEDICO

* **[Ticket: DSAUGHUD-5144]** Suporte Portal Prestador

Arquivo: RM.Sau.Cadastros.Data.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21822]** DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21827]** Criação dos endpoints de obtenção de lista de exames, grupos de exames e horarios livres. Inicio da criação dos commands de validação

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-21875]** Ajuste endpoint Horarios para retornar agendados, reservados e bloqueados, alem dos horarios livres

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimento.Server.dll

### Rotina: ANOTAÇÃO

* **[Ticket: 26787188 / DSAUPEPCONV-23178]** Ajustado a renovação de token em caso de token expirado

Arquivo: Sau/pep

### Rotina: CADASTROS SUS

* **[Ticket: 26691678 / DSAUGHFATF-25442]** O SUS passou a utilizar o CPF como cartão SUS, mas no sistema ao tentar registrar um atendimento SUS o sistema não permite que o campo esteja em branco ou que seja informado o CPF no campo CNS

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Sus.Intf.dll; RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.Sus.Server.dll; RM.Sau.Sus.Data.dll

### Rotina: CENTRAL DE LAUDOS

* **[Ticket: DSAUGHUD-5062]** Ajuste para cadastrar medico responsável ao mudar status para digitação

Arquivo: Sau/pep

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14206]** Correção para ao obter os dados de atendimento quando for criar um devolução obter o sequencial da parcial corretamente, Alterado validação de data no lançamento automático que não considerava parcial ainda não fechada em algumas situações.

Arquivos: RM.Sau.Stock.Server.dll; RM.Sau.Faturamento.Server.dll

### Rotina: PROTOCOLO TEV

* **[Ticket: 26028078 / DSAUGHNEXUS-572]** Cálculo do Score SAPS III

Arquivos: RM.Pep.Shared.dll; RM.Pep.ScorePaciente.IService.dll; RM.Sau.Server.dll; RM.Pep.ScorePaciente.Server.dll; RM.Pep.ScorePaciente.Server.Negocio.dll; RM.Sau.Score.Server.dll; RM.Sau.Score.Intf.dll

* **[Ticket: 26028078 / DSAUGHNEXUS-572]** Aplicação de cálculo de expressão matemática para a pontuação de scores

Arquivo: Sau/pep

* **[Ticket: 26028078 / DSAUGHNEXUS-572]** Ajuste para que ao alterar a seleção de um score a modal não exiba o resultado do score antigo

Arquivo: Sau/pep

## 12.1.2602.113

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21768]** Retorno de horarios passa a considerar tempo de autorição de exames

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll

* **[Ticket: DSAUGHASSIST-21769]** Inclusão calculo IMC agenda simplificada exame

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21779]** Informações do contrado agenda simplificada de exames

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21779]** Inclusão do projetos de Agendamento de exame simplificado customizado

Arquivos: RM.Sau.CadastrosFat.Data.dll; RM.Sau.CadastrosFat.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.dll

* **[Ticket: DSAUGHASSIST-21822]** DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21841]** Inclusão do projetos de Agendamento de exame simplificado customizado

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll; RM.Sau.Common.Form.dll

* **[Ticket: DSAUGHASSIST-21841]** Consulta paciente agenda simplificada exames

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21875]** Ajuste endpoint Horarios para retornar agendados, reservados e bloqueados, alem dos horarios livres

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.dll

* **[Ticket: DSAUGHASSIST-21876]** Adição de endpoint para reserva e cancelamento de reserva de horario. Criação de alguns Commands de validação de dados de paciente.

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll

* **[Ticket: DSAUGHASSIST-21879]** DSAUGHASSIST-21879 Agendamento anteriores / historico

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21907]** DSAUGHASSIST-21907 Calendário

Arquivo: Sau/saude-front

### Rotina: ATENDIMENTO SIMPLIFICADO - PACIENTE

* **[Ticket: DSAUGHASSIST-21882]** DSAUGHASSIST-21882 Criar filtros por turno e por disponibilidade do exame.

Arquivo: Sau/saude-front

### Rotina: GESTÃO DE LEITOS - OCUPAÇÃO DE LEITOS

* **[Ticket: DSAUGHASSIST-21927]** Ajuste na rotina para ocupação do leito e desocupação do leito

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

## 12.1.2602.114

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: 26515006 / DSAUGHASSIST-21698]** Ajuste na pesquisa do agendamento quando tem integração com a sala

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Data.dll

### Rotina: AGENDA DE CIRURGIAS - VISÃO

* **[Ticket: 26764784 / DSAUGHASSIST-21850]** Ajustes realizados para exclusão da grade de horários para especialidades com código alfanumérico

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21822]** DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21822]** Implementado bloqueio tela enquanto a tela estiver sendo construida

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21822]** Ajuste na data final de retorno apos adição de tempo de autorização

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.dll

* **[Ticket: DSAUGHASSIST-21827]** Criação de Validação de convenio e adição na rota de reserva

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-21955]** Criação de endpoint para salvar agendamento de exame

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-21955]** Remover Reserva antes de confirmar agendamento na agenda simplificada

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.dll

* **[Ticket: 26841504 / DSAUGHASSIST-21897]** Ajuste nas cores sobre dias disponiveis na agenda de agendamentos.

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-21905]** DSAUGHASSIST-21905 Reservar horário agendamento/cancelar reserva

Arquivo: Sau/saude-front

### Rotina: ATENDIMENTO SIMPLIFICADO - PACIENTE

* **[Ticket: 26544138 / DSAUGHASSIST-21697]** Alteração de arquivo de configuração

Arquivo: Sau/saude-front

* **[Ticket: 26544138 / DSAUGHASSIST-21697]** Adicionada janela para seleção de agendamento vinculado a senha

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Intf.dll

* **[Ticket: 26544138 / DSAUGHASSIST-21697]** Adicionada funcionalidade para selecionar agendamento relacionado ao atendimento

Arquivo: Sau/saude-front

### Rotina: ATUALIZAÇÃO BRASÍNDICE

* **[Ticket: DSAUGHFATF-25408]** Ajuste na rotina de Atualização de preço no processo de "Atualiza múltiplas informações" das tabelas de preço de MATMED, para atualizar o preço caso seja alterado o vínculo com Brasíndice ou Simpro

Arquivos: RM.Sau.Produto.Intf.dll; RM.Sau.Produto.Server.dll; RM.Sau.Produto.Data.dll; RM.Sau.Produto.Form.dll

### Rotina: ATUALIZAÇÃO DE VALORES

* **[Ticket: DSAUGHFATF-24532]** Ajuste na tela de tabela de preço para que ao carregar a tela seja exibido corretamente o fabricante em casos de preços Simpro, ou exibir corretamente o Laboratório em casos de preço Brasindice, previamente informados no cadastro.

Arquivo: RM.Sau.Produto.Form.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25485]** DESABILITADO O CAMPO EMENDA PARLAMENTAR (NÃO SERÁ MAIS UTILIZADO)

Arquivos: RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Form.dll; RM.Sau.Lib.dll; RM.Sau.Sus.Data.dll; RM.Sau.Sus.Server.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-25551]** Na tela de pesquisa de procedimentos, lista os itens da tabela especial mais os itens da tabela de procedimentos/serviços que não existem na tabela especial

Arquivo: RM.Sau.Services.Server.dll

### Rotina: FORMULÁRIO DINÂMICO

* **[Ticket: DSAUPEPCONV-23234]** FIX DSAUPEPCONV-23235 Action de produtos não visível no RM

Arquivo: RM.Sau.Produto.Form.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 26380210 / DSAUCLINICA-14220]** Realizado ajuste para permitir a finalização de solicitações que contenham o mesmo item lançado mais de uma vez. Anteriormente, a rotina bloqueava ou apresentava inconsistência ao processar solicitações com itens repetidos. Com a correção, o sistema passa a aceitar esse cenário, desde que atendidas as demais validações de negócio, garantindo o processamento adequado da solicitação.

Arquivo: RM.Sau.Stock.Server.dll

### Rotina: MEDICAMENTO

* **[Ticket: DSAUPEPCONV-23196]** Apresentação de aletas de prescrição médica quando existe registros antigos

Arquivo: Sau/pep

* **[Ticket: DSAUPEPCONV-23212]** FIX DSAUPEPCONV-23213 Correção no layout de configuração de aletas disponíveis no RM

Arquivo: RM.Sau.Cadastros.Form.dll

### Rotina: RECEPÇÃO

* **[Ticket: 26822773 / DSAUGHASSIST-21906]** Ajuste na exibição do convênio desativado na agenda de sala

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: REGISTRO DE INFORMAÇÕES CIRÚRGICAS

* **[Ticket: 26446374 / DSAUCLINICA-14228]** Ajuste na rotina de suspensão do painel de cirurgia: Passa a ser permitida a suspensão da cirurgia quando esta estiver com status “Liberado” e não houver itens utilizados. Com essa alteração, será possível realizar a devolução dos itens dispensados à cirurgia mesmo que o atendimento e/ou a cirurgia estejam cancelados.

Arquivo: RM.Sau.Stock.Server.dll

* **[Ticket: 26590752 / DSAUCLINICA-14275]** Ajuste nas políticas de permissão da tela de bloqueio de salas do bloco cirúrgico: Passa a ser possível ao administrador do sistema definir, por perfil de usuário, a permissão para incluir e/ou excluir bloqueios de salas.

Arquivo: RM.Sau.Server.dll

### Rotina: USO GERAL

* **[Ticket: DSAUGHFATF-25498]** Habilitar CodSus para todas fontes de preço

Arquivos: RM.Sau.Produto.Data.dll; RM.Sau.Produto.Form.dll

## 12.1.2602.115

### Rotina: ANOTAÇÃO

* **[Ticket: 26787188 / DSAUPEPCONV-23178]** Ajuste realizado para aumentar o limite de caracteres do campo nome da mãe

Arquivo: RM.Sau.RegistroAtendimento.Intf.dll

### Rotina: RESULTADOS DE EXAMES

* **[Ticket: DSAUPEPCONV-23126]** Exibir data da coleta

Arquivo: Sau/pep

## 12.1.2602.116

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21782]** anexar documentos agenda simplificada customizada

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21782]** Inclusão de anexo de documentos na Agendamento de exame simplificado customizado

Arquivos: RM.Sau.Utils.Server.Api.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Api.dll

* **[Ticket: DSAUGHASSIST-21822]** DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivos: Sau/saude-front; RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-21822]** [FIX] DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.dll

* **[Ticket: DSAUGHASSIST-21827]** Migração de validações da agenda necessarias no Villela Pedras

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.dll

* **[Ticket: DSAUGHASSIST-21827]** Ajuste CheckDll para geração de versão

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Intf.dll

* **[Ticket: DSAUGHASSIST-21905]** [FEAT] DSAUGHASSIST-21905 Reservar horário agendamento/cancelar reserva

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Api.dll

* **[Ticket: DSAUGHASSIST-21905]** DSAUGHASSIST-21905 Reservar horário agendamento/cancelar reserva

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21998]** Inclusão de anexo de documentos na Agendamento de exame simplificado customizado

Arquivo: RM.Sau.Api.dll

* **[Ticket: DSAUGHASSIST-21998]** ajuste dados paciente

Arquivo: Sau/saude-front

### Rotina: ELABORAÇÃO DE BPA

* **[Ticket: DSAUGHFATF-25509]** Incluir no layout da BPA a Nova regra do SIA/SUS (CPF ou CNS)

Arquivos: RM.Sau.Lib.dll; RM.Sau.Sus.Server.dll; RM.Sau.Sus.Intf.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14328]** Ajuste na tela de devolução da movimentação de estoque: ao editar um item controlado por lote adicionado manualmente, a lista de lotes não era exibida ao acionar o botão de seleção. Com a correção, o sistema passa a apresentar os lotes disponíveis, permitindo ao usuário selecionar ou alterar o lote a ser devolvido.

Arquivo: RM.Sau.Stock.Form.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - VISÃO

* **[Ticket: DSAUCLINICA-14295]** Ajuste na listagem de itens no movimento de devolução. Ao realizar a devolução de itens de um kit cuja origem seja uma folha de sala, o sistema deve a listar todos os itens do kit devolvidos na tela de visualização da movimentação de estoque.

Arquivo: RM.Sau.Stock.Data.dll

### Rotina: RECEPÇÃO

* **[Ticket: 26840286 / DSAUGHASSIST-21962]** Ajuste na seleção de dias sem agendas selecioandas.

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: USO GERAL

* **[Ticket: 26402230 / DSAUGHFATF-25207]** Ajuste no processamento do XML de Demonstrativo para atualizar automaticamente o número da guia quando houver divergência, mantendo o histórico do número anterior e garantindo consistência nas validações do sistema. Para mais informações acompanhar nossa documentação oficial : https://tdn.totvs.com/pages/viewpage.action?pageId=914797585

Arquivos: RM.Sau.Parametros.Intf.dll; RM.Sau.Tiss.Infraestrutura.Server.dll; RM.Sau.AuthorizationGuide.Intf.dll; RM.Sau.GestaoGlosa.Server.dll; RM.Sau.Ans.Sever.dll; RM.Sau.AuthorizationGuide.Data.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.CadastrosFat.Intf.dll; RM.Sau.Autorizacao.Data.dll; RM.Sau.AuthorizationGuide.Form.dll; RM.Sau.CadastrosFat.Form.dll; RM.Sau.Autorizacao.Intf.dll

## 12.1.2602.117

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21771]** Incluido verificação de permissão de agendamento por exame ao listar agendamentos

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21771]** Ajuste na aplicação de restrição agendamento por dia da semana e perfil de excecao

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21777]** Obter Preço do exame para convenio e plano

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-21767]** Validação de Bloquear Exame Repetido em 30 Dias

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-21771]** Ajuste na liberação de Reservas para considerar o usuario.

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21777]** DSAUGHASSIST-21777 US11 - Visualizar Preço do Exame Particular

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21782]** DSAUGHASSIST-21782 US16 - Ícone Anexos no Agendamento

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21822]** FAKE DSAUGHASSIST-21940\DSAUGHASSIST-21822

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21822]** DSAUGHASSIST-21822 Criar Nova View Agenda

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21827]** Ajuste na liberação de Reservas para considerar o usuario.

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-21827]** Ajuste na abertura da agenda e assistente de agendamento.

Arquivos: RM.Sau.Faturamento.Intf.dll; RM.Sau.Cadastros.Server.dll; RM.Sau.AgendaAtendimento.Intf.dll

* **[Ticket: DSAUGHASSIST-21827]** Migração de validações da agenda necessarias no Villela Pedras

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-21827]** Ajuste na definição de especialidade por horario de agenda

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21827]** Ajuste nas validações de agendamento

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21841]** ajustado dados do paciente para envio do agendamento

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21841]** Gravação de observação e medico solicitante na tabela complementar de agendamento;

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Form.dll

* **[Ticket: 26796750 / DSAUGHASSIST-21868]** Adicionado uma validação no encaixe para buscar a especialidade configurada no grade de horários

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-21898]** Sistema validando horário conflitante com bloqueio mesmo em edição de agendamento.

Arquivos: RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-21905]** [FIX] DSAUGHASSIST-21905 Reservar horário agendamento/cancelar reserva

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21996]** informação de preparo de exame

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21996]** incluido no detalhe as informações de preparo do exame

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22000]** Ajuste na nomenclatura do CrudServer para utilizar FV

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22000]** Ajuste no crudserver de inserir no carrinho para funcionar Formula Visual

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll

* **[Ticket: DSAUGHASSIST-22003]** Ajuste na lista de exames para retirar exames proibidos nas restrições contratuais e alteração no CrudServer para utilizar FV

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll

* **[Ticket: DSAUGHASSIST-22020]** Gravação de observação e medico solicitante na tabela complementar de agendamento;

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.dll

* **[Ticket: DSAUGHASSIST-22020]** gravação observação e medico solicitante

Arquivo: Sau/saude-front

### Rotina: APURAÇÃO DE PLANTÕES REALIZADOS

* **[Ticket: DSAUGHFATF-25549]** Na tela de registro de Plantão, criar um campo para informar se o Plantão é Cinderela

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.RegistroAtendimento.Data.dll

### Rotina: ATENDIMENTO SIMPLIFICADO - PACIENTE

* **[Ticket: 26544138 / DSAUGHASSIST-21697]** Adicionada janela para seleção de agendamento vinculado a senha

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-22013]** DSAUGHASSIST-22013 Tipo filtro agendamento

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22013]** ajuste filtro grupo exames

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22013]** Ajuste na obtenção de preço para não haver duplicidade de exames na lista

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: ATUALIZAÇÃO SIMPRO

* **[Ticket: DSAUGHFATF-25671]** Efetuada revisão no processo de atualização de valores simpro

Arquivos: RM.Sau.AtualizaPreco.Form.dll; RM.Sau.AtualizaPreco.Server.dll; RM.Sau.Produto.Server.dll; RM.Sau.Utils.Server.dll; RM.Sau.CrossCutting.dll

### Rotina: AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-25616]** Permitir Incluir Guia Autorização também quando o acesso é através do anexo da elaboração de contas

Arquivo: RM.Sau.AuthorizationGuide.Form.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25520]** Cálculo Automático da Competência de procedimento AIH ao incluir ou editar a data de procedimento médico.

Arquivo: RM.Sau.Sus.Form.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-22920]** Auste na solicitação de produto composto para exibir mensagem caso configuração incorreta

Arquivo: RM.Sau.Stock.Server.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: 26535456 / DSAUCLINICA-14349]** Ajuste na tela de itens da movimentação: ao acessar a edição do item, não será permitido executar os processos dessa rotina quando o tipo de movimento for Transcrição, Requisição para o Paciente, Folha de Sala ou Prescrição.

Arquivo: RM.Sau.Stock.Form.dll

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21918]** Orçamento para clientes SmartX

Arquivos: RM.Sau.Faturamento.Intf.dll; RM.Sau.SmartX.CadastrosFat.Service.dll; RM.Sau.Parametrizador.Form.dll; RM.Sau.Server.dll; RM.Sau.SmartX.OrcamentoCliente.Service.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Parametrizador.Data.dll; RM.Sau.Movimento.Service.dll; RM.Sau.SmartX.OrcamentoCliente.Objetos.Service.dll; RM.Sau.Api.dll; RM.Sau.SmartX.CadastrosFat.Objetos.Service.dll; RM.Sau.SmartX.Paciente.Objetos.Service.dll; RM.Sau.ActionsHub.Shared.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-22766]** Parametrização da obrigatoriedade do campo de fluxo na PM

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Intf.dll; RM.Sau.Cadastros.Form.dll; Sau/pep

* **[Ticket: DSAUGHASSIST-21834]** Adicionada janela para seleção de agendamento vinculado a senha

Arquivos: RM.Sau.UnidadeDiagnostico.Server.dll; RM.Sau.Integracoes.Server.dll

### Rotina: USO GERAL

* **[Ticket: DSAUGHFATF-25521]** alterar componente do Codigo Sus para selecionar

Arquivo: RM.Sau.Produto.Form.dll

## 12.1.2602.118

### Rotina: PAINEL DE DISPENSAÇÃO - EDIÇÃO

* **[Ticket: 26621310 / DSAUCLINICA-14374]** Ajuste na validação da data da requisição em relação à data de saída do paciente. Para pacientes externos, onde as datas de entrada e saída são iguais, a validação passa a considerar apenas a data (desconsiderando hora), permitindo a devolução dos itens quando as datas coincidirem.

Arquivo: RM.Sau.Stock.Server.dll

## 12.1.2602.119

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21878]** Ajuste para listar agendamento futuros com todas as informações

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22003]** Ajuste para atrelar EXAME x ESPECIALIDADE x AGENDA

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22127]** DSAUGHASSIST-22127 Melhora na usabilidade da tela

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21772]** Ajuste na busca de agendamentos na validação de 30 dias

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21772]** Ajuste na validação de horarios e dias coincidentes.

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21822]** Ajuste para ao limpar o convenio limpar a lista de plano

Arquivo: Sau/saude-front

### Rotina: PLANO TERAPÊUTICO

* **[Ticket: 26210533 / DSAUPEPCONV-22636]** DSAUPEPCONV-22636 Aumento de Caracteres nos campos abertos do Plano Terapêutico Hospitalar

Arquivo: Sau/pep

## 12.1.2602.120

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21878]** [FIX] DSAUGHASSIST-21878 Listar agendamento futuros

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21878]** DSAUGHASSIST-21878 Listar agendamento futuros

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21996]** Incluido tratativa para exibisão de informação de preparo do exame

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22137]** Ajuste para cores do calendario quando horario é especial

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-22147]** [FEAT] DSAUGHASSIST-22147 Envio de e-mail confirmação agendamento

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: FATURAMENTO TISS

* **[Ticket: 26987737 / DSAUGHFATF-25708]** Sistema ajustado para levar os MatMed no xml da TISS

Arquivo: RM.Sau.FaturamentoConvenio.Server.dll

### Rotina: IDENTIFICAÇÃO / CABEÇALHO

* **[Ticket: 26768617 / DSAUPEPCONV-23143]** DSAUPEPCONV-23143 Atualização de recursos nos servidores de portal

Arquivo: Sau/pep

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-22817]** DSAUPEPCONV-22817 SCPATROCINIO - Materiais da diluição não caem no Painel de Dispensação quando solicitados pela enfermagem

Arquivo: Sau/pep

## 12.1.2602.121

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22156]** Ajuste para remover interfaces desnecessarias

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Api.dll

* **[Ticket: DSAUGHASSIST-22156]** [FEAT] DSAUGHASSIST-22156 Ajuste dll para ambiente 3 camadas

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll

* **[Ticket: DSAUGHASSIST-21772]** Ajuste na mensagem de validação de bloqueio de 30 dias

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-21907]** DSAUGHASSIST-21907 Calendário

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-21955]** Ao confirmar um agendamento simplificado será salvo o numero cartão sus do paciente

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Intf.dll

* **[Ticket: DSAUGHASSIST-22137]** Ajuste para cores do calendario quando horario é especial

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25627]** Alterado para que após a seleção do procedimento na elaboração da AIH, caso o procedimento esteja vinculado a um único serviço e classificação, os respectivos campos já venham preenchidos automaticamente.

Arquivo: RM.Sau.Sus.Form.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-25421]** Parametrização do sistema para permitir alterar item que veio de requisição ou pedido de exames. Simula a auditoria interna.

Arquivos: RM.Sau.Faturamento.Server.dll; RM.Sau.Parametrizador.Form.dll; RM.Sau.Parametros.Data.dll; RM.Sau.Parametrizador.Intf.dll; RM.Sau.Cadastros.Intf.dll; RM.Sau.Faturamento.Intf.dll; RM.Sau.Parametros.Intf.dll; RM.Sau.AuditoriaInterna.Server.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.Parametrizador.Data.dll; RM.Sau.Faturamento.Data.dll

## 12.1.2602.122

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22137]** Ajuste para visão do calendario que exibe nenhum ou somente 1 mês

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-22156]** [FEAT] DSAUGHASSIST-22156 Ajuste dll para ambiente 3 camadas

Arquivos: RM.Sau.Server.dll; RM.Sau.Parametros.Intf.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Parametrizador.Intf.dll

### Rotina: ELABORAÇÃO DE BPA

* **[Ticket: DSAUGHFATF-25635]** Alterado para que a tela de elaboração de BPA carregue automaticamente o campo de carater do atendimento de acordo com a classificação utilizada no registro de atendimento.

Arquivos: RM.Sau.Sus.Data.dll; RM.Sau.Sus.Form.dll; RM.Sau.RegistroAtendimento.Form.dll

## 12.1.2602.123

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: DSAUCLINICA-14370]** Foi adicionada uma nova aba na busca de pacientes para exibir registros com pré-registro interno. Com essa melhoria, passa a ser possível criar agendas cirúrgicas para esses pacientes e utilizar o fluxo do painel de cirurgia, incluindo a dispensação de itens relacionados ao procedimento.

Arquivos: RM.Sau.Common.Data.dll; RM.Sau.Common.Form.dll; RM.Sau.Utils.Intf.dll; RM.Sau.AgendaCirurgia.Form.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22137]** Ajuste para visão do calendario que exibe nenhum ou somente 1 mês

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-22166]** Visualização de arquivos no agendamento simplificado de exame

Arquivos: RM.Sau.Utils.Server.Api.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Api.dll; RM.Sau.Utils.Server.dll

* **[Ticket: DSAUGHASSIST-22166]** Visualização e baixa de documentos agenda simplificada de exame

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22188]** DSAUGHASSIST-22188 Ajustes homologação 24\_03

Arquivo: Sau/saude-front

### Rotina: AVALIAÇÕES COMPLEMENTARES

* **[Ticket: DSAUPEPCONV-23244]** DSAUPEPCONV-23244 RÉPLICA para 12.1.2506 - LINK TELEMEDICINA REDIRECIONANDO PARA LOGIN DO PEP

Arquivo: Sau/pep

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25532]** Criação da central de críticas da AIH

Arquivos: RM.Sau.Sus.Data.dll; RM.Sau.Sus.Intf.dll; RM.Sau.Extensions.dll; RM.Sau.Sus.Form.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-25421]** Parametrização do sistema para permitir alterar item que veio de requisição ou pedido de exames. Simula a auditoria interna.

Arquivo: RM.Sau.Faturamento.Form.dll

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21918]** Ajustes parciais Orçamento para Cliente

Arquivos: RM.Sau.SmartX.OrcamentoCliente.Service.dll; RM.Sau.SmartX.Cadastros.Service.dll; RM.Sau.Server.dll; RM.Sau.ActionsHub.Shared.dll

### Rotina: RECURSO DE GLOSAS

* **[Ticket: 26828367 / DSAUGHFATF-25588]** Recurso de Glosa - Valores Divergentes

Arquivos: RM.Sau.GestaoGlosa.Form.dll; RM.Sau.GestaoGlosa.Server.dll

### Rotina: REGISTRO DE ATENDIMENTO

* **[Ticket: 26847089 / DSAUGHASSIST-21954]** Ajuste na verificação de agendamentos

Arquivo: Sau/saude-front

## 12.1.2602.124

### Rotina: Sem Rotina Específica

* **[Ticket: 27003673 / DSAUCLINICA-14443]** Ajuste na rotina de liberação de prescrição e solicitação de MAT/MED: ao validar o vínculo do usuário com o local de estoque, caso não exista vínculo direto, passa a ser verificado se o perfil do usuário (associado ao perfil de visualização de estoque) possui vínculo com algum local de estoque. Não havendo vínculo em nenhuma das duas situações, será exibida uma mensagem e o impedimento de liberação será mantido.

Arquivos: RM.Sau.Stock.Intf.dll; RM.Sau.Stock.Server.dll

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: 26862220 / DSAUGHASSIST-21995]** Ajuste realizado na pesquisa da especialidade conforme horário selecionado

Arquivos: RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Server.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22084]** Criação do tratamento de reagendamentos e agendamentocompl

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-22084]** Criação do tratamento de reagendamentos

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22084]** Processo de reagendamento do paciente

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22084]** DSAUGHASSIST-22084 US21 - Processo de reagendamento do paciente

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22084]** [FEAT] DSAUGHASSIST-22084 US21 - Processo de reagendamento do paciente

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-22087]** DSAUGHASSIST-22087 US22 - Cancelamento de agendamento de paciente

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22087]** Criação endpoint para excluir agendamento

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-22147]** Validação de e-mail no agendamento simplificado de exame

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.Utils.Intf.dll

* **[Ticket: DSAUGHASSIST-22198]** Inclusão de agendamentos perdidos no agendamento simplificado de exame

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-25543]** Ao encerrar parcial que voltou da remessa para correção, gera mensagem de divergencias de valores.

Arquivo: RM.Sau.Faturamento.Server.dll

* **[Ticket: DSAUGHFATF-25548]** Sistema ajustado para classificar as mensagens de críticas da AIH

Arquivos: RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Server.dll; RM.Sau.Utils.Intf.dll

* **[Ticket: DSAUGHFATF-25552]** Encerramento da conta do RN ao encerrar a conta da mãe

Arquivos: RM.Sau.Parametros.Intf.dll; RM.Sau.Parametrizador.Form.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Faturamento.Intf.dll; RM.Sau.Parametrizador.Intf.dll

* **[Ticket: DSAUGHFATF-25729]** Adicionado processo de cancelamento de atendimento na elaboração de contas

Arquivo: RM.Sau.Faturamento.Form.dll

### Rotina: IMPRESSÃO DE PARCIAIS EM LOTE

* **[Ticket: 26765640 / DSAUGHFATF-25526]** Na impressão de parciais por lote estava sumindo algumas contas pois elas não tinham relacionamento com Autorização. E em outra situação estava demorando o processamento.

Arquivos: RM.Sau.ExtratoConta.Server.dll; RM.Sau.ExtratoConta.Data.dll; RM.Sau.AuthorizationGuide.Server.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: DSAUGHFATF-25695]** Efetuado tratamento na adição das tabelas de materiais e medicamentos ao inserir um novo produto

Arquivos: RM.Sau.Produto.Data.dll; RM.Sau.Produto.Form.dll; RM.Sau.Autorizacao.Data.dll; RM.Sau.Utils.Intf.dll

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21918]** Ajuste no carregamento da tela de Sessão de Caixa no Orçamento para Clientes 2.0

Arquivos: RM.Sau.Faturamento.Intf.dll; RM.Sau.SmartX.OrcamentoCliente.Objetos.Service.dll; RM.Sau.SmartX.OrcamentoCliente.Service.dll; RM.Sau.Movimento.Service.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Api.dll; RM.Sau.ActionsHub.Shared.dll

* **[Ticket: DSAUGHASSIST-21918]** Ajuste de exibição de menu do Orçamento para Clientes 2.0

Arquivo: RM.Sau.Server.dll

### Rotina: RELATÓRIOS

* **[Ticket: 27002690 / DSAUPEPCONV-23309]** Correção no carregamento de campos do filtro de histórico de score

Arquivo: Sau/pep

## 12.1.2602.125

### Rotina: AGENDA DE CIRURGIAS - VISÃO

* **[Ticket: DSAUGHASSIST-22258]** [FEAT] DSAUGHASSIST-22258 Inclusão do manual do convênio antes da seleção do exame

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22258]** DSAUGHASSIST-22258 Inclusão do manual do convênio antes da seleção do exame

Arquivo: Sau/saude-front

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-21827]** Inclusão validação de celular no agendamento simplificado de exame

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22137]** Ajuste sobre movimentação de agendamentos entre especialidades diferentes e alguns gerando conflito com encaixes.

Arquivos: RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-22137]** Ajuste para visão do calendario que exibe nenhum ou somente 1 mês

Arquivos: RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Intf.dll

* **[Ticket: DSAUGHASSIST-22137]** Melhorada a validação que permite colocar agendamentos que possuem periodos concorrentes.

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: 27000188 / DSAUGHASSIST-22179]** Ajuste realizado quando o agendamento tem integração Sala/Prestador

Arquivos: RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll

* **[Ticket: DSAUGHASSIST-22198]** Ajuste agendamentos perdidos no agendamento simplificado de exame

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22214]** Ajuste na validação de Encaixe e na busca de horarios livres por mes

Arquivos: RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-22214]** Ajuste no status do encaixe na agenda simplificada

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22214]** Criação de validação de Encaixe

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-22214]** Ajuste na validação de Encaixe para periodos simultaneos

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Intf.dll

* **[Ticket: DSAUGHASSIST-22214]** Não exibir encaixe quando o status for bloqeuado na agenda simplificada

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22214]** Inclusão de encaixe na agenda simplificada de exame

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22227]** DSAUGHASSIST-22227 Excluir agendamento do carrinho não esta retornando para disponível

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22235]** [FIX] DSAUGHASSIST-22235 Ajuste observação situação

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22235]** DSAUGHASSIST-22235 Ajuste observação situação

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22236]** Inclusão de status no carrinho de agenda simplificada quando encaixe

Arquivo: Sau/saude-front

### Rotina: ANAMNESE

* **[Ticket: DSAUPEPCONV-22800]** DSAUPEPCONV-22800 [ Mauá ] Parametrização de dependência de ações

Arquivos: RM.Sau.Cadastros.Intf.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Cadastros.Server.dll; RM.Sau.Api.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Server.dll

* **[Ticket: DSAUPEPCONV-22801]** DSAUPEPCONV-22801 [ Mauá

Arquivo: Sau/pep

* **[Ticket: DSAUPEPCONV-22800]** DSAUPEPCONV-22800 [ Mauá

Arquivo: Sau/saude-front

### Rotina: APURAÇÃO DE PLANTÕES REALIZADOS

* **[Ticket: DSAUGHFATF-22922]** Quando existe mais de um valor de apuração de plantão no mesmo dia (valor do plantão e valor de bônus), o sistema realiza o lançamento do repasse corretamente, porém ao executar o processo de Liberação da apuração, somente um repasse é liberado.

Arquivo: RM.Sau.CadastrosFat.Server.dll

### Rotina: INTERNAÇÃO

* **[Ticket: 26472820 / DSAUGHASSIST-21809]** Ajuste no relatório com resultados dos exames e na exibição dos sub-itens do form que visualiza o resultado

Arquivo: RM.Sau.UnidadeDiagnostico.Resultado.Infraestrutura.Server.dll

### Rotina: MONITOR DE INTEGRAÇÃO

* **[Ticket: 26683554 / DSAUPEPCONV-23131]** DSAUPEPCONV-23131 [ HU

Arquivo: Sau/saude-front

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-23247]** Ajuste DrTis campo de acessKey foi removido

Arquivo: RM.Sau.UnidadeDiagnostico.Laudo.Integracao.Intf.dll

### Rotina: RECURSO DE GLOSAS

* **[Ticket: 26402611 / DSAUGHFATF-25288]** As melhorias estão sendo aplicadas nas versões de mercado

Arquivos: RM.Sau.Tiss.Application.Server.dll; RM.Sau.Tiss.Infraestrutura.Server.dll; RM.Sau.CadastrosFat.Intf.dll; RM.Sau.CadastrosFat.Form.dll; RM.Sau.Ans.Sever.dll; RM.Sau.Parametros.Intf.dll; RM.Sau.Utils.Server.dll

### Rotina: REGISTRO DE ATENDIMENTO

* **[Ticket: 26886635 / DSAUPEPCONV-23239]** DSAUPEPCONV-23239 Solicitação de internação - Campo de observação insuficiente para justificativa de internação

Arquivo: Sau/pep

### Rotina: SOROS E COMPONENTES

* **[Ticket: DSAUPEPCONV-22819]** DSAUPEPCONV-22819 [HBPSantos

Arquivo: Sau/pep

## 12.1.2602.126

### Rotina: AGENDA DE CIRURGIAS - VISÃO

* **[Ticket: DSAUGHASSIST-22258]** DSAUGHASSIST-22258 Inclusão do manual do convênio antes da seleção do exame

Arquivo: Sau/saude-front

* **[Ticket: 26910715 / DSAUGHASSIST-22029]** Ajuste nas especialidades do assistente de agendamento

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22084]** Ajuste na validação do reagendamento para desconsiderar seqagendamento anterior nas validações

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll

* **[Ticket: DSAUGHASSIST-22087]** DSAUGHASSIST-22087 US22 - Cancelamento de agendamento de paciente

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22087]** [FEAT] DSAUGHASSIST-22087 US22 - Cancelamento de agendamento de paciente

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25558]** Adicionada verificação ao editar a quantidade ou excluir um item da AIH quando é originado pelo estoque

Arquivos: RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Form.dll; RM.Sau.Sus.Data.dll

* **[Ticket: DSAUGHFATF-25685]** Cadastro de motivo de rejeição da AIH

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHFATF-25685]** Criação do cadastro de motivo de rejeição da AIH

Arquivos: RM.Sau.Sus.Server.dll; RM.Sau.Sus.Intf.dll; RM.Sau.Api.dll; RM.Sau.Sus.Form.dll

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: DSAUGHFATF-25544]** Estorno Automático de OPME na AIH por Devolução de Estoque.

Arquivo: RM.Sau.Produto.Server.dll

## 12.1.2602.127

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22084]** Ajuste no processo de reagendamento do paciente e de layout

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22235]** Incluido limite 255 caracteres na observação de situação agenda simplificada

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22283]** DSAUGHASSIST-22283 Inclusão de confirmação para cancelamento de agendamento.

Arquivo: Sau/saude-front

### Rotina: ATENDIMENTO SIMPLIFICADO - PACIENTE

* **[Ticket: DSAUGHASSIST-22290]** [FEAT] DSAUGHASSIST-22290 Limitar opções (TAG) disponíveis em situação.

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

* **[Ticket: DSAUGHASSIST-22290]** DSAUGHASSIST-22290 Limitar opções (TAG) disponíveis em situação.

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22297]** DSAUGHASSIST-22297 Filtro de Unidade não filtra datas disponiveis no calendario

Arquivo: Sau/saude-front

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25685]** Permissões de acesso do cadastro de motivo de rejeição da AIH

Arquivos: RM.Sau.Server.dll; RM.Sau.Api.dll; RM.Sau.Sus.Form.dll

### Rotina: FATURAMENTO IPASGO

* **[Ticket: 26905928 / DSAUGHFATF-25670]** Foi verificado que, quando o plano possui tabela de preço diferenciada para convênio de previdência, ao gerar o arquivo TXT de faturamento, o código levado no arquivo é o código próprio da tabela incorreta. Ou seja, não está sendo utilizado o código próprio da tabela de preços diferenciada, conforme esperado.

Arquivos: RM.Sau.Faturamento.Intf.dll; RM.Sau.Faturamento.Server.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: DSAUGHFATF-25703]** Atualização de múltiplas informações na Tela de Preços de Produtos com a atualização da codifficação e/ou descrição de acordo com a configuração de cada tabela de matmed

Arquivos: RM.Sau.Lib.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Produto.Form.dll; RM.Sau.Produto.Server.dll; RM.Sau.Produto.Intf.dll

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23270]** Configurado por parâmetro, permite a impressão automatica de exames ao LIBERAR a prescrição e ao imprimir uma LIBERAÇÃO de prescrição, se as mesmas tiverem solicitações de exames.

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Intf.dll

* **[Ticket: DSAUPEPCONV-23270]** Parametrização da Impressão de Solicitação de Exames

Arquivo: Sau/pep

## 12.1.2602.129

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUGHASSIST-21986]** DSAUGHASSIST-21986 Ausência de botão "Limpar" no campo Convênio

Arquivo: Sau/saude-front

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: DSAUGHASSIST-22309]** DSAUGHASSIST-22309 Filtro Unidade Horarios

Arquivo: Sau/saude-front

### Rotina: AGENDA DE CIRURGIAS - VISÃO

* **[Ticket: DSAUCLINICA-14471]** Ajuste na listagem do painel de cirurgia para que passe a exibir também as cirurgias que estão suspensas.

Arquivo: RM.Sau.Stock.Form.dll

* **[Ticket: DSAUCLINICA-14471]** Ajuste na listagem da agenda cirúrgica para que passe a exibir também as cirurgias que estão suspensas.

Arquivo: RM.Sau.AgendaCirurgia.Form.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22084]** DSAUGHASSIST-22084 US21 - Processo de reagendamento do paciente

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22308]** Ajuste realizado ao cancelar a primeira reserva

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-22310]** DSAUGHASSIST-22310 Ajuste campo "Disponibilidade por"

Arquivo: Sau/saude-front

### Rotina: ALTA

* **[Ticket: DSAUGHASSIST-21621]** Ajuste na validação quando o tipo de alta é alterado de óbito para qualquer outro

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: ATENDIMENTO SIMPLIFICADO - CONCLUSÃO

* **[Ticket: DSAUGHASSIST-22315]** Permitindo seleção de mais de um agendamento ao iniciar atendimento simplificado

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22315]** Atendimento simplificado não referenciando corretamente os agendamentos atrelados.

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.AuthorizationGuide.Server.dll; RM.Sau.AgendaAtendimento.Server.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25903]** Efetuada revisão nas validações ao inserir um procedimento na AIH

Arquivo: RM.Sau.Sus.Form.dll

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: DSAUGHFATF-25694]** Alteração no processo de cancelamento de AIH para permitir informar um motivo de rejeição previamente cadastrado e uma observação de texto livre

Arquivos: RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Server.dll; RM.Sau.Sus.Form.dll

### Rotina: FOLHA DE PRODUÇÃO DE PRESTADORES

* **[Ticket: DSAUGHFATF-25882]** Ao liberar algum repasse, o sistema solicita a informação de data de pagamento, onde deveria ser data de referência. Tanto é que grava a informação no campo referência.

Arquivo: RM.Sau.Repasse.Form.dll

### Rotina: MUDANÇA DE CATEGORIA DO PACIENTE

* **[Ticket: 27124520 / DSAUGHFATF-25812]** Efetuada revisão na mudança de categoria com relação ao tipo de cobrança para atendimentos SUS

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21810]** Ajuste no tamanho da sala pelo painel de exames

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.Parametrizador.Intf.dll; RM.Sau.RegistroAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-21810]** Ajuste do campo guiche/sala

Arquivos: Sau/portal-painel-chamadas; Sau/saude-front

* **[Ticket: DSAUGHASSIST-21810]** rollback da atleração do campo de sala e guiche

Arquivos: RM.Sau.Parametrizador.Intf.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Form.dll

### Rotina: PRESCRIÇÃO MÉDICA - CHECAGEM

* **[Ticket: 27032560 / DSAUPEPCONV-23431]** Correção no loading da tela de aprazamento

Arquivo: Sau/pep

### Rotina: RECURSO DE GLOSAS

* **[Ticket: 27031582 / DSAUGHFATF-25764]** Adicionado parâmetro "Soma Lançamento Fora da Conta no Recurso de Glosa" nas condições contratuais (Condições Contratuais ? Eletrônico III ? Aba Geral III) para controlar a exibição dos honorários fora da conta no relatório de Recurso de Glosa. Quando desabilitado, os lançamentos fora da conta não são somados no resumo.

Arquivos: RM.Sau.Faturamento.Form.dll; RM.Sau.CadastrosFat.Form.dll; RM.Sau.Parametros.Intf.dll; RM.Sau.CadastrosFat.Intf.dll

### Rotina: REGISTRO DE ATENDIMENTO

* **[Ticket: 27050607 / DSAUGHASSIST-22208]** Ajuste no filtro para trazer os horários ocupados na especialidade quando nao for permitido o conflito

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: USO GERAL

* **[Ticket: DSAUGHFATF-25560]** alterar componente do Codigo Sus para selecionar códigos pré-cadastrados

Arquivo: RM.Sau.Produto.Form.dll

## 12.1.2602.130

### Rotina: Sem Rotina Específica

* **[Ticket: 27242140 / DSAUGHASSIST-22356]** Ajuste realizado na exibição do botão das opções da agenda

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22198]** Nos agendamentos perdidos serão listados todos os agendamentos anteriores a hoje num intervalo de 30 dias. Agendamentos futuros serão considerados todos os agendamentos de hoje em diante

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-25478]** Efetuada revisão na central de autorizações com relação ao controle dos campos e guia de solicitação de internação

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Autorizacao.Form.dll; RM.Sau.Utils.Form.dll; RM.Sau.Extensions.dll; RM.Sau.AuthorizationGuide.Form.dll; RM.Sau.Autorizacao.Data.dll; RM.Sau.Autorizacao.Intf.dll; RM.Sau.Ans.Form.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25685]** Alteração nas rotas de API do cadastro de motivos de rejeição da AIH para que possam ser utilizadas nas demais versões.

Arquivos: RM.Sau.Api.dll; RM.Sau.Sus.Form.dll

* **[Ticket: DSAUGHFATF-25685]** Alteração para exibir corretamente a página de cadastro de motivos de rejeição da AIH

Arquivo: Sau/saude-front

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: 27149594 / DSAUGHFATF-25867]** Elaboração da AIH - Quantidade Excedida.

Arquivo: RM.Sau.Sus.Server.dll

### Rotina: FATURAMENTO TISS

* **[Ticket: DSAUGHFATF-25924]** Pequeno ajuste para que o faturamento de convenio seja executado corretamente.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: INTEGRAÇÕES LABORATORIAIS

* **[Ticket: DSAUGHASSIST-22386]** DrTis Ajuste no integraçao

Arquivos: RM.Sau.UnidadeDiagnostico.Laudo.Integracao.Intf.dll; RM.Sau.UnidadeDiagnostico.Laudo.Integracao.Server.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: 26911117 / DSAUGHFATF-25646]** Corrige itens de índice de preço que não constavam na última revista global.

Arquivos: RM.Sau.Produto.Data.dll; RM.Sau.Produto.Form.dll

* **[Ticket: DSAUGHFATF-25777]** Criação de parâmetro para permitir Atendimento Externo SUS simultâneo

Arquivos: RM.Sau.Cadastros.Intf.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Data.dll

### Rotina: RECEPÇÃO

* **[Ticket: 27041627 / DSAUGHASSIST-22207]** Realizado um ajuste para salvar como responsável o médico pediatra informado no cadastro do recém nascido

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Data.dll; RM.Sau.RegistroAtendimento.Intf.dll

### Rotina: REGISTRO E CONTROLE

* **[Ticket: DSAUPEPCONV-23496]** Ajuste na criação de uma nova unidade de atendimento

Arquivo: RM.Sau.Cadastros.Form.dll

## 12.1.2602.131

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUGHASSIST-21997]** DSAUGHASSIST-21997 Padronização de ordenação nos campos do agendamento

Arquivo: Sau/saude-front

### Rotina: APURAÇÃO DE PLANTÕES REALIZADOS

* **[Ticket: DSAUGHFATF-25698]** Na Rotina de Apuração de Plantões realizados, cria uma forma de inserir o cabeçalho, considerando os plantões cadastrados na tela de Registro de Plantões.

Arquivos: RM.Sau.CadastrosFat.Intf.dll; RM.Sau.CadastrosFat.Form.dll; RM.Sau.CadastrosFat.Server.dll

### Rotina: CADASTROS

* **[Ticket: 27220624 / DSAUGHFATF-25916]** Ajuste na rotina de cadastro de recém nascido.

Arquivo: RM.Sau.Common.Data.dll

### Rotina: CADASTROS SUS

* **[Ticket: DSAUGHFATF-25976]** Adaptação da trava de novo atendimento para validação tardia de convênio e tipo.

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.RegistroAtendimento.Data.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25661]** Ajuste realizado nas validações de permanencia longa permanencia SUS

Arquivos: RM.Sau.Sus.Server.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Sus.Intf.dll

### Rotina: FATURAMENTO DE CONVÊNIOS

* **[Ticket: 27276161 / DSAUGHFATF-25963]** Mesmo utilizando as configurações de agrupamento no XML para fatura de convênio nas condições contratuais o sistema não está agrupando corretamente, percebemos que ele está agrupando de 2 em 2 mesmo todos os procedimentos estando na mesma data.

Arquivo: RM.Sau.Tiss.Infraestrutura.Server.dll

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: DSAUGHFATF-25694]** Ajuste no novo processo de cancelamento de AIH.

Arquivos: RM.Sau.Sus.Server.dll; RM.Sau.Sus.Intf.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - VISÃO

* **[Ticket: 27185249 / DSAUCLINICA-14528]** Foi ajustado o comportamento ao cancelar um horário intermediário, que estava impactando indevidamente os horários subsequentes e gerando inconsistência ao tentar confirmar ou processar os próximos registros. Com a correção, o cancelamento passa a afetar apenas o horário selecionado, garantindo a integridade dos demais aprazamentos.

Arquivo: RM.Sau.Stock.Server.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: DSAUGHFATF-25662]** Efetuada correção ao utilizar API dos correios no endereço do paciente.

Arquivo: RM.Sau.Paciente.Form.dll

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21810]** Ajuste do campo guiche/sala

Arquivo: Sau/portal-painel-chamadas

* **[Ticket: DSAUGHASSIST-21810]** rollback da atleração do campo de sala e guiche

Arquivos: RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.Parametrizador.Intf.dll; RM.Sau.RegistroAtendimento.Form.dll

### Rotina: RESULTADOS DE EXAMES

* **[Ticket: DSAUGHASSIST-21848]** Adicionando a coluna de Data de nascimento

Arquivos: RM.Sau.UnidadeDiagnostico.Data.dll; RM.Sau.UnidadeDiagnostico.Intf.dll

## 12.1.2602.132

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22084]** Reagendamento deve gravar a novo agenda com status reagendado na agenda simplificada

Arquivo: Sau/saude-front

### Rotina: ATENDIMENTO SIMPLIFICADO - CONCLUSÃO

* **[Ticket: DSAUGHASSIST-22314]** Problema na gravação dos dados a guia

Arquivos: RM.Sau.UnidadeDiagnostico.Intf.dll; RM.Sau.AuthorizationGuide.Server.dll; RM.Sau.UnidadeDiagnostico.Server.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Intf.dll

* **[Ticket: DSAUGHASSIST-22314]** Ajuste na geração de guia ao incluir o primeiro procedimento

Arquivo: Sau/saude-front

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-25971]** Efetuada revisão nos processos da Central de Autorizações

Arquivos: RM.Sau.Tiss.Infraestrutura.Server.dll; RM.Sau.Autorizacao.Form.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Autorizacao.Data.dll; RM.Sau.Shared.dll

### Rotina: FOLHA DE PRODUÇÃO DE PRESTADORES

* **[Ticket: DSAUGHFATF-25895]** Ajuste para não exibir novamente a seleção de itens da folha de pagamento de prestadores quando os itens apresentados forem exatamente os mesmos selecionados na execução do processo.

Arquivo: RM.Sau.Repasse.Form.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23278]** cherry pick da DSAUPEPCONV-23277

Arquivo: Sau/pep

### Rotina: REGISTRO DE ATENDIMENTO

* **[Ticket: 27050607 / DSAUGHASSIST-22208]** Ajuste validação da agenda

Arquivos: RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Data.dll

### Rotina: RESULTADOS DE EXAMES

* **[Ticket: DSAUGHASSIST-22496]** Ajuste na abertura da tela de laudos que exibia mensagem invalida.

Arquivo: RM.Sau.UnidadeDiagnostico.Intf.dll

## 12.1.2602.133

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22088]** Períodos Especiais da Agenda

Arquivos: RM.Sau.Parametros.Intf.dll; RM.Sau.Parametros.Data.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.Utils.Intf.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-22088]** Período especial complementar

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-22084]** Exibir dados de autorização no detalhe do agendamentos futuros e perdidos no agendamento simplificado de exame

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; Sau/saude-front

### Rotina: CADASTROS SUS

* **[Ticket: DSAUGHFATF-25760]** Adicionar Raça Cor, Nacionalidade, e cartão do sus obrigatório quando selecionado SUS

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHFATF-25760]** criar api para nacionalidade

Arquivos: RM.Sau.Cadastros.Server.dll; RM.Sau.Api.dll; RM.Sau.Paciente.Server.dll; RM.Sau.Cadastros.Intf.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-25478]** Revisão nos componentes do form (dataset) da central de autorizações

Arquivo: RM.Sau.Autorizacao.Form.dll

### Rotina: EXAMES - RESULTADO DE EXAMES

* **[Ticket: DSAUPEPCONV-23139]** cherry-pick da 23277para a 2602

Arquivo: Sau/pep

* **[Ticket: DSAUPEPCONV-23139]** alinha segunda tabela de laudos

Arquivo: Sau/pep

* **[Ticket: DSAUPEPCONV-23139]** cherry pick da DSAUPEPCONV-23277

Arquivo: Sau/pep

### Rotina: EXAMES - SOLICITAÇÃO DE EXAMES

* **[Ticket: DSAUPEPCONV-23119]** Criação do campo de observação para solicitação de exames

Arquivo: Sau/pep

### Rotina: LIBERAÇÃO

* **[Ticket: 26798428 / DSAUGHFATF-25997]** Ao tentar suspender uma prescrição de especialista que possua um procedimento onde no cadastro desse procedimento existam 2 itens de débito distintos SUS, o sistema apresenta problemas.

Arquivo: RM.Sau.Sus.Data.dll

### Rotina: REPASSES

* **[Ticket: DSAUGHFATF-25785]** Alteração no cadastro de prestadores pertencentes a um grupo. Para maiores detalhes acessar a documentação https://tdn.totvs.com/x/Q-NTK

Arquivos: RM.Sau.Faturamento.Server.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.Faturamento.Intf.dll; RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Intf.dll; RM.Sau.CadastrosFat.Server.dll; RM.Sau.Cadastros.Form.dll

### Rotina: SCORES - OUTROS

* **[Ticket: DSAUPEPCONV-23307]** Scores: habilitar múltiplas seleções

Arquivo: Sau/pep

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23118]** Integração da Observação da Solicitação de Exame do PEP para a Unidade Diagnóstica (RM)

Arquivos: RM.Sau.UnidadeDiagnostico.Intf.dll; RM.Sau.UnidadeDiagnostico.Form.dll; RM.Sau.Pep.Server.dll; RM.Sau.UnidadeDiagnostico.Data.dll; RM.Sau.UnidadeDiagnostico.Server.dll

* **[Ticket: DSAUPEPCONV-23118]** DSAUPEPCONV-23118 [ BP

Arquivo: Sau/pep

## 12.1.2602.134

### Rotina: EXAMES - RESULTADO DE EXAMES

* **[Ticket: DSAUPEPCONV-23139]** expande ícone de cadeado para remover scroll horizontal

Arquivo: Sau/pep

* **[Ticket: DSAUPEPCONV-23139]** expande primeira coluna para corrigir quebra de ícone de assinatura

Arquivo: Sau/pep

### Rotina: FOLHA DE PRODUÇÃO DE PRESTADORES

* **[Ticket: DSAUGHFATF-25896]** Alteração para permitir incluir uma observação na folha de pagamento de prestadores e enviá-la ao back-office.

Arquivos: RM.Sau.Movimento.Service.dll; RM.Sau.Repasse.Intf.dll; RM.Sau.Repasse.Form.dll; RM.Sau.Repasse.Data.dll; RM.Sau.Repasse.Server.dll; RM.Sau.Interfaces.Intf.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23548]** Tratativa de bloqueio de botão quando item de mat/med tem origem em prescrição medica

Arquivo: RM.Sau.Pep.Intf.dll

## 12.1.2602.135

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23548]** Tratativa de bloqueio de botão quando item de mat/med tem origem em prescrição medica

Arquivos: RM.Sau.Facade.dll; RM.Sau.Stock.Intf.dll; RM.Sau.Stock.Server.dll

## 12.1.2602.136

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22088]** Implementado encaixe em agendamento em horarios especiais

Arquivos: RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: APURAÇÃO DE PLANTÕES REALIZADOS

* **[Ticket: DSAUGHFATF-25698]** Na Rotina de Apuração de Plantões realizados, cria uma forma de inserir o cabeçalho, considerando os plantões cadastrados na tela de Registro de Plantões.

Arquivo: RM.Sau.CadastrosFat.Form.dll

### Rotina: ATENDIMENTO SIMPLIFICADO - CONCLUSÃO

* **[Ticket: 26843236 / DSAUGHASSIST-22270]** Ajuste realizado no geração do responsável financeiro quando o mesmo é estrangeiro

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: 27393929 / DSAUGHFATF-26032]** Adaptação da trava de novo atendimento para validação tardia de convênio e tipo.

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: 27272382 / DSAUGHFATF-25964]** A correção garante que, ao reprocessar, os dados anteriores sejam removidos, permitindo que o faturamento seja realizado normalmente.

Arquivos: RM.Sau.Faturamento.Server.dll; RM.Sau.Tiss.Infraestrutura.Server.dll

### Rotina: FOLHA DE PRODUÇÃO DE PRESTADORES

* **[Ticket: DSAUGHFATF-25894]** Incluir filtro de pesquisas na tela de folha de pagamento de prestadores

Arquivo: RM.Sau.Repasse.Form.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23548]** SQL - unidade selecionada incorreta

Arquivo: Sau/pep

* **[Ticket: DSAUPEPCONV-23548]** Tratativa de bloqueio de botão quando item de mat/med tem origem em prescrição medica

Arquivos: RM.Sau.Facade.dll; RM.Sau.Stock.Server.dll

* **[Ticket: DSAUPEPCONV-23593]** Ajuste das correções após rollback

Arquivo: Sau/pep

### Rotina: PEDIDO DE EXAMES

* **[Ticket: 26842521 / DSAUGHASSIST-22250]** Ajuste realizado para habilitar checkbox referente a Material pendente para exames executados dentro da instituição

Arquivo: RM.Sau.UnidadeDiagnostico.Form.dll

### Rotina: USO GERAL

* **[Ticket: 26432878 / DSAUGHFATF-26043]** Ajuste no método PreencheDadosAIH para considerar pacientes com sexo indeterminado na geração do arquivo AIH do SUS, conforme layout esperado pelo SIH/SUS

Arquivos: RM.Sau.Lib.dll; RM.Sau.Sus.Server.dll

## 12.1.2602.137

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22088]** Implementado encaixe em agendamento em horarios especiais

Arquivos: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll; RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: DSAUGHASSIST-22214]** Validação de existe agendamento no mesmo horario de encaixe

Arquivo: Sau/saude-front

### Rotina: APURAÇÃO DE PLANTÕES REALIZADOS

* **[Ticket: DSAUGHFATF-26008]** Processo para alteração da data do período de plantão apenas para itens selecionados no grid. Hoje ao alterar a data é alterado para todos os itens.

Arquivos: RM.Sau.RegistroAtendimento.Data.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.RegistroAtendimento.Intf.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25602]** Criação rotina de lançamento automático de diária.

Arquivos: RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Server.dll; RM.Sau.CrossCutting.dll; RM.Sau.CadastrosFat.Intf.dll; RM.Sau.Sus.Form.dll; RM.Sau.Sus.Data.dll

### Rotina: EVOLUÇÃO

* **[Ticket: 26665078 / DSAUPEPCONV-23085]** DSAUPEPCONV-23085 12.1.2506 - Nomenclatura "Médico solicitante:" na aba Evolução

Arquivo: Sau/pep

### Rotina: GLOSAS

* **[Ticket: 27330717 / DSAUGHFATF-26024]** Sistema ajustado para não exibir motivos de pendência para coligadas diferentes.

Arquivo: RM.Sau.Faturamento.Form.dll

### Rotina: MAPA DE DISPENSAÇÃO

* **[Ticket: 27392539 / DSAUCLINICA-14594]** Ajuste na busca de lote, localizada na movimentação de estoque, com o objetivo de melhorar a performance.

Arquivo: RM.Sau.Produto.Server.dll

### Rotina: PLANO TERAPÊUTICO

* **[Ticket: DSAUPEPCONV-23621]** ajusta painel plano terapeutico

Arquivo: Sau/pep

### Rotina: RECEPÇÃO

* **[Ticket: 27260670 / DSAUGHASSIST-22402]** Ajuste realizado na criação do atendimento a partir da agenda quando o convênio é alterado

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.RegistroAtendimento.Server.dll

## 12.1.2602.138

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: 26857490 / DSAUGHFATF-25595]** Sistema ajustado para calcular o resumo corretamente na execução do relatório de Guias ANS TISS

Arquivos: RM.Sau.Faturamento.Server.dll; RM.Sau.Faturamento.Intf.dll; RM.Sau.Faturamento.Form.dll

### Rotina: USO GERAL

* **[Ticket: 27450960 / DSAUGHFATF-26091]** Sistema ajustado para carregar as nacionalidades corretamente quando base de dados Oracle.

Arquivo: RM.Sau.Cadastros.Server.dll

## 12.1.2602.139

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22607]** [FIX] DSAUGHASSIST-22607 - Confirmação de agendamento. Datas com DateTime.Min onde deveria aceitar null

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: CIRURGIAS - STATUS DO AGENDAMENTO

* **[Ticket: DSAUCLINICA-14565]** Foi incluída, no caminho Cadastro > Cuidados com o Paciente > Cirurgia, uma nova opção de menu que permite ao usuário cadastrar e gerenciar os status da agenda cirúrgica.

Arquivos: RM.Sau.AgendaCirurgia.Form.dll; RM.Sau.Server.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-26025]** Adicionadas verificações ao alterar ou excluir procedimento da elaboração de AIH, caso o mesmo seja originado Evolução Clínica do PEP.

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Form.dll

### Rotina: MOTIVO DE RESERVA DE LEITO - CADASTRO

* **[Ticket: DSAUGHFATF-25845]** Criado cadastro de Tipo de Evolução

Arquivos: RM.Sau.Cadastros.Intf.dll; RM.Sau.Server.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Data.dll; RM.Sau.Utils.Server.dll

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-21811]** Atualização do nome do paciente no painel de chamadas

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.Paciente.Server.Api.dll; RM.Sau.AgendaAtendimento.Server.dll

## 12.1.2602.140

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22607]** [FEAT] DSAUGHASSIST-22607 ajuste convenio com busca por paciente

Arquivos: RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimentoCustomizada.Intf.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll

* **[Ticket: DSAUGHASSIST-22607]** DSAUGHASSIST-22607 Confirmar agendamentos

Arquivo: Sau/saude-front

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-26025]** Adicionadas verificações ao alterar ou excluir procedimento da elaboração de AIH, caso o mesmo seja originado Evolução Clínica do PEP.

Arquivos: RM.Sau.Sus.Data.dll; RM.Sau.Sus.Intf.dll

## 12.1.2602.141

### Rotina: Sem Rotina Específica

* **[Ticket: 27102653 / DSAUGHFATF-25888]** Sistema apresentando problema ao tentar faturar remessa do convênio IPSEMG usando a versão TISS 3.03.03

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: LIBERAÇÃO

* **[Ticket: 27424768 / DSAUPEPCONV-23619]** Ajuste para atualizar a tela de aprazamento após reaprazar

Arquivo: Sau/pep

* **[Ticket: 27424768 / DSAUPEPCONV-23619]** Ajuste para atualizar a checkagem após atualizar

Arquivo: Sau/pep

### Rotina: RECEPÇÃO

* **[Ticket: 27367623 / DSAUGHASSIST-22511]** Atendimento simplificado agora permite selecionar agendamentos com convênios diferentes

Arquivo: Sau/saude-front

* **[Ticket: 27367623 / DSAUGHASSIST-22511]** Hoje o atendimento simplificado exibe um modal contendo os agendamentos do paciente para o mesmo dia.

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: 27367623 / DSAUGHASSIST-22511]** Após selecionar dois agendamentos no atendimento simplificado o mesmo alterava o convênio dos dois agendamentos.

Arquivo: Sau/saude-front

## 12.1.2602.142

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22558]** Trazer os dados do convenio e plano do ultimo atendimento a consulta de paciente no agendamento simplificado

Arquivos: RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll

* **[Ticket: DSAUGHASSIST-22558]** Poder informar multiplas carteirinhas no agendamento simplificado

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22646]** [FIX] DSAUGHASSIST-22646 Tela travando ao adicionar exame de 1 em 1 minuto

Arquivo: RM.Sau.AgendaAtendimentoCustomizada.Server.Api.dll

### Rotina: ELETIVOS

* **[Ticket: DSAUPEPCONV-22756]** DSAUPEPCONV-22756 [ Mauá

Arquivo: Sau/pep

### Rotina: HISTÓRICO DE ATENDIMENTO

* **[Ticket: DSAUPEPCONV-23448]** Adição da coluna grupo profissional no histórico de atendimento

Arquivo: Sau/pep

### Rotina: INTERNAÇÃO

* **[Ticket: DSAUGHASSIST-20474]** Ajuste no cadastro do recém nascido onde não estava liberando o leito quando o cadastramento é cancelado

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.RegistroAtendimento.Form.dll

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23316]** Tempo do alerta de exame em tela

Arquivo: Sau/pep

## 12.1.2602.143

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-26031]** Sincronização com a versão 2602

Arquivos: RM.Sau.Sus.Server.dll; RM.Sau.Sus.Intf.dll; RM.Sau.Utils.Intf.dll

### Rotina: FATURAMENTO TISS

* **[Ticket: 27221068 / DSAUGHFATF-26044]** Atualmente, para o correto faturamento dos atendimentos, foi necessária a criação de dois parâmetros distintos: Interno e Externo.Para os atendimentos internos (guia de resumo de internação), é necessário acessar a condição contratual do convênio e desmarcar o parâmetro "Tratar pacote como procedimento". Dessa forma, o pacote lançado na conta será enviado no XML dentro da tag de Outras Despesas, utilizando a tabela adequada.Já para os atendimentos externos, é preciso retornar à condição contratual e marcar novamente o parâmetro "Tratar pacote como procedimento", garantindo que o pacote seja enviado como procedimento no XML.

Arquivos: RM.Sau.Tiss.Infraestrutura.Server.dll; RM.Sau.Ans.Sever.dll; RM.Sau.Tiss.Application.Server.dll; RM.Sau.FaturamentoConvenio.Server.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.CadastrosFat.Form.dll; RM.Sau.Parametros.Intf.dll

### Rotina: RECEPÇÃO

* **[Ticket: 27367623 / DSAUGHASSIST-22511]** Atendimento simplificado depois de registrar e fechar o atendimento e abrir novamente o RM imprimia uma mensagem invalida.

Arquivo: Sau/saude-front

### Rotina: REGISTRO DE ATENDIMENTO

* **[Ticket: 26886608 / DSAUGHFATF-25797]** Ao realizar ao acessar a tela de encerramento de contas sem débitos, as parciais de pacientes internados que ainda não receberam alta não estão sendo listados, mesmo atendendo a condição de não possuir débitos.

Arquivo: RM.Sau.Faturamento.Data.dll

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23318]** Parametrização de Prioridade Default para Exames - Solicitação de Exames

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Cadastros.Intf.dll

* **[Ticket: DSAUPEPCONV-23318]** DSAUPEPCONV-23318 [ Mauá

Arquivo: Sau/pep

### Rotina: SOROS E COMPONENTES

* **[Ticket: DSAUPEPCONV-23702]** DSAUPEPCONV-23702 Cypress E2E - Refactory

Arquivo: Sau/pep

## 12.1.2602.144

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25853]** Automação de Lançamento via Gatilho Assistencial.

Arquivos: RM.Sau.Sus.Server.dll; RM.Sau.Pep.Server.dll; RM.Sau.Cadastros.Intf.dll; RM.Sau.Pep.Intf.dll; RM.Sau.Sus.Data.dll; RM.Sau.CadastrosFat.Intf.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-26103]** Ao lançar um kit de lançamentos, e caso algum item não exista na tabela do convênio, o sistema apresenta mensagem valor zerado e não lança os demais itens. O correto é ignorar o que não consta na tabela e lançar os demais e Alteração de um label - DataReferencia Aba Liberação de Repasse.

Arquivos: RM.Sau.Faturamento.Server.dll; RM.Sau.Repasse.Form.dll

### Rotina: KANBAN DE HIGIENIZAÇÃO DE LEITOS - MOVIMENTAÇÃO DE LEITO

* **[Ticket: 27187279 / DSAUGHASSIST-22501]** Criado uma validação para que se caso ja existir uma higienização ATIVA para aquele leito, não inserir novamente e manter o estado da higienização já em andamento, assim resolvendo o problema das higienizações duplicadas no kanban

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

### Rotina: MOTIVO DE RESERVA DE LEITO - CADASTRO

* **[Ticket: DSAUGHFATF-25854]** Remover Procedimento SUS quando suspender, ou cancelar uma evolucao

Arquivos: RM.Sau.Pep.Server.dll; RM.Sau.Pep.Intf.dll

### Rotina: MOVIMENTO (RT)

* **[Ticket: 26393811 / DSAUGHFATF-25484]** Sistema ajustado para verificar o registro de Integração Relacionamento do menu Utilitarios para mapear corretamente os paises entre os sistemas.

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Integracoes.Intf.dll; RM.Sau.Movimento.Service.dll; RM.Sau.Integracoes.Server.dll

### Rotina: UNIDADE DE ATENDIMENTO - ABA FARMÁCIA

* **[Ticket: 26411602 / DSAUGHASSIST-21681]** Ajuste no cadastro da estação de trabalho para se comportar conforme a configuração nos parâmetros onde o cadastro é identifaco como usuário ou estação de trabalho

Arquivo: RM.Sau.Parametrizador.Form.dll

## 12.1.2602.145

### Rotina: Sem Rotina Específica

* **[Ticket: 27102653 / DSAUGHFATF-26167]** Ao emitir xml de Guia da TISS IPSEMG gerava problema.

Arquivo: RM.Sau.Ans.Sever.dll

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: 26515006 / DSAUGHASSIST-22385]** Alteração correta de status de agendamento

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22088]** Exibição dos horários disponíveis no assistente de agendamento

Arquivos: RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Server.dll

* **[Ticket: 27276123 / DSAUGHASSIST-22446]** Foi realizado um ajuste na forma que o sistema identifica a chave para uma nova configuração

Arquivos: RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.Cadastros.Server.dll

* **[Ticket: DSAUGHASSIST-22646]** DSAUGHASSIST-22646 Tela travando ao adicionar exame de 1 em 1 minuto

Arquivo: Sau/saude-front

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: 27239120 / DSAUGHFATF-25915]** Efetuado tratamento para utilizar o fabricante do lançamento especial na geração do XML de faturamento.

Arquivos: RM.Sau.Ans.Sever.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.FaturamentoConvenio.Server.dll

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: DSAUGHFATF-25813]** Implementar o lançamento automático de diárias de acompanhante para AIHs SUS, identificando o perfil do paciente (idoso, criança ou gestante) e calculando a quantidade correta com base nos dias de internação, UTI e adicional de óbito. Reduz glosas de quantidade e aumenta o aproveitamento da receita.

Arquivos: RM.Sau.Sus.Server.dll; RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Form.dll

### Rotina: HISTÓRICO DE ATENDIMENTO

* **[Ticket: 26734038 / DSAUPEPCONV-23349]** DSAUPEPCONV-23349 Visualização da triagem na tela do Histórico não funciona

Arquivo: Sau/pep

### Rotina: PAINEL DE CIRURGIAS - EDIÇÃO

* **[Ticket: DSAUGHFATF-26106]** Processo de cancelamento de cirurgia.

Arquivo: RM.Sau.AgendaCirurgia.Form.dll

## 12.1.2602.146

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22088]** Ajuste para não bloquear indevidamento horários em agendamentos com período especial com duração menor que a duração do período padrão

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

## 12.1.2602.147

### Rotina: AGENDAMENTO

* **[Ticket: 27707540 / DSAUGHASSIST-22718]** Ajustado as consultas da API de agendamentos para retornar os valores corretos.

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: 27286004 / DSAUCLINICA-14618]** Ajuste na rotina de checagem, implementado bloqueio para impedir a checagem de itens que ainda não foram dispensados pela farmácia.

Arquivo: RM.Sau.Pep.Server.dll

## 12.1.2602.148

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: 27068843 / DSAUGHFATF-25970]** Ao tentar gerar o movimento no backoffice na geração do pedido de NF de paciente veio via importação

Arquivo: RM.Sau.Movimento.Service.dll

## 12.1.2602.149

### Rotina: Sem Rotina Específica

* **[Ticket: 27437008 / DSAUCLINICA-14643]** Ajuste no painel de dispensação para que, no filtro de locais de estoque, sejam exibidos apenas os locais aos quais o usuário logado possui permissão de acesso.

Arquivos: RM.Sau.Stock.Form.dll; RM.Sau.Stock.Intf.dll; RM.Sau.Stock.Server.dll

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23305]** Parametrização de Prioridade Default para Exames - Prescrição

Arquivos: RM.Sau.Cadastros.Intf.dll; RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Form.dll

* **[Ticket: DSAUPEPCONV-23305]** Parametrização de Prioridade

Arquivo: Sau/pep

## 12.1.2602.150

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: 27293181 / DSAUGHASSIST-22425]** Ajuste na busca interna por especialidades no agendamento

Arquivos: RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Data.dll

### Rotina: CONDIÇÕES FINANCEIRAS

* **[Ticket: 27953502 / DSAUGHFATF-26166]** Foi retirado do calculo para definição de longa permanência as diarias de UTI que estavam indevidamente sendo adicionadas no alerta.

Arquivo: RM.Sau.Sus.Server.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-25776]** Central de críticas da AIH

Arquivos: RM.Sau.Sus.Intf.dll; RM.Sau.Sus.Server.dll; RM.Sau.Server.dll; RM.Sau.Sus.Form.dll

### Rotina: FATURAMENTO SUS AIH

* **[Ticket: DSAUGHFATF-26017]** Adicionado campo "Código Diária UTI SIGTAP" no cadastro de leitos

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Intf.dll

### Rotina: ORÇAMENTO PARA CLIENTES

* **[Ticket: DSAUGHFATF-26211]** Remoção do menu orçamento para clientes 2.0

Arquivos: RM.Sau.ActionsHub.Shared.dll; RM.Sau.Server.dll

### Rotina: RECEPÇÃO

* **[Ticket: 27675587 / DSAUGHFATF-26119]** Valores Padrão para atendimento TISS não está sendo puxado para a tela do registro de atendimento

Arquivos: RM.Sau.Ans.Sever.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.CadastrosAns.Data.dll

## 12.1.2602.151

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: 27164435 / DSAUGHASSIST-22447]** Ajuste na validade da elegibilidade não permitindo a criação tanto o agendamento quanto o atendimento

Arquivos: RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: 27293181 / DSAUGHASSIST-22425]** Ajuste na busca interna por especialidades no agendamento

Arquivos: RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Form.dll

### Rotina: ANÁLISE DE PRESCRIÇÕES - EDIÇÃO

* **[Ticket: 28105675 / DSAUPEPCONV-23784]** Ajuste o solicitar MAT/MED com quantidade maior que 1

Arquivo: RM.Sau.Stock.Server.dll

### Rotina: MEDICAMENTO

* **[Ticket: 28055737 / DSAUPEPCONV-23774]** Ajuste no lançamento de diluentes do tipo material.

Arquivo: RM.Sau.Produto.Server.dll

## 12.1.2602.152

### Rotina: AGENDAMENTO

* **[Ticket: 27359557 / DSAUGHASSIST-22552]** Foi alterado a forma com que envia o e-mail para ficar igual ao enviado pela agenda

Arquivos: RM.Sau.Portal.Agenda.Server.dll; RM.Sau.Portal.Agenda.Service.dll

* **[Ticket: 27963457 / DSAUCLINICA-14686]** Na agenda de cirurgia, ao buscar as salas, são exibidas apenas as salas pertencentes à unidade em que o usuário possui perfil, ou salas que não estejam vinculadas a nenhuma unidade de atendimento, desde que o parâmetro responsável por essa configuração esteja ativado.

Arquivos: RM.Sau.Api.dll; RM.Sau.AgendaCirurgia.Intf.dll; RM.Sau.AgendaCirurgia.Data.dll; RM.Sau.AgendaCirurgica.Server.dll

### Rotina: ANAMNESE

* **[Ticket: DSAUPEPCONV-23735]** DSAUPEPCONV-23735 Habilitar DTA Voice

Arquivo: Sau/pep

### Rotina: ATENDIMENTO SIMPLIFICADO - CONCLUSÃO

* **[Ticket: DSAUGHASSIST-22791]** Agenda de atendimento não estava validando encaixe quando pesquisava paciente.

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.Sus.Server.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Form.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-26145]** Tela Guia Autorização da Elaboração de Contas a data esta como obrigatoria

Arquivos: RM.Sau.Autorizacao.Form.dll; RM.Sau.Autorizacao.Intf.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-26016]** Geração automática de diárias de UTI na AIH a partir das movimentações de leito do paciente, com validações de procedimento principal, idade, quantidade máxima e dias de internação.

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Sus.Intf.dll; RM.Sau.Lib.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.Sus.Server.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: DSAUGHFATF-26257]** DSAUGHFATF-26257 Criar um parâmetro geral para habilitar o uso de faixa de codificação de produtos na Nota Fiscal.

Arquivos: RM.Sau.Parametrizador.Intf.dll; RM.Sau.Parametrizador.Form.dll; RM.Sau.Parametrizador.Data.dll

* **[Ticket: DSAUGHFATF-26262]** Emissão de NF baseada em Faixa de Codificação (Flexibilização de Validação)

Arquivos: RM.Sau.Tesouraria.Server.dll; RM.Sau.Parametrizador.Intf.dll

### Rotina: FATURAMENTO TISS

* **[Ticket: 27977013 / DSAUGHFATF-26183]** Efetuada revisão na validação de guias ao encerrar parcial

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: FOLHA DE PRODUÇÃO DE PRESTADORES

* **[Ticket: DSAUGHFATF-26234]** Alterar a nomenclatura dos créditos criados pela apuração de plantões realizados. SUGESTÃO: Plantão - <PSI - PRONTO SOCORRO INFANTIL> - <Pediatria> - NOME DO MÉDICO DO PLANTÃO

Arquivo: RM.Sau.CadastrosFat.Server.dll

### Rotina: IMPORTAÇÃO SIMPRO

* **[Ticket: 27350785 / DSAUGHFATF-26030]** Ajuste para que o histórico de atualização de preços SIMPRO apresente a data de início da vigência do item atualizado ao invés da data em que a atualização foi realizada no sistema.

Arquivo: RM.Sau.Produto.Server.dll

### Rotina: ORÇAMENTO PARA CLIENTES

* **[Ticket: 27181006 / DSAUGHFATF-25883]** Adicionadas novas verificações no responsável financeiro pelo paciente, caso o mesmo seja menor de idade.

Arquivos: RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.Cadastros.Server.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Extensions.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.RegistroAtendimento.Form.dll

## 12.1.2602.153

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 28076017 / DSAUPEPCONV-23775]** Ajuste diluentes multiplicando no MAT/MED

Arquivos: RM.Sau.Utils.Intf.dll; RM.Sau.Produto.Server.dll; RM.Sau.Produto.Intf.dll; RM.Sau.Stock.Server.dll; RM.Sau.Pep.Intf.dll

* **[Ticket: 28076017 / DSAUPEPCONV-23775]** Ajuste na multiplicação dos diluentes na solicitação MAT/MED

Arquivo: RM.Sau.Stock.Server.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE

* **[Ticket: 28165154 / DSAUCLINICA-14695]** Ajuste na rotina de inclusão de produtos pertencentes ao composto, utilizada na nova requisição de movimentação de estoque. Quando estiver habilitada a configuração de recuperação automática de lotes pelo método PEPS, os itens controlados por lote deverão ter suas informações de lote preenchidas automaticamente com base no lote retornado pelo PEPS.

Arquivos: RM.Sau.Produto.Intf.dll; RM.Sau.Produto.Server.dll; RM.Sau.Produto.Form.dll

* **[Ticket: 28165154 / DSAUCLINICA-14695]** DSAUCLINICA-14727\DSAUCLINICA-14695 :: Ajuste na rotina de inclusão de produtos pertencentes ao composto, utilizada na nova requisição de movimentação de estoque. Quando estiver habilitada a configuração de recuperação automática de lotes pelo método PEPS, os itens controlados por lote deverão ter suas informações de lote preenchidas automaticamente com base no lote retornado pelo PEPS.

Arquivo: RM.Sau.Produto.Form.dll

## 12.1.2602.154

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22946]** [FIX] DSAUGHASSIST-22946 Validação de período especial como destino

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

* **[Ticket: DSAUGHASSIST-22954]** DSAUGHASSIST-22954 Filtro dos anexos por agendamento. (VILELA)

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHASSIST-22967]** DSAUGHASSIST-22967 Item incluído no carrinho (agenda simplificada)

Arquivo: Sau/saude-front

### Rotina: AGENDAS

* **[Ticket: 28361138 / DSAUGHASSIST-22945]** [FIX] DSAUGHASSIST-22945 Nova Agenda Simplificada – Unidade em branco

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

## 12.1.2602.155

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-22976]** Ajuste na busca da especialidade na API do agendamento

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: MEDICAMENTO

* **[Ticket: DSAUPEPCONV-23406]** Remove o campo Justificativa se ele estiver apenas associado a itens Liberados com Ressalva

Arquivo: Sau/pep

### Rotina: SOROS E COMPONENTES

* **[Ticket: DSAUPEPCONV-23702]** DSAUPEPCONV-23702 Cypress E2E - Refactory

Arquivo: Sau/pep-e2e

## 12.1.2602.156

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 27212606 / DSAUPEPCONV-23526]** Associar um MAT/MED o sistema não permite a alteração de unidade do medicamento

Arquivo: RM.Sau.Stock.Server.dll

## 12.1.2602.157

### Rotina: ATENDIMENTO SIMPLIFICADO - PACIENTE

* **[Ticket: 28301005 / DSAUGHASSIST-22916]** Ajuste no bloqueio de horários

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: ATENDIMENTO SIMPLIFICADO - PAGAMENTO

* **[Ticket: DSAUGHFATF-25762]** Ajustes no atendimento simplificado para que seja possível realizar atendimentos do SUS

Arquivo: Sau/saude-front

### Rotina: AUTORIZAÇÕES

* **[Ticket: 27990626 / DSAUGHFATF-26208]** Relatório ajustado e liberado a impressão de guias de outas despesas no módulo de registro de atendimento.

Arquivo: RM.Sau.AuthorizationGuide.Intf.dll

### Rotina: CADASTROS SUS

* **[Ticket: DSAUGHFATF-25763]** adicionar campus SUS em conclusão

Arquivo: Sau/saude-front

* **[Ticket: DSAUGHFATF-25763]** pular pagamento e informar sus na conclusão do atendimento simplificado

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: 28133284 / DSAUGHFATF-26236]** Relatório ajustado e liberado a impressão de guias de outas despesas no módulo de registro de atendimento.

Arquivo: RM.Sau.AuthorizationGuide.Intf.dll

### Rotina: ELETIVOS

* **[Ticket: 26973040 / DSAUGHASSIST-22773]** mensagem de retorno 500 ao abrir telas em angular em abiente 2 camadas sou t-cloud

Arquivo: RM.Sau.RegistroAtendimento.Server.dll

### Rotina: FATURAMENTO TISS

* **[Ticket: 28104243 / DSAUGHFATF-26235]** Ajuste para exibir a opção de imprimir a guia de outras despesas apenas se houverem outras despesas na conta.

Arquivos: RM.Sau.FaturamentoConvenio.Server.dll; RM.Sau.Tiss.Infraestrutura.Server.dll; RM.Sau.AuthorizationGuide.Intf.dll; RM.Sau.AuthorizationGuide.Server.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.Tiss.Application.Server.dll; RM.Sau.FaturamentoConvenio.Intf.dll; RM.Sau.Extensions.dll

* **[Ticket: DSAUGHFATF-26311]** Foi criado o parâmetro “Usa a hora inicial e final da Taxa/Serviço no XML” que, quando habilitado, efetua o preenchimento da hora inicial e final conforme cadastro da taxa/serviço da conta.

Arquivos: RM.Sau.Parametros.Intf.dll; RM.Sau.CadastrosFat.Form.dll; RM.Sau.Ans.Sever.dll; RM.Sau.Tiss.Infraestrutura.Server.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE

* **[Ticket: 28133311 / DSAUCLINICA-14692]** Ajuste na tela de requisição do paciente, na requisição do paciente, foi adicionado o botão “Suspender Item”. Esse botão será exibido apenas quando a requisição tiver sido criada a partir de uma solicitação de exame. Será possível suspender os itens oriundo da solicitação de exame.

Arquivos: RM.Sau.Stock.Data.dll; RM.Sau.Stock.Form.dll; RM.Sau.Stock.Intf.dll; RM.Sau.Stock.Server.dll

### Rotina: ONCOLOGIA - QUIMIOTERAPIA

* **[Ticket: 26512006 / DSAUPEPCONV-23696]** Parâmetro de Cálculo de Superfície Corporal

Arquivos: RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Data.dll; Sau/pep; RM.Sau.Cadastros.Intf.dll; RM.Sau.Utils.Intf.dll

### Rotina: ORÇAMENTO PARA CLIENTES

* **[Ticket: 28116810 / DSAUGHFATF-26230]** Efetuada revisão nos parâmetros referentes a orçamentos

Arquivo: RM.Sau.Parametrizador.Form.dll

### Rotina: OUTROS CADASTROS

* **[Ticket: DSAUGHFATF-26310]** DSAUGHFATF-26310 - No controle de documentos, criar uma forma de retirar um documento de um malote.

Arquivos: RM.Sau.ControleDocumentos.Intf.dll; RM.Sau.ControleDocumentos.Data.dll; RM.Sau.ControleDocumentos.Form.dll

### Rotina: SOROS E COMPONENTES

* **[Ticket: DSAUPEPCONV-23702]** DSAUPEPCONV-23702 Cypress E2E - Refactory

Arquivo: Sau/pep-e2e

## 12.1.2602.158

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUGHFATF-26207]** Quebra ao informar o numero do prestador TISS

Arquivo: RM.Sau.AuthorizationGuide.Data.dll

### Rotina: AGENDAMENTO

* **[Ticket: 28302178 / DSAUGHASSIST-22903]** Ajuste de regra interna

Arquivos: RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll

### Rotina: ATENDIMENTO SIMPLIFICADO - CONCLUSÃO

* **[Ticket: DSAUGHFATF-26176]** Removida obrigatoriedade nos campos dos dados da autorização no atendimento simplificado

Arquivo: Sau/saude-front

### Rotina: PARECER DE ESPECIALISTA

* **[Ticket: 28143189 / DSAUPEPCONV-23837]** Visualização dos Resultados de Exames e Configuração

Arquivo: RM.Sau.UnidadeDiagnostico.Data.dll

## 12.1.2602.162

### Rotina: AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-26364]** Adicionada a Central de Autorizações como anexo do registro de atendimento

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: 27304067 / DSAUGHFATF-25989]** Data da Guia sem Informações (Central de Autorização)

Arquivos: RM.Sau.GestaoGlosa.Server.dll; RM.Sau.Ans.Sever.dll; RM.Sau.Lib.dll; RM.Sau.Autorizacao.Intf.dll; RM.Sau.Movimento.Service.dll; RM.Sau.Autorizacao.Data.dll; RM.Sau.AuthorizationGuide.Intf.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.AuthorizationGuide.Server.dll

* **[Ticket: DSAUGHFATF-26365]** A partir de agora, o campo de indicação clínica está disponível para preenchimento diretamente na central de autorizações, alinhado ao comportamento já existente no registro de atendimento.

Arquivo: RM.Sau.Autorizacao.Form.dll

### Rotina: DEFINIR PARÂMETROS DO PORTAL DO PACIENTE

* **[Ticket: 27006390 / DSAUGHASSIST-22611]** Ajuste em fluxo interno ,garantindo uma maior consistencia

Arquivos: RM.Sau.Portal.Lib.Application.Api.dll; RM.Sau.Cadastros.Server.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14782]** Ajuste no tipo de movimento “Requisição do Paciente” da tela de Movimentação de Estoque: quando configurado para permitir o processamento de itens sem confirmação, ao adicionar um item na requisição ele será automaticamente salvo como confirmado, eliminando a necessidade de utilizar a função “Confirmar Item".

Arquivo: RM.Sau.Stock.Form.dll

### Rotina: PROCESSOS FARMACÊUTICOS - EDIÇÃO

* **[Ticket: DSAUCLINICA-14739]** Ajuste na tela de devolução dos processos farmacêuticos: ao realizar a leitura do código de barras de um item, ele será automaticamente adicionado à grid de itens devolvidos. Caso a quantidade não seja informada, será atribuída automaticamente a quantidade 1.

Arquivo: RM.Sau.Stock.Form.dll

## 12.1.2602.163

### Rotina: AGENDAMENTO

* **[Ticket: 28264701 / DSAUGHASSIST-22878]** Ajuste realizados na criação do horário especial que não permite salvar horarios duplicados

Arquivos: RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.Utils.Intf.dll; RM.Sau.AgendaAtendimento.Data.dll

* **[Ticket: 28264959 / DSAUGHASSIST-22879]** Ajuste realizado no processo que move o encaixe de um período especial para um período normal

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-26365]** A partir de agora, o campo de indicação clínica está disponível para preenchimento diretamente na central de autorizações, alinhado ao comportamento já existente no registro de atendimento.

Arquivo: RM.Sau.Autorizacao.Form.dll

### Rotina: CONDIÇÕES CONTRATUAIS

* **[Ticket: 28508625 / DSAUGHFATF-26379]** Preenchimento automático do campo “Regime de Atendimento” nas informações ANS TISS, o campo sempre era preenchido como Pronto Socorro.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: CÓPIA DE PRESCRIÇÃO

* **[Ticket: DSAUPEPCONV-23408]** Adicionado o botão Ciente Ressalva também para prescrições vencidas

Arquivo: Sau/pep

### Rotina: REGISTRO E CONTROLE

* **[Ticket: DSAUGHFATF-26393]** Ao remover documento do malote, retornar o status De: A Confirmar para: Em Aberto

Arquivos: RM.Sau.ControleDocumentos.Data.dll; RM.Sau.ControleDocumentos.Form.dll

### Rotina: VISUALIZAR RESULTADOS DE EXAMES

* **[Ticket: 27866473 / DSAUGHASSIST-22687]** Ajuste na geração do Gráficos no Historico de Resultado

Arquivo: Sau/portalpaciente

## 12.1.2602.164

### Rotina: AGENDAMENTO

* **[Ticket: 28301045 / DSAUGHASSIST-22905]** Corrigido o comportamento orren

Arquivo: RM.Sau.AgendaAtendimento.Form.dll

### Rotina: GESTÃO DE LEITOS - OCUPAÇÃO DE LEITOS

* **[Ticket: 27315017 / DSAUGHASSIST-22900]** Ajuste em fluxo interno ,garantindo uma maior consistencia

Arquivos: RM.Sau.Utils.Server.dll; RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.RegistroAtendimento.Data.dll; RM.Sau.Consultas.Intf.dll; RM.Sau.RegistroAtendimento.Server.dll

### Rotina: LIBERAÇÃO

* **[Ticket: DSAUPEPCONV-23832]** Obrigatoriedade de Justificativa para Prescrição de Itens com Ressalva

Arquivos: RM.Sau.Stock.Server.dll; RM.Sau.Stock.Intf.dll

* **[Ticket: DSAUPEPCONV-23832]** Criação do campo justificativa para itens liberados com ressalva

Arquivo: Sau/pep

### Rotina: MEDICAMENTO

* **[Ticket: DSAUPEPCONV-23403]** Parametrização para Obrigatoriedade de Justificativa em Itens com Ressalva

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Form.dll; RM.Sau.Cadastros.Intf.dll

## 12.1.2602.165

### Rotina: AGENDAMENTO

* **[Ticket: 27223738 / DSAUGHASSIST-22991]** Tempo elevado de horários disponiveis reduzido atingindo melhor usabilidade na obteção de horários.

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: ATUALIZAÇÃO BRASÍNDICE

* **[Ticket: 28289407 / DSAUGHFATF-26288]** Problema ao registrar uma tabela de preço quando o campo fonte de preço está vazio.

Arquivo: RM.Sau.Produto.Form.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-26374]** Agora é possível selecionar e autorizar vários itens de uma guia de uma só vez nas autorizações offline, agilizando o processo quando há vários itens a serem tratados.

Arquivos: RM.Sau.Autorizacao.Intf.dll; RM.Sau.Autorizacao.Server.dll; RM.Sau.Autorizacao.Form.dll

### Rotina: ONCOLOGIA - QUIMIOTERAPIA

* **[Ticket: 26512006 / DSAUPEPCONV-23696]** Cálculo corporal refletindo em pacientes de outra unidade

Arquivo: Sau/pep

### Rotina: RECEPÇÃO

* **[Ticket: 28424929 / DSAUGHASSIST-22966]** Foi realizado um ajuste na criação do exame simplificado a partir do atendimento para registrar corretamente o medico solicitante

Arquivo: RM.Sau.UnidadeDiagnostico.Server.dll

## 12.1.2602.166

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUCLINICA-14679]** Ajuste na tela de devolução da Movimentação de Estoque: foi corrigido um problema que ocasionava a exibição de uma mensagem de não tratada ao tentar editar um produto, impedindo sua alteração. Com a correção, o usuário pode editar o produto normalmente.

Arquivo: RM.Sau.Stock.Form.dll

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-23093]** Ajuste para corrigir a pesquisa dos dias com horários normais

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: ATENDIMENTO SIMPLIFICADO - CONCLUSÃO

* **[Ticket: 26498197 / DSAUGHASSIST-21826]** Estrutura que permite ordenar colunas A-Z no atendimento simplificado.

Arquivo: Sau/saude-front

## 12.1.2602.168

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUPEPCONV-23755]** Correção ortográfica na modal

Arquivo: Sau/pep

### Rotina: AGENDAS

* **[Ticket: 28514972 / DSAUGHASSIST-23009]** Ajuste realizado nos métodos que controlam o encaixe para habilitar quando existe periodos de especialidades diferentes no mesmo dia

Arquivos: RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll

### Rotina: ALTA

* **[Ticket: 28799409 / DSAUGHASSIST-23109]** Ajuste para exibição do Número da Declaração de Óbito na grid do registro de atendimentos

Arquivo: RM.Sau.RegistroAtendimento.Data.dll

### Rotina: ATENDIMENTO SIMPLIFICADO - PACIENTE

* **[Ticket: DSAUGHASSIST-23021]** DSAUGHASSIST-23021 Mover agendamento com 1 exame para um agendamento com a duração menor.

Arquivos: RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.AgendaAtendimento.Form.dll; RM.Sau.AgendaAtendimento.Intf.dll

### Rotina: ELABORAÇÃO DE CONTAS

* **[Ticket: 28430058 / DSAUGHFATF-26361]** Ao tentar aplicar Desconto de Cobertura do Convênio, para mais de um procedimento de uma única vez, o sistema está apresentando incosistencia.

Arquivo: RM.Sau.Faturamento.Server.dll

### Rotina: FATURAMENTO PARTICULAR

* **[Ticket: 28781312 / DSAUGHFATF-26465]** Ao encerrar uma elaboração de contas de um paciente particular para geração do pedido de nota fiscal o sistema está listando regras tributárias de outras coligadas..

Arquivo: RM.Sau.Tesouraria.Form.dll

### Rotina: PAINEL DE CHAMADAS

* **[Ticket: DSAUGHASSIST-22929]** Incluir a coluna de unidade na aba setor do totem

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Form.dll

### Rotina: PRESCRIÇÃO MÉDICA - APRAZAMENTO

* **[Ticket: DSAUPEPCONV-23839]** DSAUPEPCONV-23839 Análise PUC aprazamento horário incorreto

Arquivo: Sau/pep

### Rotina: RECEPÇÃO

* **[Ticket: 28807949 / DSAUGHASSIST-23135]** Ajuste realizados nas colunas do grid de exibição dos dados do visitante

Arquivo: RM.Sau.Consultas.Form.dll

## 12.1.2602.169

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUPEPCONV-23755]** DSAUPEPCONV-23755 PEP - Atividade para Teste Sistêmico 2606

Arquivo: Sau/pep

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-23141]** DSAUGHASSIST-23141 Especialidade x Agendamento

Arquivos: RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.AgendaAtendimento.Form.dll

## 12.1.2602.170

### Rotina: AGENDA DE CIRURGIAS - EDIÇÃO

* **[Ticket: DSAUGHASSIST-23103]** [FIX] DSAUGHASSIST-23103 Padronização da tela de Pesquisa de Paciente

Arquivos: RM.Sau.Common.Form.dll; RM.Sau.AgendaAtendimentoCustomizada.Form.dll

### Rotina: AGENDAMENTO

* **[Ticket: 28495193 / DSAUGHASSIST-23144]** Ajuste para inativar uma agenda

Arquivo: RM.Sau.AgendaAtendimento.Data.dll

### Rotina: CADASTRO DE DENTES

* **[Ticket: 27377395 / DSAUGHASSIST-22515]** remover condição de eletivos para minha agenda quando for odontologia

Arquivo: Sau/pep

### Rotina: DEFINIR PARÂMETROS DO PORTAL DO PACIENTE

* **[Ticket: 27417801 / DSAUGHASSIST-22551]** Corrigido a busca de feriados.

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: 28799812 / DSAUGHFATF-26505]** Ajuste na rotina de edição/exclusão de procedimentos da AIH gerados via integração com o estoque para que o sistema deixe de impedir a ação, ficando a critério do usuário decidir se irá prosseguir mediante caixa de diálogo de confirmação.

Arquivos: RM.Sau.Sus.Data.dll; RM.Sau.Sus.Form.dll

### Rotina: MANUTENÇÃO DE TABELA DE PREÇO DE MATERIAIS E MEDICAMENTOS

* **[Ticket: 28279081 / DSAUGHFATF-26284]** Ajuste na tela de manutenção de tabelas de preços para que o componente de histórico não impeça a seleção dos registros.

Arquivos: Sau/saude-front; RM.Sau.TabelaPreco.Intf.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 28807360 / DSAUPEPCONV-23954]** DSAUPEPCONV-23954 VISUALIZAÇÃO DA SOLICITAÇÃO DE MAT/MED

Arquivo: Sau/pep

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14445]** Requisição do paciente. Ajuste na rotina de conversão de unidades de medida durante a criação e processamento de requisições. Para itens que necessitam conversão de unidade, ou seja, quando a unidade de controle é diferente da unidade de faturamento ou quando o item é prescrito em uma unidade distinta, o cálculo passa a considerar o volume de faturamento do produto, em substituição ao fator de conversão anteriormente utilizado. Com essa alteração, situações em que o fator de conversão resulta em dízimas periódicas deixam de gerar divergências, garantindo que os valores cobrados na conta e as quantidades baixadas no estoque permaneçam consistentes.

Arquivos: RM.Sau.Stock.Intf.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Produto.Server.dll; RM.Sau.Lib.dll; RM.Sau.Produto.Intf.dll; RM.Sau.Extensions.dll; RM.Sau.Stock.Form.dll; RM.Sau.Stock.Data.dll; RM.Sau.Utils.Intf.dll

* **[Ticket: DSAUCLINICA-14445]** Prescrição Médica, Painel de dispensação e Solicitação de Mat/Med. Ajuste na rotina de conversão de unidades de medida durante a criação e processamento de requisições. Para itens que necessitam conversão de unidade, ou seja, quando a unidade de controle é diferente da unidade de faturamento ou quando o item é prescrito em uma unidade distinta, o cálculo passa a considerar o volume de faturamento do produto, em substituição ao fator de conversão anteriormente utilizado. Com essa alteração, situações em que o fator de conversão resulta em dízimas periódicas deixam de gerar divergências, garantindo que os valores cobrados na conta e as quantidades baixadas no estoque permaneçam consistentes.

Arquivos: RM.Sau.Stock.Intf.dll; RM.Sau.Stock.Server.dll; RM.Sau.Stock.Form.dll

* **[Ticket: DSAUCLINICA-14445]** Ajuste na requisição de paciente da movimentação de estoque. Ao selecionar um kit, a quantidade informada passa a ser exibida corretamente na unidade de controle no momento da inclusão na requisição, realizando também a conversão adequada para a unidade de faturamento.

Arquivo: RM.Sau.Stock.Form.dll

### Rotina: ORÇAMENTO

* **[Ticket: 27326605 / DSAUGHASSIST-22512]** Ajuste no campo procedimento

Arquivo: Sau/pep

### Rotina: RESULTADOS DE EXAMES

* **[Ticket: 28491678 / DSAUGHASSIST-23063]** Ajuste realizado para que ao pressionar a tecla TAB realize a validação do método

Arquivo: RM.Sau.UnidadeDiagnostico.Form.dll

## 12.1.2602.171

### Rotina: Sem Rotina Específica

* **[Ticket: 28829780 / DSAUGHFATF-26503]** Grupo de prestadores com limite de descrição no prestador principal

Arquivos: RM.Sau.Cadastros.Data.dll; RM.Sau.Cadastros.Intf.dll

* **[Ticket: DSAUPEPCONV-23755]** Descrição de prescrição médica é replicada em oncologia

Arquivo: Sau/pep

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: 28833368 / DSAUGHFATF-26511]** Agora a validação de AIH esta sincronizado com as regras de lançamento de diárias corretamente.

Arquivo: RM.Sau.Sus.Server.dll

* **[Ticket: DSAUGHFATF-26518]** Ao tentar aplicar Desconto de Cobertura do Convênio, para mais de um procedimento de uma única vez, o sistema está apresentando incosistencia.

Arquivo: RM.Sau.Sus.Intf.dll

* **[Ticket: DSAUGHFATF-26518]** Informar a data de lançamento e data de competência para procedimentos AIH

Arquivo: RM.Sau.Sus.Intf.dll

### Rotina: FATURAMENTO PARTICULAR

* **[Ticket: 28781309 / DSAUGHASSIST-23195]** Ajuste no responsável financeiro

Arquivo: RM.Sau.RegistroAtendimento.Form.dll

### Rotina: INTERNAÇÃO

* **[Ticket: DSAUGHASSIST-21596]** Inclusão da possibilidade de transferir o paciente para a unidade do leito

Arquivos: RM.Sau.Parametrizador.Form.dll; RM.Sau.Bed.Form.dll; RM.Sau.Bed.Server.dll; RM.Sau.Bed.Intf.dll; RM.Sau.Parametrizador.Data.dll; RM.Sau.Parametros.Intf.dll; RM.Sau.Parametrizador.Intf.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 28807642 / DSAUPEPCONV-23972]** DSAUPEPCONV-23972 NÚMERO DA REQUISIÇÃO DA SOLICITAÇÃO

Arquivo: Sau/pep

### Rotina: MOVIMENTAÇÃO DE ESTOQUE

* **[Ticket: 28903219 / DSAUCLINICA-14833]** Ajuste na rotina de suspensão da requisição do paciente na movimentação de estoque. Após a conclusão da suspensão, será exibida apenas uma única mensagem de sucesso, independentemente da quantidade de itens suspensos, informando que a operação foi realizada com sucesso.

Arquivo: RM.Sau.Stock.Form.dll

### Rotina: MOVIMENTAÇÃO DE ESTOQUE - EDIÇÃO

* **[Ticket: DSAUCLINICA-14445]** Ajuste na rotina de conversão de unidades de medida durante a criação e processamento de requisições. Para itens que necessitam conversão de unidade, ou seja, quando a unidade de controle é diferente da unidade de faturamento ou quando o item é prescrito em uma unidade distinta, o cálculo passa a considerar o volume de faturamento do produto, em substituição ao fator de conversão anteriormente utilizado. Com essa alteração, situações em que o fator de conversão resulta em dízimas periódicas deixam de gerar divergências, garantindo que os valores cobrados na conta e as quantidades baixadas no estoque permaneçam consistentes.

Arquivos: RM.Sau.Stock.Server.dll; RM.Sau.Produto.Intf.dll; RM.Sau.UnidadeDiagnostico.Server.dll; RM.Sau.Stock.Data.dll; RM.Sau.Lib.dll; RM.Sau.Stock.Intf.dll; RM.Sau.Manipulacao.Server.dll; RM.Sau.Manipulacao.Intf.dll; RM.Sau.Produto.Server.dll; RM.Sau.Pep.Server.dll; RM.Sau.Stock.Form.dll

* **[Ticket: DSAUCLINICA-14445]** Ajuste na rotina de conversão de unidades de medida. Para itens que necessitam conversão de unidade, ou seja, quando a unidade de controle é diferente da unidade de faturamento ou quando o item é prescrito em uma unidade distinta, o cálculo passa a considerar o volume de faturamento.

Arquivos: Sau/portal-farmacia; Sau/Sau-PortalFarmacia

### Rotina: OUTROS CADASTROS

* **[Ticket: 28644877 / DSAUGHFATF-26421]** Ajuste nos parâmetros gerais de faturamento.

Arquivo: RM.Sau.Parametrizador.Intf.dll

### Rotina: RECEPÇÃO

* **[Ticket: 28800071 / DSAUGHASSIST-23120]** DSAUGHASSIST-23120 #HCSS - Filtro utilizando o Campo Status Conta

Arquivo: RM.Sau.RegistroAtendimento.Data.dll

## 12.1.2602.172

### Rotina: AGENDAMENTO

* **[Ticket: 28899486 / DSAUGHASSIST-23239]** Inconsistência entre as APIs appointments e appointmentavailables

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

### Rotina: CENTRAL DE AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-26467]** Ajuste no agendamento de múltiplos exames com restrição contratual que exigem liberação pelo convênio.

Arquivo: RM.Sau.AgendaAtendimento.Server.dll

## 12.1.2602.173

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUCLINICA-14679]** Ajuste na devolução da tela de Movimentação de Estoque: foi corrigido um problema que ocorria ao realizar devoluções utilizando a unidade de faturamento. No momento da gravação, o fator de conversão estava sendo salvo incorretamente com o valor 1. Como consequência, durante o processamento da devolução, a conversão da unidade de faturamento para a unidade de controle era realizada de forma incorreta, resultando na mesma quantidade para ambas as unidades. Essa situação gerava divergências no saldo de estoque. Com a correção, o fator de conversão passa a ser gravado corretamente, garantindo a conversão adequada das quantidades.

Arquivo: RM.Sau.Stock.Form.dll

* **[Ticket: DSAUPEPCONV-23755]** Descrição de prescrição médica campo complementar

Arquivo: Sau/pep

### Rotina: AGENDAMENTO

* **[Ticket: DSAUGHASSIST-23162]** DSAUGHASSIST-23162 agendamento de exames remover status pre-agendado

Arquivo: Sau/saude-front

### Rotina: ANÁLISE DE PRESCRIÇÕES - VISÃO

* **[Ticket: 26868566 / DSAUPEPCONV-23352]** DSAUPEPCONV-23352 Abertura da tela de Análise Farmacêutica

Arquivo: Sau/pep

### Rotina: AUTORIZAÇÕES

* **[Ticket: DSAUGHFATF-26478]** Ajuste na rotina de impressão em lote para reutilizar valores em comum de consultas anteriores (cache) e realizar impressão simultânea de mais de um report em grupos de até 5 por vez.

Arquivos: RM.Sau.AuthorizationGuide.Server.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Extensions.dll; RM.Sau.Utils.Intf.dll; RM.Sau.Utils.Server.dll; RM.Sau.Autorizacao.Server.dll; RM.Sau.Faturamento.Intf.dll

### Rotina: LIBERAÇÃO

* **[Ticket: 28873371 / DSAUCLINICA-14849]** Ajuste na validação de saldo para integrações com o EMS via iPaaS. Foi adicionada a validação do preenchimento do lote e realizado o ajuste no processamento do objeto de retorno do JSON, garantindo a recuperação correta do saldo do produto.

Arquivos: RM.Sau.Produto.Server.dll; RM.Sau.Produto.Intf.dll

### Rotina: PEDIDO DE EXAMES

* **[Ticket: DSAUGHASSIST-22632]** Alterado parametro Utiliza Status Liberação na Recepção da unidade diagnóstico para não permitir digitação do campo

Arquivo: RM.Sau.Parametrizador.Form.dll

## 12.1.2602.174

### Rotina: AGENDAMENTO

* **[Ticket: 28495193 / DSAUGHASSIST-23322]** Ajuste ao salvar uma nova agenda em base Oracle

Arquivos: RM.Sau.Sus.Server.dll; RM.Sau.Cadastros.Data.dll; RM.Sau.Repasse.Server.dll; RM.Sau.AgendaAtendimento.Data.dll; RM.Sau.Integracoes.Server.dll; RM.Sau.Cadastros.Server.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.UnidadeDiagnostico.Data.dll

### Rotina: FATURAMENTO TISS

* **[Ticket: DSAUCLINICA-14791]** Alterações necessárias para utilização de Faturamento de Convênio padrão TISS versão 4.03.00, conforme documentação no TDN https://tdn.totvs.com/x/f49\_Pg e documentação TISS site https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/padrao-tiss-janeiro-2026

Arquivos: RM.Sau.AuthorizationGuide.Form.dll; RM.Sau.Tiss.Infraestrutura.Server.dll; RM.Sau.Lib.dll; RM.Sau.AuthorizationGuide.Intf.dll; RM.Sau.Tiss.Application.Server.dll; RM.Sau.RegistroAtendimento.Server.dll; RM.Sau.SmartX.Cadastros.Service.dll; RM.Sau.AgendaAtendimento.Server.dll; RM.Sau.Utils.Intf.dll; RM.Sau.FaturamentoConvenio.Intf.dll; RM.Sau.CadastrosFat.Form.dll; RM.Sau.Ans.Sever.dll; RM.Sau.SmartX.CadastrosAns.Service.dll; RM.Sau.ActionsHub.Shared.dll; RM.Sau.GestaoGlosa.Form.dll; RM.Sau.CadastrosFat.Data.dll; RM.Sau.GestaoGlosa.Server.dll; RM.Sau.CadastrosFat.Intf.dll; RM.Sau.AgendaAtendimento.Intf.dll; RM.Sau.Autorizacao.Form.dll; RM.Sau.Tiss.Infraestrutura.Intf.dll; RM.Sau.SmartX.Cadastros.Objetos.Service.dll; RM.Sau.AuthorizationGuide.Server.dll; RM.Sau.GestaoGlosa.Intf.dll; RM.Sau.Faturamento.Intf.dll; RM.Sau.Ans.Data.dll; RM.Sau.Faturamento.Form.dll; RM.Sau.SmartX.CadastrosAns.Objetos.Service.dll; RM.Sau.Faturamento.Server.dll; RM.Sau.Ans.Form.dll; RM.Sau.RegistroAtendimento.Intf.dll; RM.Sau.Parametros.Intf.dll; RM.Sau.Ans.Intf.dll; RM.Sau.RegistroAtendimento.Form.dll; RM.Sau.Server.dll; RM.Sau.AuthorizationGuide.Data.dll; RM.Sau.FaturamentoConvenio.Server.dll

* **[Ticket: DSAUGHFATF-26630]** Ajuste para atender requisitos de qualidade da aplicação.

Arquivos: RM.Sau.Tesouraria.Server.dll; RM.Sau.Movimento.Server.dll

### Rotina: REPASSES

* **[Ticket: 28108609 / DSAUGHFATF-26294]** Ajuste na rotina de cancelamento da folha de pagamento para retornar o controle do repasse para o status de Liberado, possibilitando a atualização de valores em caso de reprocessamento dos critérios aplicados.

Arquivo: RM.Sau.Movimento.Service.dll

# TOTVS Gestão Hospitalar Prontuário Eletrônico

## 12.1.2602.100

### Rotina: FORMULÁRIO DINÂMICO

* **[Ticket: DSAUPEPCONV-22917]** Ajuste na suspensão de formulários dinâmicos

Arquivos: RM.Pep.SmartX.Prescricao.Objects.dll; RM.Pep.SmartX.dll; RM.Pep.SmartX.Prescricao.Service.dll; RM.Pep.SmartX.Extensions.dll; RM.Pep.FormularioDinamico.Api.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-22896]** [FIX] DSAUPEPCONV-22896 Checagem / Aprazamento. Horários

Arquivos: RM.Pep.PrescricaoEnfermagem.Server.Negocio.dll; RM.Pep.PlanejamentoTerapeutico.IService.dll; RM.Pep.PlanejamentoTerapeutico.Server.dll; RM.Pep.PrescricaoEnfermagem.Facade.dll; RM.Pep.PlanejamentoTerapeutico.Server.Negocio.dll

## 12.1.2602.101

### Rotina: Sem Rotina Específica

* **[Ticket: 26168331 / DSAUGHUD-5010]** Na central de laudos em prontuário eletrônico ao Liberar um laudo com assinatura digital EvalTec foi incluido no rodape do laudo os dados da pessoa que assinou o laudo;

Arquivo: RM.Pep.CentralLaudo.Server.dll

### Rotina: CADASTRO DE DENTES

* **[Ticket: DSAUGHPACDIG-1337]** adicionado no mapa facial dentro do prontuario eletronico

Arquivos: RM.Pep.Odontologia.Service.dll; RM.Pep.Odontologia.IService.dll

### Rotina: ONCOLOGIA - TRATAMENTOS

* **[Ticket: DSAUGHNEXUS-656]** Suspensão de Materiais e Diluentes não estava sendo enviada para estoque

Arquivo: RM.Pep.ItemQuimio.Server.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-22831]** DSAUPEPCONV-22831 RÉPLICA para 12.1.2602 - [Mauá] - Parametrização - Aletas da prescrição médica

Arquivos: RM.Pep.Prescricao.Shared.dll; RM.Pep.Settings.Server.dll; RM.Pep.Prescricao.Server.dll; RM.Pep.Prescricao.Server.Negocio.dll; RM.Pep.Settings.IService.dll; RM.Pep.Prescricao.Api.dll; RM.Pep.Prescricao.IService.dll; RM.Pep.Prescricao.Shared.Facade.dll

## 12.1.2602.107

### Rotina: Sem Rotina Específica

* **[Ticket: DSAUPEPCONV-22865]** Informativo na solicitação

Arquivos: RM.Pep.SolicitacaoMaterialMedicamento.Server.dll; RM.Pep.Produto.Server.dll; RM.Pep.SolicitacaoMaterialMedicamento.IService.dll; RM.Pep.Produto.IService.dll; RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll; RM.Pep.Produto.Server.Negocio.dll; RM.Pep.SolicitacaoMaterialMedicamento.Facade.dll

### Rotina: LIBERAÇÃO

* **[Ticket: DSAUPEPCONV-22741]** Obrigatoriedade de retorno Item Liberado com Ressalva

Arquivos: RM.Pep.Prescricao.Server.dll; RM.Pep.Settings.Server.dll; RM.Pep.Prescricao.Shared.Facade.dll; RM.Pep.Prescricao.Shared.dll; RM.Pep.Settings.IService.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-23005]** Unidade de Dosagem de material

Arquivos: RM.Pep.SolicitacaoMaterialMedicamento.Server.dll; RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll; RM.Pep.SolicitacaoMaterialMedicamento.Facade.dll

### Rotina: RESULTADOS DE EXAMES

* **[Ticket: DSAUGHUD-4945]** Adiciona data da coleta na tela de resultados PEP

Arquivo: RM.Pep.CentralLaudo.Server.dll

## 12.1.2602.110

### Rotina: URGÊNCIA E EMERGÊNCIA

* **[Ticket: 26503442 / DSAUPEPCONV-22909]** Ajustado a reabertura do atendimento médico no painel de urgência

Arquivo: RM.Pep.Atendimento.Server.Negocio.dll

## 12.1.2602.111

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-22817]** Painel de Dispensação quando solicitados pela enfermagem

Arquivo: RM.Pep.Prescricao.Server.dll

## 12.1.2602.112

### Rotina: PROTOCOLO TEV

* **[Ticket: 26028078 / DSAUGHNEXUS-572]** Cálculo do Score SAPS III

Arquivos: RM.Pep.ScorePaciente.Server.dll; RM.Sau.Server.dll; RM.Pep.ScorePaciente.IService.dll; RM.Pep.Shared.dll; RM.Pep.ScorePaciente.Server.Negocio.dll; RM.Pep.ScorePaciente.Api.dll

## 12.1.2602.115

### Rotina: RESULTADOS DE EXAMES

* **[Ticket: DSAUPEPCONV-23126]** Adiciona data de coleta na tela de resultado do pep

Arquivos: RM.Pep.ResultadoExame.Server.dll; RM.Pep.SolicitacaoExame.Server.dll; RM.Pep.SolicitacaoExame.IService.dll; RM.Pep.SolicitacaoExame.Server.Negocio.dll; RM.Pep.ResultadoExame.Facade.dll; RM.Pep.ResultadoExame.IService.dll

## 12.1.2602.116

### Rotina: MEDICAMENTO

* **[Ticket: 26705779 / DSAUPEPCONV-23097]** Ajustado para que obter a condição contratual do convênio da parcial

Arquivos: RM.Pep.AlertaMedicamento.Server.dll; RM.Pep.AlertaMedicamento.Server.Negocio.dll; RM.Pep.Prescricao.Shared.Facade.dll; RM.Pep.Faturamento.Facade.dll

## 12.1.2602.117

### Rotina: HISTÓRICO DE ATENDIMENTO

* **[Ticket: DSAUPEPCONV-22129]** Ajustado para aplicar o filtro do usuário criador do registro somente atravez da api de resumo.

Arquivo: RM.Pep.HistoricoClinico.Server.dll

* **[Ticket: 26727806 / DSAUPEPCONV-23117]** DSAUPEPCONV-23117 Ajuste de horário no histórico de Atendimento

Arquivo: RM.Pep.HistoricoClinico.Server.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-22766]** Parametrização da obrigatoriedade do campo de fluxo na PM

Arquivos: RM.Pep.Prescricao.Shared.Facade.dll; RM.Pep.Prescricao.Shared.dll; RM.Pep.Settings.IService.dll; RM.Pep.Settings.Server.dll; RM.Pep.Prescricao.Server.Negocio.dll

## 12.1.2602.124

### Rotina: FORMULÁRIO DINÂMICO

* **[Ticket: 25521671 / DSAUPEPCONV-22087]** Ajuste para gerar assinatura digital em caso de formulários dinâmicos sem rascunho prévio salvo.

Arquivo: RM.Pep.FormularioDinamico.Api.dll

## 12.1.2602.125

### Rotina: ANAMNESE

* **[Ticket: DSAUPEPCONV-22801]** DSAUPEPCONV-22801 [ Mauá ] - Validação de Anamnese por Tipo de Ação

Arquivos: RM.Pep.ObrigatoriedadeClinica.IService.dll; RM.Pep.Atendimento.IService.dll; RM.Pep.Shared.dll; RM.Pep.Prescricao.Shared.Facade.dll; RM.Pep.Anamnesis.Intf.dll; RM.Pep.ObrigatoriedadeClinica.Api.dll; RM.Pep.ObrigatoriedadeClinica.Server.dll; RM.Pep.Anamnesis.Server.dll; RM.Pep.CrossCutting.Contracts.dll

## 12.1.2602.126

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-23423]** Visualização das prescrições médicas no histórico de atendimento

Arquivo: RM.Pep.HistoricoClinico.Server.dll

## 12.1.2602.127

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23270]** Configurado por parâmetro, permite a impressão automatica de exames ao LIBERAR a prescrição e ao imprimir uma LIBERAÇÃO de prescrição, se as mesmas tiverem solicitações de exames.

Arquivos: RM.Pep.Prescricao.Server.Negocio.dll; RM.Pep.Settings.IService.dll; RM.Pep.Prescricao.IService.dll; RM.Pep.Prescricao.Server.dll; RM.Pep.Prescricao.Shared.Facade.dll; RM.Pep.Prescricao.Shared.dll; RM.Pep.Settings.Server.dll

## 12.1.2602.132

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-23423]** Prescrição Médica não exibida no Resumo de Atendimento

Arquivo: RM.Pep.HistoricoClinico.Server.dll

## 12.1.2602.133

### Rotina: EXAMES - SOLICITAÇÃO DE EXAMES

* **[Ticket: DSAUPEPCONV-23119]** FEAT DSAUPEPCONV-23367 Criação do campo de observação na solicitação de exames.

Arquivos: RM.Pep.Prescricao.Server.dll; RM.Pep.PlanejamentoTerapeutico.Server.Negocio.dll; RM.Pep.Prescricao.Facade.dll; RM.Pep.Prescricao.IService.dll; RM.Pep.SolicitacaoExame.Server.Negocio.dll; RM.Pep.Prescricao.Server.Negocio.dll; RM.Pep.PlanejamentoTerapeutico.Facade.dll

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-23423]** Ajuste na visualização das prescrições médicas no histórico de atendimento

Arquivo: RM.Pep.HistoricoClinico.Server.dll

### Rotina: SCORES - OUTROS

* **[Ticket: DSAUPEPCONV-23307]** Scores: habilitar múltiplas seleções

Arquivos: RM.Pep.ScorePaciente.Server.dll; RM.Pep.ScoreEscala.IService.dll; RM.Pep.ScorePaciente.Server.Negocio.dll; RM.Pep.ScoreEscala.Server.Negocio.dll; RM.Pep.CrossCutting.Dto.dll; RM.Pep.CrossCutting.Contracts.dll; RM.Pep.ScorePaciente.IService.dll; RM.Pep.ScoreEscala.Server.dll

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23118]** Integração da Observação da Solicitação de Exame do PEP para a Unidade Diagnóstica (RM)

Arquivos: RM.Pep.Prescricao.Server.Negocio.dll; RM.Pep.SolicitacaoExame.Facade.dll

## 12.1.2602.134

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23548]** Tratativa de bloqueio de botão quando item de mat/med tem origem em prescrição medica

Arquivo: RM.Pep.AlertaMedicamento.Server.Negocio.dll

## 12.1.2602.135

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23548]** Tratativa de bloqueio de botão quando item de mat/med tem origem em prescrição medica

Arquivos: RM.Pep.SolicitacaoMaterialMedicamento.Server.dll; RM.Pep.Prescricao.Server.Negocio.dll; RM.Pep.SolicitacaoMaterialMedicamento.IService.dll; RM.Pep.Prescricao.IService.dll; RM.Pep.Prescricao.Server.dll; RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll; RM.Pep.Prescricao.Shared.dll; RM.Pep.SolicitacaoMaterialMedicamento.Facade.dll

## 12.1.2602.137

### Rotina: HISTÓRICO DE ATENDIMENTO

* **[Ticket: 26557396 / DSAUPEPCONV-23026]** Ajuste na visualização de arquivos de forms no histórico de atendimento no expandir da timeline.

Arquivo: RM.Pep.FormularioDinamico.Server.dll

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23550]** Quantidade prescrita é alterada após finalizar solicitação

Arquivo: RM.Pep.SolicitacaoMaterialMedicamento.Server.dll

## 12.1.2602.140

### Rotina: FORMULÁRIO DINÂMICO

* **[Ticket: 25651645 / DSAUPEPCONV-22324]** DSAUPEPCONV-22324 Exibição de anexos do prontuário do paciente

Arquivo: RM.Pep.Documents.Infra.dll

### Rotina: INTERCONSULTA AMBULATORIAL

* **[Ticket: 26614492 / DSAUPEPCONV-23075]** DSAUPEPCONV-23075 PEP RM - Exames Pendentes para o Status 'O'

Arquivo: RM.Pep.SolicitacaoExame.Server.dll

## 12.1.2602.142

### Rotina: Sem Rotina Específica

* **[Ticket: 26512254 / DSAUPEPCONV-22993]** tempo de esperar no Prontuario Eletronico

Arquivo: RM.Pep.Schedule.Server.Negocio.dll

### Rotina: HISTÓRICO DE ATENDIMENTO

* **[Ticket: DSAUPEPCONV-23448]** FEAT DSAUPEPCONV-23448 Criação da coluna de grupo profissional no histórico

Arquivos: RM.Pep.HistoricoClinico.Server.Negocio.dll; RM.Pep.HistoricoClinico.IService.dll; RM.Pep.Shared.dll; RM.Pep.FormularioDinamico.Server.dll; RM.Pep.HistoricoClinico.Server.dll

## 12.1.2602.143

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23318]** [ Mauá ] Parametrização de Prioridade Default para Exames - Solicitação de Exames

Arquivos: RM.Pep.Settings.Server.dll; RM.Pep.Settings.IService.dll

## 12.1.2602.144

### Rotina: ELABORAÇÃO DE AIH

* **[Ticket: DSAUGHFATF-26026]** Inclusão automática de itens da Equipe Multiprofissional na conta AIH via Evolução.

Arquivos: RM.Pep.ClinicalEvolution.Infra.dll; RM.Pep.ClinicalEvolution.Application.dll; RM.Pep.Shared.dll; RM.Pep.ClinicalEvolution.Server.dll; RM.Pep.ClinicalEvolution.Domain.dll

### Rotina: INTERCONSULTA AMBULATORIAL

* **[Ticket: 27685250 / DSAUPEPCONV-23693]** FEAT DSAUPEPCONV-23693 Correção no email enviado de recuperação de login

Arquivo: RM.Pep.Prestador.Server.Negocio.dll

### Rotina: MOTIVO DE RESERVA DE LEITO - CADASTRO

* **[Ticket: DSAUGHFATF-25854]** Remover Procedimento SUS quando suspender, ou cancelar uma evolucao

Arquivos: RM.Pep.Shared.dll; RM.Pep.ClinicalEvolution.Application.dll; RM.Pep.ClinicalEvolution.Server.dll

## 12.1.2602.145

### Rotina: HISTÓRICO DE ATENDIMENTO

* **[Ticket: 26734038 / DSAUPEPCONV-23349]** Ajuste na visualização da triagem no histórico clínico

Arquivos: RM.Pep.CrossCutting.Dto.dll; RM.Pep.ClassificacaoRisco.Server.dll; RM.Pep.ClassificacaoRisco.Server.Negocio.dll; RM.Pep.ScorePaciente.Server.dll; RM.Pep.CrossCutting.Contracts.dll; RM.Pep.ClassificacaoRisco.IService.dll

## 12.1.2602.149

### Rotina: SOLICITAÇÕES DE EXAMES

* **[Ticket: DSAUPEPCONV-23305]** Parametrização de Prioridade Default para Exames - Prescrição

Arquivos: RM.Pep.Settings.IService.dll; RM.Pep.Settings.Server.dll

## 12.1.2602.150

### Rotina: PRESCRIÇÃO MÉDICA

* **[Ticket: DSAUPEPCONV-23756]** Avaliação de desempenho do 9 de Julho

Arquivos: RM.Pep.Prescricao.Server.Negocio.dll; RM.Pep.UnidadeMedida.Server.Negocio.dll; RM.Pep.Prescricao.Server.dll; RM.Pep.Produto.Server.dll; RM.Pep.Produto.IService.dll; RM.Pep.UnidadeMedida.Server.dll; RM.Pep.Produto.Server.Negocio.dll

## 12.1.2602.152

### Rotina: PRESCRIÇÃO MÉDICA - APRAZAMENTO

* **[Ticket: 27362083 / DSAUPEPCONV-23636]** Avaliação de desempenho do 9 de Julho - COPIA

Arquivo: RM.Pep.Prescricao.Server.Negocio.dll

## 12.1.2602.153

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 28076017 / DSAUPEPCONV-23775]** Ajuste na multiplicação dos diluentes na solicitação MAT/MED

Arquivos: RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll; RM.Pep.Produto.IService.dll; RM.Pep.Produto.Server.Negocio.dll; RM.Pep.Produto.Server.dll

## 12.1.2602.154

### Rotina: RECEITA

* **[Ticket: 28136848 / DSAUPEPCONV-23841]** Ajuste para abrir receitas memed

Arquivo: RM.Pep.Integrations.dll

## 12.1.2602.157

### Rotina: ONCOLOGIA - QUIMIOTERAPIA

* **[Ticket: 26512006 / DSAUPEPCONV-23696]** Parâmetro de Cálculo de Superfície Corporal

Arquivos: RM.Pep.Settings.Server.dll; RM.Pep.Settings.IService.dll

## 12.1.2602.162

### Rotina: CÓPIA DE PRESCRIÇÃO

* **[Ticket: DSAUPEPCONV-23408]** Padronização do Fluxo de Aceite de Ressalva Farmacêutica

Arquivo: RM.Pep.Prescricao.Server.dll

## 12.1.2602.164

### Rotina: LIBERAÇÃO

* **[Ticket: DSAUPEPCONV-23832]** Obrigatoriedade de Justificativa para Prescrição de Itens com Ressalva

Arquivos: RM.Pep.Prescricao.IService.dll; RM.Pep.Estoque.Facade.dll; RM.Pep.Prescricao.Server.dll; RM.Pep.ControleEnfermagem.IService.dll; RM.Pep.Prescricao.Api.dll; RM.Pep.AnaliseFarmaceuticaPrescricao.IService.dll; RM.Pep.AnaliseFarmaceuticaPrescricao.Server.Negocio.dll; RM.Pep.AnaliseFarmaceuticaPrescricao.Server.dll; RM.Pep.Prescricao.Server.Negocio.dll

### Rotina: MEDICAMENTO

* **[Ticket: DSAUPEPCONV-23403]** Parametrização para Obrigatoriedade de Justificativa em Itens com Ressalva

Arquivos: RM.Pep.Settings.IService.dll; RM.Pep.Prescricao.Shared.Facade.dll; RM.Pep.Settings.Server.dll; RM.Pep.Prescricao.Shared.dll

## 12.1.2602.168

### Rotina: PRESCRIÇÃO MÉDICA - CHECAGEM

* **[Ticket: 28614949 / DSAUPEPCONV-23952]** Ajuste na exibição dos anexos

Arquivo: RM.Pep.Documents.Infra.dll

## 12.1.2602.169

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 28548732 / DSAUPEPCONV-23921]** DSAUPEPCONV-23921 RELATÓRIO DA SOLICITAÇÃO DE MAT/MED

Arquivos: RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll; RM.Pep.SolicitacaoMaterialMedicamento.IService.dll; RM.Sau.Stock.Server.dll; RM.Pep.SolicitacaoMaterialMedicamento.Server.dll; RM.Sau.Pep.Intf.dll; RM.Sau.Stock.Intf.dll

## 12.1.2602.170

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: 28548732 / DSAUPEPCONV-23921]** DSAUPEPCONV-23921 RELATÓRIO DA SOLICITAÇÃO DE MAT/MED

Arquivos: RM.Pep.SolicitacaoMaterialMedicamento.Server.dll; RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll

* **[Ticket: 28807360 / DSAUPEPCONV-23954]** DSAUPEPCONV-23954 VISUALIZAÇÃO DA SOLICITAÇÃO DE MAT/MED

Arquivos: RM.Pep.SolicitacaoMaterialMedicamento.Server.dll; RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll

## 12.1.2602.173

### Rotina: PORTAL DO PACIENTE

* **[Ticket: 27685115 / DSAUPEPCONV-23678]** Ajuste no botão chamar próximo no PEP

Arquivo: RM.Pep.Documents.Server.dll

## 12.1.2602.174

### Rotina: MATERIAIS E MEDICAMENTOS

* **[Ticket: DSAUPEPCONV-23898]** DSAUPEPCONV-23898 SIST-V2606 - MAT/MED: Lista de itens do produto composto não é exibida

Arquivo: RM.Pep.SolicitacaoMaterialMedicamento.Server.Negocio.dll

# TOTVS Incorporação

## 12.1.2602.100

### Rotina: ADMINISTRAÇÃO - ADITIVO ALTERAÇÃO DE LOCADOR

* **[Ticket: 25713787 / TINREV001-25537]** Melhoria no aditivo de troca de locatário

Arquivo: RM.Imb.Aluguel.ContratoLoc.Form.dll

### Rotina: ALUGUEL COMPLEMENTAR

* **[Ticket: TINREV001-25702]** Adição do campo Data de Medição no processo de consolidação diária

Arquivos: RM.Imb.Aluguel.ContratoLoc.Intf.dll; RM.Imb.Aluguel.ContratoLoc.Data.dll; RM.Imb.Aluguel.ContratoLoc.Form.dll

### Rotina: CONTRATO DE LOCAÇÃO

* **[Ticket: TINREV001-25263]** Desabilitado a abertura automática do anexo de imóveis no contrato de locação, passando a exigir ação manual do usuário.

Arquivos: RM.Imb.Venda.Facade.dll; RM.Imb.Aluguel.ContratoLoc.Form.dll

* **[Ticket: 17792650 / TINREV001-19938]** Adicionado coluna CPF/CNPJ do locatário na visão de contrato de locação

Arquivos: RM.Imb.Recursos.dll; RM.Imb.Aluguel.ContratoLoc.Data.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21420]** melhoria no reajuste para calcular cpara calcular a fómrula GETVALORCMACUMULADAPARAM

Arquivos: RM.Imb.Venda.Calc.Formula.dll; RM.Imb.Venda.Calc.CalculosBase.dll

### Rotina: DESPESA DE ALUGUEL

* **[Ticket: 26253702 / TINREV001-25773]** Melhoria no processo de Gerar Pagamento de Despesas para considerar o Centro de Custo do imóvel como prioridade. Caso não esteja informado, o sistema utiliza o Centro de Custo definido nos Parâmetros Financeiros, conforme hierarquia estabelecida.

Arquivos: RM.Imb.ControleDespesa.Service.dll; RM.Imb.Venda.Facade.dll; RM.Imb.ControleDespesa.Data.dll

### Rotina: EMPREENDIMENTO

* **[Ticket: 26440099 / DTCGI\_INTSYNC-2587]** Ajuste ao salvar alterações realizadas no empreendimento.

Arquivo: Imb/pvi

### Rotina: PROPOSTA

* **[Ticket: 25919410 / DTCGI\_INTSYNC-2590]** Ajuste na edição da proposta para data ter fuso horário correto

Arquivo: Imb/portalgestaoimoveis

### Rotina: ROLETA DE VENDAS

* **[Ticket: DTCGI\_INTSYNC-2549]** Refatoração envio de e-mails após giro da roleta

Arquivo: RM.Imb.RoletaVendas.Service.dll

### Rotina: VENDA - ADITIVO DE ALTERAÇÃO DE VALOR DA PARCELA

* **[Ticket: 26242232 / TINPAD001-21629]** LOG para verificação dos bloqueios das parcelas

Arquivos: RM.Imb.Venda.Aditivo.Data.dll; RM.Imb.Venda.Facade.dll

## 12.1.2602.101

### Rotina: CONTRATO DE VENDA

* **[Ticket: 24710040 / TINPAD001-21670]** Melhoria nas regras de seguraça do campo de alteração global de vendas.

Arquivo: RM.Imb.Venda.Contrato.Data.dll

### Rotina: GERAIS

* **[Ticket: TINPAD001-21776]** Novo banner OQDigital

Arquivos: RM.Imb.Venda.Lib.WinForms.dll; RM.Imb.dll

### Rotina: IMÓVEL

* **[Ticket: TINREV001-25921]** Redirecionamento para documentação sobre a reforma tributária no banner exibido na abertura do contrato de locação.

Arquivos: RM.Imb.Aluguel.Imovel.Form.dll; RM.Imb.Aluguel.ContratoLoc.Form.dll; RM.Imb.dll; RM.Imb.Venda.Lib.WinForms.dll

### Rotina: VENDA - DIMOB

* **[Ticket: 26410568 / TINPAD001-21730]** Venda sendo considerada na Dimob com a data da venda

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.CalculosBase.dll

## 12.1.2602.102

### Rotina: VENDA - CALCULO

* **[Ticket: 26464087 / TINPAD001-21786]** Ajuste para exibir o banner apenas quando a chamada não for originada de teste automatizado

Arquivos: RM.Imb.Venda.Empreendimento.Form.dll; RM.Imb.Venda.Contrato.Form.dll

## 12.1.2602.103

### Rotina: FECHAMENTO DO CONDOMÍNIO

* **[Ticket: 26296488 / TINREV001-25766]** Cadastro de Despesa Financeira (anexo do condomínio individual) ajustado para permitir a definição do tipo de valor do lançamento: Valor Original ou Valor Líquido.

Arquivos: RM.Imb.Cond.Resources.dll; RM.Imb.Cond.Fechamento.Intf.dll; RM.Imb.Cond.Consts.dll; RM.Imb.Cond.Fechamento.Data.dll; RM.Imb.Cond.Fechamento.Service.dll; RM.Imb.Cond.Fechamento.Form.dll

### Rotina: PROPOSTA

* **[Ticket: 26125430 / TINPAD001-21605]** Ajuste para poder excluir venda cancelada e bloquear cancelamento de venda de origem do PI pelo TCGI

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.CalculosBase.dll

## 12.1.2602.105

### Rotina: PROPOSTA - CONDIÇÕES DE PAGAMENTO

* **[Ticket: 26042701 / DTCGI\_INTSYNC-2598]** PI - Melhoria na validação de VPL com relação a valor VPL padrão e da proposta e Melhoria para salvar o valor total encontrado na proposta.

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Regra.Data.dll; RM.Imb.Venda.Regra.Intf.dll

## 12.1.2602.106

### Rotina: Sem Rotina Específica

* **[Ticket: 26044044 / DTCGI\_INTSYNC-2470]** PI - Melhoria no envio da data PI Proposta, Salvando data assinatura, data base, data venda de acordo com informação no momento de enviar ao backoffice.

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.Portal.dll

### Rotina: BÁSICOS

* **[Ticket: 25578180 / TINPAD001-21288]** Ajuste para processo de atualizar em lote, atualizar caracteristicas de subunidades em diferentes unidade tambem

Arquivo: RM.Imb.Venda.Empreendimento.Data.dll

### Rotina: LANÇAMENTO - BAIXA

* **[Ticket: 26280244 / TINPAD001-21825]** Ajustes no processo de baixa do lançamento

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

## 12.1.2602.107

### Rotina: ALUGUEL - ADITIVO ALTERAÇÃO DE LOCATÁRIO

* **[Ticket: 26380380 / TINREV001-25817]** Foi realizado um ajuste no anexo “Aditivos / Alteração de Locatário” do contrato de locação.Ao executar os processos “Efetivar” ou “Desfazer”, o usuário poderá selecionar a nova opção “Desconsiderar Condomínios Calculados”.- Quando a opção estiver marcada: o sistema irá ignorar os condomínios já fechados (calculados) vinculados ao contrato, permitindo a execução do processo normalmente.- Quando a opção não estiver marcada: o comportamento permanece inalterado. Caso existam condomínios fechados vinculados ao contrato, o sistema não permitirá a execução do processo.Essa alteração oferece maior flexibilidade na execução de aditivos e alterações de locatário, especialmente quando já houver movimentações de condomínio registradas.

Arquivos: RM.Imb.Aluguel.ContratoLoc.Server.dll; RM.Imb.Aluguel.Lancamento.Server.dll; RM.Imb.Aluguel.ContratoLoc.Intf.dll; RM.Imb.Aluguel.ContratoLoc.Form.dll

## 12.1.2602.110

### Rotina: Sem Rotina Específica

* **[Ticket: 26121104 / DTCGI\_INTSYNC-2482]** [RM] - Melhoria no giro da roleta, quando uma equipe ou corretor é inativado.

Arquivo: RM.Imb.RoletaVendas.Service.dll

* **[Ticket: DTCGI\_INTSYNC-2497]** Correção adição pessoas adicionais a proposta em Oracle

Arquivo: RM.Imb.Venda.Contrato.Server.dll

### Rotina: COMISSÃO (NOVO MODELO)

* **[Ticket: 25958217 / TINPAD001-21492]** Ajuste nos processos de gerar e cancelar comissão 1.0

Arquivo: RM.Imb.Contratos.Data.dll

## 12.1.2602.111

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: 26531657 / TINREV001-25932]** Melhoria na confissão de divida para que o valor integração seja preenchido nos lançamentos de múltiplas coligadas.

Arquivo: RM.Imb.Aluguel.ConfissaoDivida.Service.dll

### Rotina: FUNDO PROMOCIONAL

* **[Ticket: 25514986 / TINREV001-25935]** Foram realizados ajustes no anexo “Cobrança em Dobro” do cadastro de “Fundo Promocional”. O sistema passa a permitir a alteração do período de cobrança, desde que não existam parcelas geradas para o fundo fora do novo período informado.

Arquivos: RM.Imb.Aluguel.ContratoLoc.Data.dll; RM.Imb.Aluguel.MapaCobranca.Data.dll; RM.Imb.Lib.Intf.dll

### Rotina: MAPA DE DISPONIBILIDADE

* **[Ticket: 26721264 / DTCGI\_INTSYNC-2705]** Melhoria na visão do mapa de disponibilidade

Arquivo: Imb/pvi

### Rotina: PLANO DE PAGAMENTO

* **[Ticket: TINREV001-25934]** Melhoria na confissão de divida para que o valor original considere o valor de integração.

Arquivo: RM.Imb.Aluguel.ConfissaoDivida.Service.dll

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: 26555095 / TINPAD001-21889]** Melhoria na busca da base de cálculo do valor pro-rara para nunca pegar a base que não seja padrão, pois os demais cálculos são valores intermediários e o sistema tem que pegar sempre a base cheia, no final do mês , ou na data base do reajuste que é o primeiro reajuste

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: SISTEMA

* **[Ticket: DTCGI\_INTSYNC-2663]** [RM] - Melhoria em ambiente check do portal de imóveis

Arquivo: RM.Imb.Api.dll

* **[Ticket: DTCGI\_INTSYNC-2663]** Melhoria em ambiente check do portal de imóveis

Arquivo: Imb/pvi

## 12.1.2602.112

### Rotina: CONTRATOS

* **[Ticket: 26485981 / DTCGI\_INTSYNC-2721]** Melhoria para assinar contrato com certificado

Arquivo: Imb/pvi

### Rotina: FUNDO PROMOCIONAL

* **[Ticket: TINREV001-25963]** No cadastro de Fundo em Dobro do Fundo Promocional, o sistema passa a validar se o campo de integração está devidamente informado no tipo de evento financeiro. Quando esse campo estiver preenchido, também será validado se a ação configurada é “Acrescenta”. Essas validações ocorrem quando a forma de cobrança não estiver informada no cadastro do Fundo em Dobro.Essas validações também são realizadas no momento da geração das parcelas do Fundo Promocional no contrato de locação.Caso seja identificada inconsistência nesses parâmetros, as parcelas não serão geradas. Nessa situação, será necessário ajustar as configurações para que o processo possa ser executado posteriormente.

Arquivos: RM.Imb.Aluguel.MapaCobranca.Data.dll; RM.Imb.Aluguel.Lancamento.Server.dll; RM.Imb.Aluguel.MapaCobranca.IServer.dll; RM.Imb.Aluguel.MapaCobranca.Server.dll

### Rotina: SISTEMA

* **[Ticket: DTCGI\_INTSYNC-2662]** PI - Melhoria na unificação base PI-RM (Conversor Base) para cliente que utilizam base oracle no RM - LOG e AUDITTRAIL passam a não bloquear a conversão mais se não conseguirem ser migradas

Arquivo: RM.Imb.Integracao.Server.dll

### Rotina: VENDA - MANUTENÇÃO DE USUÁRIOS

* **[Ticket: 26271037 / TINPAD001-21650]** Ajuste no processo de manutenção de usuários do PDC para enviar email para todos emails cadastrados do comprador

Arquivo: RM.Imb.Venda.Lib.Server.dll

## 12.1.2602.113

### Rotina: PARÂMETROS

* **[Ticket: TINREV001-25878]** Melhoria na confissão de divida, adicionado o campo origem do lançamento nos parametros financeiros

Arquivos: RM.Imb.Aluguel.ConfissaoDivida.Data.dll; RM.Imb.Consts.dll; RM.Imb.Aluguel.ConfissaoDivida.Form.dll; RM.Imb.Aluguel.ConfissaoDivida.Intf.dll

### Rotina: SISTEMA

* **[Ticket: DTCGI\_INTSYNC-2723]** [RM] - API para banner do portal

Arquivos: RM.Imb.Api.dll; RM.Imb.Cadastros.IServer.dll; RM.Imb.Cadastros.Server.dll

### Rotina: VENDA - DIMOB

* **[Ticket: 26690409 / TINPAD001-21847]** Venda distratada não está sendo enviada para o arquivo DIMOB, mesmo existindo parcelas pagas em 2025.

Arquivo: RM.Imb.DIMOB.Server.dll

## 12.1.2602.114

### Rotina: CONTRATO DE VENDA

* **[Ticket: 25988023 / TINPAD001-21510]** Mellhoria na performance na tela de alteração de cadastro global

Arquivo: RM.Imb.Venda.Contrato.Form.dll

### Rotina: PARÂMETROS

* **[Ticket: TINREV001-25971]** Melhoria na confissão de divida, adicionado o campo origem do lançamento nos parametros financeiros

Arquivos: RM.Imb.Aluguel.ConfissaoDivida.Data.dll; RM.Imb.Aluguel.ConfissaoDivida.Service.dll

### Rotina: PROPOSTA - MINUTAS

* **[Ticket: 26662699 / DTCGI\_INTSYNC-2661]** Ajuste para exibir valor por extenso da tag valor total corrigido

Arquivo: Imb/pvi

### Rotina: SISTEMA

* **[Ticket: DTCGI\_INTSYNC-2723]** Modal de divulgação de produto

Arquivo: Imb/pvi

### Rotina: SPED/EFD

* **[Ticket: 25553154 / TINPAD001-21309]** Ajuste para log do sped salvar em diretório compartilhado

Arquivo: RM.Imb.Empreendimento.Server.dll

## 12.1.2602.115

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21771]** Melhoria no novo resíduo para distribuir valor nas parcelas futuras ou criar uma parcela e também o processo de desfazer a distribuição

Arquivos: RM.Imb.Venda.Calc.CalculosBase.Controller.dll; RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Calc.Lib.dll; RM.Imb.Venda.Financeiro.Server.dll; RM.Imb.Venda.Regra.Data.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Venda.Financeiro.Data.dll; RM.Imb.Venda.Financeiro.IServer.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Consts.dll; RM.Imb.Venda.Resources.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Financeiro.Intf.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll

* **[Ticket: TINPAD001-21771]** Implementação do cálculo o resíduo para a nova máquina de ´calulo, foi criado um objeto para cada tipo de resíduo para herdar do CM e Juros

Arquivos: RM.Imb.Venda.Calc.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Api.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Lancamento.Server.dll; RM.Imb.Contratos.Data.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll; RM.Imb.Venda.Financeiro.Server.dll; RM.Imb.Venda.Reajuste.Server.dll; RM.Imb.Venda.Upg.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll; RM.Imb.Venda.Calc.Formula.dll; RM.Imb.Venda.Regra.Data.dll; RM.Imb.Venda.Regra.Form.dll; RM.Imb.Venda.Lib.Server.dll; RM.Imb.Venda.Calc.Lib.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Cobranca.Server.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Calc.CalculosBase.Controller.dll; RM.Imb.Relatorio.Data.dll; RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Integracao.Server.dll; RM.Imb.Venda.Contrato.Server.dll

* **[Ticket: 26706431 / TINPAD001-21855]** Ajusta datas do comprador e componentes conforme nova data da venda

Arquivos: RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Calc.Calculos.Proc.Portal.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Calc.Lib.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

## 12.1.2602.116

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21771]** Implementação do cálculo o resíduo para a nova máquina de ´calulo, foi criado um objeto para cada tipo de resíduo para herdar do CM e Juros

Arquivos: RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Financeiro.Data.dll; RM.Imb.Venda.Financeiro.Server.dll; RM.Imb.Venda.Financeiro.Intf.dll

* **[Ticket: TINPAD001-21771]** Melhoria no novo resíduo para distribuir valor nas parcelas futuras ou criar uma parcela e também o processo de desfazer a distribuição

Arquivos: RM.Imb.Venda.Facade.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Venda.IFacade.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Menu.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Financeiro.Intf.dll; RM.Imb.Venda.Calc.CalculosBase.Controller.dll; RM.Imb.Venda.Financeiro.Data.dll; RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Reajuste.Form.dll; RM.Imb.Venda.Reajuste.Form.dll; RM.Imb.Venda.Calc.Lib.dll

### Rotina: INTEGRAÇÃO

* **[Ticket: DTCGI\_INTSYNC-2455]** PI - Melhoria na notificação de associar lead ao corretor pela roleta, quando a roleta for executada e tiver associado leads para um corretor, será enviada mensagem via whatsapp.

Arquivos: RM.Imb.RoletaVendas.Service.dll; RM.Imb.RoletaVendas.Intf.dll; RM.Imb.Venda.Contrato.Data.dll

* **[Ticket: DTCGI\_INTSYNC-2737]** Melhoria na sessão da RD para o cliente não ficar sem a integração

Arquivo: Imb/pvi

* **[Ticket: DTCGI\_INTSYNC-2455]** PI - Melhoria na unificação base PI-RM (Conversor Base) para cliente que utilizam base oracle no RM - LOG e AUDITTRAIL passam a não bloquear a conversão mais se não conseguirem ser migradas

Arquivo: RM.Imb.Integracao.Server.dll

## 12.1.2602.117

### Rotina: Sem Rotina Específica

* **[Ticket: 26860633 / TINREV001-26047]** Melhoria no processo de geração de despesas para considerar o parâmetro financeiro conforme a coligada da despesa.

Arquivo: RM.Imb.ControleDespesa.Service.dll

### Rotina: ALUGUEL - APP

* **[Ticket: 26763928 / TINPAD001-21901]** Ajuste no processo de notificações de boleto no app

Arquivo: RM.Imb.Cobranca.Data.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21917]** Melhoria no reajuste para utilizar um valor base fixo para reajustar a partir de uma data e criar esse ponto do importador

Arquivos: RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Contrato.Form.dll

* **[Ticket: TINPAD001-21917]** Melhoria no reajuste para utilizar um valor base fixo para reajustar a partir de uma data e criar esse ponto do importadorMelhoria na reforma tributaria para tratar redutor de ajuste , são redutores que ocorrem na obra do condominio

Arquivos: RM.Imb.Venda.Empreendimento.Form.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Menu.dll

### Rotina: FECHAMENTO DO CONDOMÍNIO

* **[Ticket: 26546409 / TINREV001-26017]** Melhoria no cálculo de locação no mapa de cobrança, considerando apenas eventos financeiros de origem locação.

Arquivo: RM.Imb.Aluguel.MapaCobranca.Data.dll

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: TINPAD001-21772]** Melhoria no reajuste para utilizar um valor base fixo para reajustar a partir de uma data e criar esse ponto do importadorMelhoria na reforma tributaria para tratar redutor de ajuste , são redutores que ocorrem na obra do condominio

Arquivos: RM.Imb.Consts.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Contrato.Data.dll

* **[Ticket: TINPAD001-21772]** Melhoria na apuração de compentencia para fazer automatico.

Arquivos: RM.Imb.Venda.Financeiro.Data.dll; RM.Imb.Venda.Aditivo.Data.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Venda.Lib.Server.dll; RM.Imb.Venda.Financeiro.IServer.dll; RM.Imb.Venda.Financeiro.Server.dll

### Rotina: ROLETA DE VENDAS

* **[Ticket: 26758843 / DTCGI\_INTSYNC-2730]** [RM] - Melhoria no giro da roleta de leads para que a distribuição e ordeação dos corretores sejam gravadas em banco para que seja possível obter informações de posições dos corretores na fila

Arquivos: RM.Imb.RoletaVendas.Data.dll; RM.Imb.RoletaVendas.Service.dll; RM.Imb.RoletaVendas.Intf.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: 26365381 / TINPAD001-21711]** Habilitando troca de data da emissão para Distrato

Arquivo: RM.Imb.Venda.Contrato.Server.dll

## 12.1.2602.119

### Rotina: DASHBOARD

* **[Ticket: 26741311 / DTCGI\_INTSYNC-2731]** [RM] - Ajustes ao cadastrar pessoa na proposta como solteiro

Arquivo: RM.Imb.Venda.Financeiro.Server.dll

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: TINPAD001-21772]** Melhoria na distribuição do Resíduo

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

## 12.1.2602.123

### Rotina: VENDA - DIMOB

* **[Ticket: 26701806 / TINPAD001-21908]** Ajuste no relatorio DIMOB ao gerar intermediação

Arquivo: RM.Imb.DIMOB.Server.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: 26726377 / TINPAD001-21907]** Correção nas vendas quitadas para realização do distrato

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

## 12.1.2602.124

### Rotina: Sem Rotina Específica

* **[Ticket: DTCGI\_INTSYNC-2862]** [RM] - Ajuste na validação dos campos obrigatórios

Arquivo: RM.Imb.Venda.Financeiro.Data.dll

* **[Ticket: 26859541 / TINPAD001-21993]** ajuste no relatório de Informe de pagamentos para não retornar saldo de vendas distratadas

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

* **[Ticket: TINPAD001-22057]** Ajustes para que seja possível converter comissões

Arquivo: RM.Imb.Conversor.Server.dll

### Rotina: ALUGUEL - DIMOB

* **[Ticket: 26543864 / TINREV001-26018]** Foi realizada a identificação e inclusão, na DIMOB, dos lançamentos confessados e baixados. Esses valores passam a ser registrados no registro R2 (Ficha de Locação).

Arquivos: RM.Imb.Lib.dll; RM.Imb.DIMOB.IServer.dll; RM.Imb.DIMOB.Server.dll

### Rotina: APURAÇÃO DE COMPETÊNCIA

* **[Ticket: TINPAD001-21904]** melhoria no arredondamento da comissão para 6 casas

Arquivo: RM.Imb.Venda.Calc.CalculosBase.Controller.dll

### Rotina: COCKPIT

* **[Ticket: 26865577 / TINPAD001-21992]** Melhoria no módulo de despesas para inserir as parcelas de reembolso no plano de financiamento e ao excluir o reembolso excluir a parcela na venda também.Foi criado um parâmetro na integração financeira , financeiro, escolhe o componente que fará a referência na regra da venda. Com isso, o módulo de cobrança. apuração de competência, ficha financeira e IR, tratará as parcelas das despesas. Ajuste no cockpit para não duplicar os dados das despesas e permitir o cliente filtra por ativo, mudanças nas cores de acordo com a situação e o nome do comprador principal

Arquivos: RM.Imb.CockPit.Data.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Parametros.Data.dll; RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Api.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll; RM.Imb.ControleDespesa.Service.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Venda.Distrato.Data.dll; RM.Imb.Venda.Financeiro.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Empreendimento.Server.dll; RM.Imb.Atendimento.Form.dll; RM.Imb.Venda.Financeiro.Server.dll; RM.Imb.Consts.dll; RM.Imb.Parametros.Form.dll; RM.Imb.Venda.Financeiro.IServer.dll; RM.Imb.Venda.Aditivo.Data.dll; RM.Imb.Venda.Calc.Lib.dll; RM.Imb.Parametros.Intf.dll; RM.Imb.Venda.Empreendimento.Data.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.CockPit.Wpf.dll; RM.Imb.Atendimento.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Resources.dll; RM.Imb.CockPit.Intf.dll; RM.Imb.Venda.Financeiro.Intf.dll; RM.Imb.Venda.Regra.Data.dll; RM.Imb.DIMOB.Server.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21916]** resíduo para chamar o reajuste online

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Reajuste.Server.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Calc.Formula.dll

### Rotina: EMPREENDIMENTOS

* **[Ticket: 26659323 / DTCGI\_INTSYNC-2695]** Ajuste audittrail para evitar lentidão

Arquivo: Imb/pvi

### Rotina: FECHAMENTO DO CONDOMÍNIO

* **[Ticket: 26883338 / TINREV001-26076]** Melhoria no cadastro de associação de cobrança por orçamento

Arquivos: RM.Imb.Cond.Cadastros.Intf.dll; RM.Imb.Cond.Fechamento.Service.dll; RM.Imb.Cond.Cadastros.Form.dll; RM.Imb.Menu.dll; RM.Imb.Cond.Cadastros.Data.dll

### Rotina: PESSOAS

* **[Ticket: 26882373 / DTCGI\_INTSYNC-2830]** Remoção do caractere + nos campos de telefone quando vazios

Arquivo: Imb/portalgestaoimoveis

## 12.1.2602.125

### Rotina: ALUGUEL - CALCULO

* **[Ticket: TINREV001-25970]** Ajuste no cálculo do reajuste do CTO do Processo de "Aplicar Reajuste" do Contrato de locação.Foi realizado um ajuste no cálculo do reajuste do CTO do processo de "Aplicar Reajuste" do contrato de locação. Passa a contemplar a criação de uma faixa de faturamento adicional quando a data de reajuste ocorrer no meio do mês (a partir do dia 2).Nessa situação, será criada uma faixa intermediária correspondente ao mês do reajuste, iniciando no primeiro dia e finalizando no último dia do mês. Esse comportamento ocorre somente quando o contrato estiver configurado para utilizar pró-rata no reajuste.Exemplo:Considerando um reajuste com data em 20 de janeiro:A faixa anterior será encerrada em 31 de dezembro do ano anterior;Será criada uma faixa intermediária para o mês de janeiro (01/01 a 31/01), com cálculo pró-rata:Do dia 01 até 19, será considerado o valor anterior;A partir do dia 20, será aplicado o novo valor reajustado.Em seguida, será criada uma nova faixa a partir de 01 de fevereiro, já com o valor reajustado integral.

Arquivo: RM.Imb.Aluguel.Reajuste.Server.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21916]** implementação do novo parâmetro do RET no empreendimento

Arquivos: RM.Imb.Empreendimento.Server.dll; RM.Imb.Empreendimento.IServer.dll; RM.Imb.Venda.Empreendimento.Form.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: FECHAMENTO DO CONDOMÍNIO

* **[Ticket: 26882384 / TINREV001-26072]** Ajuste no cálculo de subsídio no módulo de Shopping, considerando regras de CTO, descontos e valores zerados.

Arquivo: RM.Imb.Cond.Fechamento.Service.dll

### Rotina: SPED/EFD

* **[Ticket: 26785702 / TINPAD001-21974]** ajuste de parametrôs para a geração de arquivos EFD

Arquivo: RM.Imb.Empreendimento.Server.dll

## 12.1.2602.127

### Rotina: GERAIS

* **[Ticket: TINPAD001-21958]** Configuração Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Form.dll; RM.Imb.RDStation.Marketing.SmartLink.Server.dll; RM.Imb.Venda.Resources.dll; RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.Venda.Distrato.Data.dll; RM.Imb.RDStation.Marketing.SmartLink.Data.dll; RM.Imb.RDStation.Marketing.SmartLink.Service.dll; RM.Imb.Venda.Contrato.Data.dll

* **[Ticket: TINPAD001-21958]** Menu Configuração Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Form.dll; RM.Imb.Menu.dll

* **[Ticket: TINPAD001-21958]** Ajuste e-mail Configuração Integração RD Station Marketing Smartlink

Arquivo: RM.Imb.RDStation.Marketing.SmartLink.Server.dll

* **[Ticket: TINPAD001-21958]** Json Configuração Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.RDStation.Marketing.SmartLink.Server.dll; RM.Imb.RDStation.Marketing.SmartLink.Service.dll

* **[Ticket: TINPAD001-21958]** Ajuste mensagem Configuração Integração RD Station Marketing Smartlink

Arquivo: RM.Imb.RDStation.Marketing.SmartLink.Form.dll

### Rotina: PROPOSTA

* **[Ticket: 27118206 / DTCGI\_INTSYNC-2932]** [RM] - Ajuste para pegar valor de parâmetros independente se variável maiúscula ou minúscula

Arquivo: RM.Imb.Parametros.Data.dll

### Rotina: PROPOSTA - ASSINATURA ELETRÔNICA

* **[Ticket: DTCGI\_INTSYNC-2745]** Criação da opção de assinatura eletrônica da proposta de aquisição padrão do portal

Arquivo: Imb/pvi

* **[Ticket: DTCGI\_INTSYNC-2745]** Melhoria na mensagem quando não tem permissão de acesso ao menu

Arquivo: Imb/pvi

### Rotina: VENDA - PDC

* **[Ticket: TINPAD001-22067]** Ajustes gerais no acelerador

Arquivo: Imb/portal-imobiliario

* **[Ticket: TINPAD001-22067]** Ajuste no qrcode da ultima etapa do acelerador para atualizar de acordo com o parametro

Arquivo: RM.Imb.Api.dll

## 12.1.2602.129

### Rotina: Sem Rotina Específica

* **[Ticket: TINPAD001-21425]** Ajustes nos serviços do acelerador

Arquivo: RM.Imb.Cadastros.Server.dll

* **[Ticket: TINPAD001-21425]** Pequenas melhorias e ajustes

Arquivo: Imb/portal-imobiliario

* **[Ticket: 26905657 / DTCGI\_INTSYNC-2827]** PI - Melhoria performance do sincronismo de dados para o PI

Arquivo: RM.Imb.Integracao.Server.dll

### Rotina: EMPREENDIMENTOS

* **[Ticket: DTCGI\_INTSYNC-2920]** PI - Melhoria na gravação dos dados da tabela AUDITTRAIL, Criação do serviço que será responsavel por gravar em jobassincrono.

Arquivos: RM.Imb.Api.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Venda.Resources.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Integracao.Intf.dll; RM.Imb.Integracao.Server.dll; RM.Imb.Venda.Lib.Server.dll; Imb/pvi

### Rotina: GERAIS

* **[Ticket: TINPAD001-21958]** Provisionamento IPaaS Configuração Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Server.dll; RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.RDStation.Marketing.SmartLink.Data.dll; RM.Imb.RDStation.Marketing.SmartLink.Form.dll

### Rotina: PLANO DE PAGAMENTO

* **[Ticket: TINREV001-26120]** Melhoria no confissão de dívida referente a opção de separação de juros e multa.

Arquivos: RM.Imb.Aluguel.ConfissaoDivida.IService.dll; RM.Imb.Aluguel.ConfissaoDivida.Form.dll; RM.Imb.Aluguel.ConfissaoDivida.Service.dll; RM.Imb.Aluguel.ConfissaoDivida.Intf.dll; RM.Imb.Aluguel.ConfissaoDivida.Data.dll; RM.Imb.Menu.dll

### Rotina: PROPOSTA - ASSINATURA ELETRÔNICA

* **[Ticket: DTCGI\_INTSYNC-2745]** Validar se tem assinatura eletrônica configurada para enviar documento para o TAE

Arquivo: Imb/pvi

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22146]** Implementação de log na contabilização do reajuste e formula

Arquivos: RM.Imb.Venda.Resources.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Log.Form.dll; RM.Imb.Recursos.dll; RM.Imb.Formula.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Log.Data.dll; RM.Imb.Venda.Reajuste.Form.dll; RM.Imb.Venda.Calc.Formula.dll; RM.Imb.Venda.Calc.Lib.dll; RM.Imb.Log.Intf.dll

### Rotina: VENDA - PDC

* **[Ticket: TINPAD001-21927]** Ajustando angular elements para incluir nova galeria de fotos no portal PDC(antigo PDC)

Arquivo: Imb/portalcliente

* **[Ticket: TINPAD001-21927]** REVERT: Ajustando angular elements para incluir nova galeria de fotos no portal PDC(antigo PDC)

Arquivo: Imb/portalcliente

## 12.1.2602.130

### Rotina: GERAIS

* **[Ticket: TINPAD001-21958]** Log Provisionamento IPaaS Configuração Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Server.dll; RM.Imb.RDStation.Marketing.SmartLink.Data.dll

* **[Ticket: TINPAD001-21958]** Novos eventos Quitar e Cancelar Contrato Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Venda.Contrato.Server.dll; RM.Imb.RDStation.Marketing.SmartLink.Server.dll

### Rotina: PLANO DE PAGAMENTO

* **[Ticket: TINREV001-26120]** Melhoria no confissão de dívida referente a opção de separação de juros e multa.

Arquivo: RM.Imb.Aluguel.ConfissaoDivida.Intf.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22146]** Implementação de log na contabilização do reajuste e a parametrização tributária

Arquivos: RM.Imb.Contratos.IServer.dll; RM.Imb.Cadastros.Form.dll; RM.Imb.Venda.Empreendimento.Data.dll; RM.Imb.Contratos.Data.dll

* **[Ticket: TINPAD001-22146]** AJuste na reforma tributaria para o financeiro

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

## 12.1.2602.131

### Rotina: ALUGUEL - RELATÓRIOS

* **[Ticket: 27018380 / TINREV001-26121]** Foi realizado um ajuste no relatório “Extrato do Condomínio na Competência” para garantir a exibição das informações também quando o processo de apuração for executado de forma individualizada.

Arquivo: RM.Imb.Aluguel.Relatorio.Service.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21420]** Nova Reforma tributária no TCGI

Arquivos: RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Cadastros.Form.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Calc.CalculosBase.Controller.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Empreendimento.Data.dll

* **[Ticket: TINPAD001-21420]** melhoria na tela de regime de casamento

Arquivo: RM.Imb.Cadastros.Form.dll

### Rotina: MODELOS DE CONTRATOS

* **[Ticket: 27120047 / TINREV001-26123]** Foi realizado um ajuste na busca do modelo de contrato ao criar um novo contrato. O sistema não estava trazendo a fórmula de DIMOB quando ela estava definida no modelo.

Arquivos: RM.Imb.Aluguel.ContratoLoc.Form.dll; RM.Imb.Aluguel.ContratoLoc.Intf.dll

### Rotina: PESSOAS

* **[Ticket: 27012110 / DTCGI\_INTSYNC-2876]** Ajuste pagina de pessa migrada para que seja atualizado o status após a atualização de um interesse para Perdido

Arquivo: Imb/pvi

* **[Ticket: 27010332 / DTCGI\_INTSYNC-2905]** Ajuste no status do lead após inserir registro na Timeline

Arquivos: Imb/portalgestaoimoveis; Imb/pvi

## 12.1.2602.132

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21420]** melhoria na tela de regime de casamento

Arquivo: RM.Imb.Venda.Empreendimento.Form.dll

### Rotina: GERAIS

* **[Ticket: TINPAD001-21958]** Novos campos contato e contrato Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.RDStation.Marketing.SmartLink.Server.dll

### Rotina: PESSOAS

* **[Ticket: 27012110 / DTCGI\_INTSYNC-2876]** Ajuste pagina de pessa migrada para que seja atualizado o status após a atualização de um interesse para Perdido

Arquivo: Imb/portalgestaoimoveis

### Rotina: ROLETA DE VENDAS

* **[Ticket: DTCGI\_INTSYNC-2895]** [RM] - Ajuste para exclusão de Roleta de leads, removendo referencias da roleta na tabela de fila do lead

Arquivo: RM.Imb.RoletaVendas.Data.dll

## 12.1.2602.133

### Rotina: COMISSÃO

* **[Ticket: 27101068 / TINPAD001-22144]** Ajuste na função de fórmula TABEMPREENDIMENTOCOMPL, que não está retornando valor na comissão da venda

Arquivo: RM.Imb.Venda.Calc.Formula.dll

### Rotina: DESPESA DE VENDA

* **[Ticket: 26980326 / TINPAD001-22028]** TCGI - Vendas - Ajuste para o processo Regerar Pagamento Despesa não processar parcelas com data vencimento anterior a data referência para troar de responsavel

Arquivos: RM.Imb.ControleDespesa.IService.dll; RM.Imb.ControleDespesa.Data.dll; RM.Imb.ControleDespesa.Service.dll

### Rotina: GERAIS

* **[Ticket: TINPAD001-21958]** Adicionando projeto de teste a Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.RDStation.Marketing.SmartLink.Server.dll

### Rotina: ROLETA DE VENDAS

* **[Ticket: DTCGI\_INTSYNC-2895]** Ajuste exclusão de Roleta de leads e Equpe da roleta

Arquivo: Imb/portalgestaoimoveis

* **[Ticket: DTCGI\_INTSYNC-2931]** [RM] - Ajuste para exclusão de Roleta de leads, removendo referencias da roleta na tabela de fila do lead

Arquivos: RM.Imb.RoletaVendas.Service.dll; RM.Imb.RoletaVendas.Intf.dll

## 12.1.2602.135

### Rotina: ALUGUEL - ADITIVO RENEGOCIAÇÃO DE DÍVIDA

* **[Ticket: 27179800 / TINREV001-26149]** Foram realizados ajustes nos processos de “Efetivar Aditivo” e “Desfazer Aditivo” do contrato de locação. O sistema passa a permitir a execução quando a data do aditivo for igual à data de reajuste do contrato. Anteriormente, a execução era permitida apenas quando a data do aditivo era inferior.

Arquivos: RM.Imb.Aluguel.ContratoLoc.Data.dll; RM.Imb.Aluguel.ContratoLoc.Server.dll; RM.Imb.Recursos.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21420]** Melhoria na reforma tributária com fórmulas e tela

Arquivos: RM.Imb.Formula.dll; RM.Imb.Venda.Distrato.Data.dll; RM.Imb.Venda.Calc.Formula.dll; RM.Imb.Recursos.dll

* **[Ticket: TINPAD001-21420]** AJuste na reforma tributária do log

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

### Rotina: GERAIS

* **[Ticket: TINPAD001-21958]** Ajuste totvsId Integração RD Station Marketing Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Server.dll; RM.Imb.RDStation.Marketing.SmartLink.Intf.dll

## 12.1.2602.136

### Rotina: CONTRATO DE LOCAÇÃO

* **[Ticket: TINREV001-25467]** Incluído o processo “Gerar Movimento de Locação” no cadastro de contratos de locação.Esse processo tem como finalidade identificar e processar as baixas de locação realizadas dentro do período informado pelo usuário, considerando os parâmetros definidos na tela de execução.

Arquivos: RM.Imb.Menu.dll; RM.Imb.Aluguel.Facade.dll; RM.Imb.Aluguel.ContratoLoc.Data.dll; RM.Imb.Aluguel.ContratoLoc.Intf.dll; RM.Imb.Aluguel.ContratoLoc.Form.dll; RM.Imb.Lib.dll; RM.Imb.Aluguel.Integracao.IService.dll; RM.Imb.Aluguel.Integracao.Service.dll

* **[Ticket: TINREV001-25758]** Adicionado o processo “Cancelar Movimento de Locação” na visão “Movimentos Gerados por Pagamento”, permitindo o cancelamento dos movimentos gerados a partir das baixas de locação.

Arquivos: RM.Imb.Aluguel.Facade.dll; RM.Imb.Lib.dll; RM.Imb.Menu.dll; RM.Imb.Aluguel.Integracao.IService.dll; RM.Imb.Aluguel.ContratoLoc.Form.dll; RM.Imb.Server.dll; RM.Imb.Aluguel.ContratoLoc.Data.dll; RM.Imb.Aluguel.Integracao.Service.dll

* **[Ticket: TINREV001-26152]** Adicionado o anexo “Movimentos Gerados por Pagamento” no contrato de locação, onde serão exibidas as informações dos movimentos gerados a partir da baixa dos lançamentos de aluguel.

Arquivos: RM.Imb.Aluguel.ContratoLoc.Data.dll; RM.Imb.Aluguel.ContratoLoc.Intf.dll; RM.Imb.Menu.dll; RM.Imb.Server.dll; RM.Imb.Lib.dll; RM.Imb.Recursos.dll; RM.Imb.Aluguel.ContratoLoc.Form.dll

### Rotina: GERAR LANÇAMENTO FINANCEIRO

* **[Ticket: TINREV001-25936]** O processo de geração dos lançamentos financeiros do aluguel no contrato de locação foi atualizado para atender às novas regras da reforma tributária. A partir dessa atualização, o sistema passa a calcular automaticamente os tributos conforme a regra tributária definida no contrato de locação. Os tributos serão calculados quando todas as condições abaixo forem atendidas: Houver uma regra tributária definida no contrato de locação; O valor do aluguel, deduzido do valor de redução(valor de redução multiplicado pela quantidade de imóveis residenciais), for maior que zero. Em outras palavras, o cálculo dos tributos ocorrerá somente quando houver base de cálculo positiva. O valor de dedução é aplicável somente a imóveis residenciais vinculados ao contrato, demais tipos de imóveis não terão dedução e o valor do imposto será calculado em cima do valor total de locação.

Arquivos: RM.Imb.Aluguel.ContratoLoc.IServer.dll; RM.Imb.Aluguel.ContratoLoc.Server.dll; RM.Imb.Venda.Facade.dll; RM.Imb.Aluguel.Imovel.Intf.dll; RM.Imb.Aluguel.Imovel.Data.dll; RM.Imb.Aluguel.Facade.dll; RM.Imb.Aluguel.Lancamento.Server.dll; RM.Imb.Aluguel.Imovel.Form.dll; RM.Imb.Aluguel.Lancamento.IServer.dll

### Rotina: PROPOSTA

* **[Ticket: 27287531 / DTCGI\_INTSYNC-3021]** [RM] - Melhoria no filtro dos lookups Portal Imóveis

Arquivos: RM.Imb.Cadastros.Server.dll; RM.Imb.Cadastros.IServer.dll; RM.Imb.Api.dll

* **[Ticket: 27287531 / DTCGI\_INTSYNC-3021]** Melhoria no filtro dos lookups Portal Imóveis

Arquivo: Imb/portalgestaoimoveis

## 12.1.2602.137

### Rotina: CONTABILIZAÇÃO DE TRANSFERÊNCIA LONGO P/ CURTO PRAZO

* **[Ticket: 26499408 / TINPAD001-21791]** Melhoria no tratamento da de novos campo e no Rel IRRF

Arquivos: RM.Imb.Relatorio.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll; RM.Imb.Relatorio.Form.dll

### Rotina: CONTRATO DE LOCAÇÃO

* **[Ticket: TINREV001-25758]** Adicionado o processo “Cancelar Movimento de Locação” na visão “Movimentos Gerados por Pagamento”, permitindo o cancelamento dos movimentos gerados a partir das baixas de locação.

Arquivos: RM.Imb.Aluguel.ContratoLoc.Data.dll; RM.Imb.Aluguel.ContratoLoc.Intf.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: 27139212 / TINPAD001-22281]** TCGI - Vendas - Pequenas correções ao entrar no modulo do TCGI

Arquivo: RM.Imb.Parametros.Intf.dll

### Rotina: IMPORTADOR DE BAIXAS

* **[Ticket: 27018195 / TINPAD001-22047]** valor da parcela que não estava refletindo na tela

Arquivo: RM.Imb.Venda.Financeiro.Data.dll

### Rotina: MÓDULO DE COBRANÇA

* **[Ticket: 27150695 / TINPAD001-22181]** Ajuste no parâmetro ao gerar ação manual de cobrança do tipo Whatsapp.

Arquivo: RM.Imb.Facade.dll

### Rotina: PDC - RELATÓRIOS

* **[Ticket: 27248428 / TINPAD001-22192]** TCGI - Vendas - Ajuste na geração da ficha financeira no PDC

Arquivo: RM.Imb.PortalCliente.Server.dll

### Rotina: VENDA - CALCULO

* **[Ticket: 27167126 / TINPAD001-22182]** Ajuste ao aplicar o reajuste de juros do contrato de venda, o valor de juros não é aplicado nas parcelas.

Arquivos: RM.Imb.Venda.Calc.CalculosBase.Controller.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.CalculosBase.dll

## 12.1.2602.138

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-22171]** Criação de novo campo de motivo de venda para seguir os requisitos da integração com o RD Station.

Arquivos: RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Recursos.dll; RM.Imb.Venda.Resources.dll; RM.Imb.Log.Data.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Log.Intf.dll

### Rotina: FICHA FINANCEIRA

* **[Ticket: 27311485 / TINREV001-26209]** Relatórios de ficha financeira de aluguel, deixam de exibir lançamentos cancelados.

Arquivo: RM.Imb.Aluguel.Relatorio.Data.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22146]** Melhoria no distrato para salvar a foto das parcelas no momento antes de cancelar, o sistema faz o reajuste em memória para o dia do distrato

Arquivos: RM.Imb.Venda.Reajuste.Data.dll; RM.Imb.Venda.Distrato.Data.dll; RM.Imb.Venda.Calc.Lib.dll; RM.Imb.Venda.Resources.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll; RM.Imb.Venda.Distrato.Form.dll; RM.Imb.Venda.Aditivo.Form.dll; RM.Imb.Venda.Calc.Formula.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Distrato.Intf.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

## 12.1.2602.139

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-21420]** Desfazer a alteração do campo novo

Arquivos: RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Venda.Resources.dll; RM.Imb.Log.Intf.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Log.Data.dll; RM.Imb.Recursos.dll

## 12.1.2602.140

### Rotina: CONTRATOS

* **[Ticket: DTCGI\_INTSYNC-2977]** Opção de baixar todos os documentos de pessoa

Arquivo: Imb/pvi

### Rotina: ITEM DE COBRANÇA

* **[Ticket: 27317230 / TINREV001-26216]** O processo “Excluir Cálculo” do fechamento de condomínio por competência passa a verificar se existem processos integrados. Caso existam, a exclusão não será realizada.

Arquivo: RM.Imb.Cond.Fechamento.Service.dll

## 12.1.2602.142

### Rotina: ENCERRAR/ RESCINDIR CONTRATO DE LOCAÇÃO

* **[Ticket: TINREV001-26278]** Ajuste no processo de efetivar rescisão e efetivar aditivo alteração de vigência. Reforma tributária.

Arquivo: RM.Imb.Aluguel.Lancamento.Server.dll

### Rotina: PROPOSTA

* **[Ticket: 27427071 / DTCGI\_INTSYNC-3107]** PI - Melhoria SMTP envio email em mensagens da proposta/contrato

Arquivo: Imb/pvi

## 12.1.2602.143

### Rotina: Sem Rotina Específica

* **[Ticket: TINPAD001-22342]** Desfazer a alteração do log

Arquivo: RM.Imb.Venda.Calc.Calculos.dll

* **[Ticket: TINPAD001-22342]** AJuste no para de reajsute on-line

Arquivo: RM.Imb.Venda.Financeiro.Data.dll

### Rotina: PESSOAS

* **[Ticket: 27147061 / DTCGI\_INTSYNC-3130]** PI - Melhoria para recuperar dados em memoria para utilização de telas novas no PI Migrado.

Arquivo: Imb/pvi

## 12.1.2602.144

### Rotina: SINCRONIZAR

* **[Ticket: 27470647 / DTCGI\_INTSYNC-3096]** PI - Melhoria no tratamento de data para salvar no sincronismo de empreendimento e na carga de dados, para atualizar ou incluir

Arquivo: RM.Imb.Integracao.Server.dll

## 12.1.2602.145

### Rotina: Sem Rotina Específica

* **[Ticket: 27293034 / TINPAD001-22227]** Melhoria na apuração de competência para não juntar o valor de desconto com a baixa e criar dois novos com o valores do TCGI

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Financeiro.Intf.dll; RM.Imb.Venda.Financeiro.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: COCKPIT

* **[Ticket: 27357673 / TINPAD001-22266]** Correção realizada no cockpit aonde os dados do contrato do cliente não estavam sendo carregados.

Arquivo: RM.Imb.CockPit.Data.dll

### Rotina: CONFIGURAÇÃO

* **[Ticket: TINREV001-24202]** Foi realizada uma alteração no processo de confissão de dívida. Agora é permitido informar desconto sobre juros e multa.O desconto pode ser definido: Por percentual; ou Por valor, limitado ao valor calculado de juros ou multa.A taxa de desconto deve estar entre 0% (zero) e 100%, e o valor informado não pode ser negativo.

Arquivos: RM.Imb.Aluguel.ConfissaoDivida.IService.dll; RM.Imb.Aluguel.ConfissaoDivida.Form.dll; RM.Imb.Aluguel.ConfissaoDivida.Data.dll; RM.Imb.Aluguel.ConfissaoDivida.Service.dll; RM.Imb.Aluguel.ConfissaoDivida.Intf.dll

### Rotina: GERAR LANÇAMENTO FINANCEIRO

* **[Ticket: TINREV001-25756]** O processo de geração de aluguel complementar do contrato de locação foi atualizado para atender às novas regras da reforma tributária.A partir dessa atualização, o sistema passa a calcular automaticamente os tributos conforme a regra tributária definida no contrato de locação.Os tributos serão calculados quando existir uma regra tributária definida no contrato de locação.Para imóveis residenciais, será aplicado o valor de redução previsto na regra tributária. O valor da redução será calculado conforme a quantidade de imóveis residenciais vinculados ao contrato.Cálculo da redução: Valor de redução × quantidade de imóveis residenciaisPara imóveis não residenciais, os tributos serão calculados sobre o valor integral do aluguel, sem aplicação de redução.Os tributos somente serão calculados quando a base de cálculo resultante for maior que zero.

Arquivos: RM.Imb.Aluguel.Lancamento.IServer.dll; RM.Imb.Aluguel.Lancamento.Server.dll

### Rotina: PROPOSTA

* **[Ticket: 27484812 / TINPAD001-22370]** Melhoria na apuração de competência para não juntar o valor de desconto com a baixa e criar dois novos com o valores do TCGI

Arquivos: RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Facade.dll; RM.Imb.Venda.Distrato.Form.dll

### Rotina: ROLETA DE VENDAS

* **[Ticket: 27629137 / DTCGI\_INTSYNC-3098]** [RM] - Melhoria em integração RDStation CRM V2 para associação de negociações a proposta

Arquivos: RM.Imb.RoletaVendas.Data.dll; RM.Imb.RoletaVendas.Intf.dll; RM.Imb.RoletaVendas.Service.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22321]** Desfazer a Melhoria na exclusão do plano de financiamento quando tiver o TPD para não excluir a parcela

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

## 12.1.2602.146

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-22171]** Inclusão de novo campo de motivo de compra.

Arquivos: RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Log.Data.dll; RM.Imb.Venda.Resources.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Recursos.dll; RM.Imb.Log.Intf.dll

## 12.1.2602.147

### Rotina: ROLETA DE VENDAS

* **[Ticket: 27929511 / DTCGI\_INTSYNC-3181]** PI - Melhoria no tratameno dos dados, quando chega um novo lead do RDSTATION pelo webhook, com impressão do Json, caso precise habilitar parametro 'imprimir\_log\_rdstation'

Arquivo: Imb/pvi

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22321]** Melhoria no distrato para validar a obrigatoriedade da contabilização

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Parametros.Form.dll; RM.Imb.Venda.Distrato.Data.dll; RM.Imb.Parametros.Data.dll; RM.Imb.Parametros.Intf.dll; RM.Imb.Venda.Calc.Calculos.Resources.dll; RM.Imb.Venda.Distrato.Form.dll; RM.Imb.Venda.Calc.Calculos.dll

* **[Ticket: TINPAD001-22321]** Se for boletro hibidro o sistmea não exclui o lancamento

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

## 12.1.2602.148

### Rotina: APURAÇÃO DE COMPETÊNCIA

* **[Ticket: TINPAD001-22282]** Melhoria na apuração para bloquear venda em preparação

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Contratos.Data.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22321]** Melhoria no distrato para validar a obrigatoriedade da contabilização

Arquivo: RM.Imb.Venda.Distrato.Form.dll

## 12.1.2602.149

### Rotina: GERAR LANÇAMENTO FINANCEIRO

* **[Ticket: TINREV001-25757]** O processo de geração de lançamentos do contrato de locação foi atualizado para atender às novas regras da reforma tributária nos casos em que houver cálculo de aluguel em dobro.A partir dessa atualização, o sistema passa a calcular automaticamente os tributos conforme a regra tributária definida no contrato de locação.Os tributos serão calculados quando existir uma regra tributária configurada no contrato de locação.# Comportamento do Aluguel em Dobro Quando o aluguel em dobro não for gerado de forma agregada: - O lançamento do aluguel normal mantém a aplicação da redução para imóveis residenciais sobre a base de cálculo dos tributos; - O lançamento referente ao aluguel em dobro não considera a redução para imóveis residenciais, ou seja, será tratado tributariamente como imóvel comercial.Os tributos somente serão calculados quando a base de cálculo resultante for maior que zero.

Arquivos: RM.Imb.Aluguel.Lancamento.IServer.dll; RM.Imb.Aluguel.Lancamento.Server.dll; RM.Imb.Aluguel.Facade.dll

## 12.1.2602.150

### Rotina: APURAÇÃO DE COMPETÊNCIA

* **[Ticket: TINPAD001-22282]** Melhoria na poisção do botão de executar de andares

Arquivos: RM.Imb.Venda.Empreendimento.Form.dll; RM.Imb.Parametros.Intf.dll; RM.Imb.Cadastros.Data.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: 28160015 / TINPAD001-22444]** Melhoria na versão para forçar a compilação das dlls

Arquivos: RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Venda.Contrato.Server.dll; RM.Imb.Venda.Contrato.IServer.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Api.dll; RM.Imb.Venda.Contrato.Form.dll

### Rotina: PROPOSTA - ASSINATURA ELETRÔNICA

* **[Ticket: 27722368 / DTCGI\_INTSYNC-3180]** Ajuste para enviar documento para o TAE pelo portal de imóveis.

Arquivo: Imb/pvi

## 12.1.2602.151

### Rotina: Sem Rotina Específica

* **[Ticket: TINREV001-26256]** Ao cancelar uma baixa de lançamento originada de aluguel, o sistema irá validar se a baixa está vinculada a algum movimento gerado pelo processo “Gerar Movimento de Locação”.Caso exista vínculo, o cancelamento da baixa não será permitido. Nessa situação, será necessário cancelar primeiro o movimento gerado para, posteriormente, realizar o cancelamento da baixa.

Arquivo: RM.Imb.Aluguel.ConfissaoDivida.Service.dll

### Rotina: APP - SITUAÇÃO FINANCEIRA

* **[Ticket: 27097479 / TINPAD001-22209]** TCGI - Vendas - Ajuste nos valores enviados ao app

Arquivo: RM.Imb.Venda.Calc.Calculos.Proc.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: 28160015 / TINPAD001-22444]** Melhoria na versão para forçar a compilação das dlls para o campo motivo de compra

Arquivos: RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Venda.Contrato.Form.dll

### Rotina: PROPOSTA - CONDIÇÕES DE PAGAMENTO

* **[Ticket: 27722305 / DTCGI\_INTSYNC-3151]** [RM] - Inserção de parametro para permiter ou não mais componentes.

Arquivos: RM.Imb.Venda.Regra.Data.dll; RM.Imb.Venda.Regra.Intf.dll

* **[Ticket: 27722305 / DTCGI\_INTSYNC-3151]** Inserção de parâmetro para permitir ou não mais componentes.

Arquivo: Imb/portalgestaoimoveis

### Rotina: SINCRONIZAR

* **[Ticket: 27586266 / DTCGI\_INTSYNC-3106]** Ajuste no sincronismo do portal sem migrar para base única.

Arquivo: Imb/pvi

### Rotina: VENDA - ADITIVO DE RENEGOCIAÇÃO DE CONTRATO

* **[Ticket: 27081027 / TINPAD001-22154]** Melhoria no renegociador para considerar o sinal da parcela a pagar

Arquivos: RM.Imb.Venda.Resources.dll; RM.Imb.Venda.Regra.Data.dll; RM.Imb.Venda.Financeiro.Server.dll; RM.Imb.Venda.Calc.Calculos.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Parametros.Intf.dll; RM.Imb.Parametros.Data.dll; RM.Imb.Venda.Calc.Calculos.Resources.dll; RM.Imb.Parametros.Form.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Financeiro.Intf.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Venda.Lib.Intf.dll; RM.Imb.Venda.Financeiro.Data.dll

## 12.1.2602.152

### Rotina: ALUGUEL - ADITIVO GARANTIA DO CONTRATO

* **[Ticket: 28086634 / TINREV001-26421]** Foi realizado um ajuste no cadastro de aditivos de “Alteração de Garantias do Contrato” do contrato de locação. O sistema não estava exibindo as garantias anteriores que não possuíam seguro vinculado.

Arquivo: RM.Imb.Aluguel.ContratoLoc.Data.dll

### Rotina: APP - SITUAÇÃO FINANCEIRA

* **[Ticket: 27097479 / TINPAD001-22209]** Melhorias nas funcionalidade das tabelas da tela de situação financeira

Arquivo: Imb/portalcliente

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-22172]** Melhoria na cancelamento do boleto hibrido

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

* **[Ticket: TINPAD001-22172]** Melhoria na validação de executar a apuracao

Arquivo: RM.Imb.Venda.Financeiro.Server.dll

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25955]** Criação do modulo de negociação de boletos do modulo de locação

Arquivos: RM.Imb.Aluguel.Cadastros.Data.dll; RM.Imb.Aluguel.ConfissaoDivida.Service.dll; RM.Imb.Menu.dll; RM.Imb.Shopping.Service.dll; RM.Imb.Shopping.Data.dll; RM.Imb.Aluguel.Lib.Intf.dll; RM.Imb.Shopping.Form.dll; RM.Imb.Aluguel.Cadastros.Form.dll; RM.Imb.Aluguel.Facade.dll; RM.Imb.Consts.dll; RM.Imb.Shopping.Intf.dll; RM.Imb.Recursos.dll; RM.Imb.Aluguel.ConfissaoDivida.Form.dll; RM.Imb.Shopping.IService.dll; RM.Imb.Aluguel.Cadastros.Intf.dll

### Rotina: VENDA - ADITIVO DE RENEGOCIAÇÃO DE CONTRATO

* **[Ticket: 27081027 / TINPAD001-22154]** Melhoria no renegociador para considerar o sinal da parcela a pagar

Arquivos: RM.Imb.Venda.Aditivo.Data.dll; RM.Imb.Venda.Aditivo.Form.dll; RM.Imb.Venda.Aditivo.Intf.dll

## 12.1.2602.153

### Rotina: CADASTROS ALUGUEL

* **[Ticket: TINREV001-25861]** No cadastro de regras redutoras de aluguel, foram adicionadas validações para evitar duplicidade de regras na mesma competência (mês/ano) para valores de redução.Ao incluir ou alterar uma regra redutora, o sistema passa a validar, com base na data inicial informada, se já existem outras regras redutoras dos tipos Aluguel ou Social para a mesma competência. Essa validação também considera os reajustes vinculados às regras.As mesmas validações são realizadas ao incluir ou alterar reajustes das regras redutoras.

Arquivos: RM.Imb.Venda.Empreendimento.Data.dll; RM.Imb.Lib.Intf.dll; RM.Imb.Venda.Empreendimento.Intf.dll

### Rotina: CONTRATO DE VENDA

* **[Ticket: 28294753 / TINPAD001-22496]** Melhoria na comissão para atribuir o valor de %atreado a baixa com fórmula e Melhoria na configuração do componente e melhoria na definição de despesas

Arquivos: RM.Imb.ControleDespesa.Form.dll; RM.Imb.Venda.Regra.Form.dll; RM.Imb.Venda.Calc.Calculos.Proc.Portal.dll

### Rotina: DESPESA DE VENDA

* **[Ticket: 26980326 / TINPAD001-22318]** Ajuste ao aplicar o reajuste de juros do contrato de venda, o valor de juros não é aplicado nas parcelas.

Arquivo: RM.Imb.Venda.Movimento.Data.dll

### Rotina: USO EXTERNO DE API / WEBSERVICE

* **[Ticket: TINPAD001-22377]** TCGI - Vendas - Melhoria para enviar Motivo compra da venda para RD Station Marketing

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.RDStation.Marketing.SmartLink.Server.dll; RM.Imb.RDStation.Marketing.SmartLink.Form.dll; RM.Imb.RDStation.Marketing.SmartLink.Data.dll

* **[Ticket: TINPAD001-22469]** Desenvolvimento do processo de habilitar/desabilitar integração RD Marketing com Smartlink

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Server.dll; RM.Imb.RDStation.Marketing.SmartLink.Form.dll; RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.Parametros.Data.dll; RM.Imb.Parametros.Intf.dll; RM.Imb.RDStation.Marketing.SmartLink.Service.dll; RM.Imb.RDStation.Marketing.SmartLink.Data.dll

## 12.1.2602.154

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-22526]** Melhoria no reajuste com fórmula global

Arquivo: RM.Imb.Venda.Calc.CalculosBase.dll

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25421]** Processo de Negociação de boleto

Arquivos: RM.Imb.Shopping.Intf.dll; RM.Imb.Consts.dll; RM.Imb.Aluguel.ContratoLoc.Intf.dll; RM.Imb.Shopping.Service.dll

### Rotina: USO EXTERNO DE API / WEBSERVICE

* **[Ticket: TINPAD001-22377]** TCGI - Vendas - Pequenos ajustes e melhorias

Arquivos: FrameHTML/RM.Imb.ImbControllerWebApi.dll

## 12.1.2602.155

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25421]** Processo de Negociação de boleto

Arquivos: RM.Imb.Shopping.Service.dll; RM.Imb.Shopping.Data.dll; RM.Imb.Aluguel.Facade.dll

### Rotina: PROPOSTA

* **[Ticket: 27339798 / DTCGI\_INTSYNC-3060]** Ajuste para aplicar "Desconto especial" em proposta (legado), com inclusão de novos componentes disponíveis em modalidade restringe

Arquivo: Imb/pvi

### Rotina: SISTEMA

* **[Ticket: 28074930 / DTCGI\_INTSYNC-3225]** [RM] - Ajuste no processo de conversão do Portal de Imóveis, o cenário esta ocorrendo devido a ordenação errada de colunas na tabela de Pessoa com XPIPessoa

Arquivo: RM.Imb.Integracao.Server.dll

## 12.1.2602.156

### Rotina: CONTRATO DE VENDA

* **[Ticket: TINPAD001-22526]** Melhoria no reajuste com fórmula global

Arquivos: RM.Imb.Venda.Contrato.Server.dll; RM.Imb.Menu.dll

## 12.1.2602.157

### Rotina: PROPOSTA

* **[Ticket: 27920160 / DTCGI\_INTSYNC-3153]** Ajuste ao avançar etapa cliente da proposta para validar estado civil casado de pessoas adicionais para manter compatibilidade com Proposta não migrada

Arquivo: Imb/portalgestaoimoveis

## 12.1.2602.158

### Rotina: Sem Rotina Específica

* **[Ticket: 28170445 / TINREV001-26459]** Foi realizado um ajuste no processo de geração de lançamentos de reembolso da funcionalidade “Parcela de Reembolso”. O sistema passa a considerar o locatário principal mesmo quando ele estiver inativo.

Arquivo: RM.Imb.ControleDespesa.Service.dll

## 12.1.2602.161

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: TINPAD001-22174]** remoção do menu de gerar movimento da reforma

Arquivo: RM.Imb.Menu.dll

### Rotina: TABELA DE PREÇOS

* **[Ticket: 27261561 / DTCGI\_INTSYNC-3182]** Ajuste sincronismo para evitar duplicidade de dados

Arquivo: Imb/pvi

## 12.1.2602.162

### Rotina: PESSOAS

* **[Ticket: 28104259 / DTCGI\_INTSYNC-3226]** Melhoria campos do cadastro do cliente/fornecedor do RM para levar para o Portal

Arquivo: Imb/portalgestaoimoveis

### Rotina: VENDA - DISTRATO

* **[Ticket: TINPAD001-22556]** melhoria no distrato para contabilizar na data atual quando o período contábil estiver fechado

Arquivos: RM.Imb.Venda.Calc.Calculos.Proc.Aditivos.dll; RM.Imb.Venda.IFacade.dll; RM.Imb.Venda.Facade.dll; RM.Imb.Venda.Calc.CalculosBase.dll; RM.Imb.Venda.Reajuste.Form.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

## 12.1.2602.163

### Rotina: FATURAMENTO DIARIO

* **[Ticket: 28483755 / TINREV001-26494]** Foi realizado um ajuste no Portal de Aluguel para permitir o lançamento do faturamento diário, desde que o usuário possua a permissão necessária para essa operação.Além disso, foram adicionados os menus “Documentos” e “Relatórios” no Portal do Lojista, proporcionando acesso mais rápido às informações e funcionalidades disponíveis.

Arquivos: RM.Imb.Menu.dll; RM.Imb.Cadastros.IServer.dll; RM.Imb.Cadastros.Server.dll

* **[Ticket: 28483755 / TINREV001-26494]** Foi realizado um ajuste no Portal de Aluguel para permitir o lançamento do faturamento diário, desde que o usuário possua a permissão necessária para essa operação.

Arquivo: Imb/portal-imobiliario

### Rotina: PROPOSTA - CONDIÇÕES DE PAGAMENTO

* **[Ticket: 28333382 / DTCGI\_INTSYNC-3289]** PI - Melhoria no cálculo da diferença a ser utilizado no acrescimo do item da regra quando existe desconto geral e modificação no valor total das regras, o que ocasiona diferença no total do plano.

Arquivos: RM.Imb.Integracao.Server.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

## 12.1.2602.164

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: TINPAD001-22174]** Melhoria no conversor de reajuste

Arquivos: RM.Imb.Venda.Financeiro.Form.dll; RM.Imb.Venda.Financeiro.Data.dll

## 12.1.2602.165

### Rotina: PROPOSTA - MINUTAS

* **[Ticket: 28169217 / DTCGI\_INTSYNC-3296]** [RM] - Ajuste ao imprimir minuta.

Arquivos: RM.Imb.Api.dll; RM.Imb.Venda.Regra.Data.dll; RM.Imb.Venda.Regra.Intf.dll

* **[Ticket: 28169217 / DTCGI\_INTSYNC-3296]** Ajuste ao imprimir minuta.

Arquivo: Imb/pvi

## 12.1.2602.166

### Rotina: CONTRATOS

* **[Ticket: DTCGI\_INTSYNC-2973]** Adicionando a opção de enviar para o TAE os documentos das unidades

Arquivo: Imb/pvi

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: TINPAD001-22174]** Melhoria no conversor de reajuste

Arquivos: RM.Imb.Venda.Contrato.Intf.dll; RM.Imb.Venda.Contrato.Form.dll; RM.Imb.Venda.Regra.Form.dll; RM.Imb.Menu.dll; RM.Imb.Venda.Resources.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll; RM.Imb.Venda.Contrato.Data.dll; RM.Imb.Conversor.Data.dll; RM.Imb.TotvsSign.Service.dll

## 12.1.2602.167

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25421]** Processo de Renegociação de Saldo de Boleto restante

Arquivos: RM.Imb.Shopping.Intf.dll; RM.Imb.Menu.dll; RM.Imb.Shopping.Service.dll; RM.Imb.Shopping.Data.dll; RM.Imb.Shopping.IService.dll; RM.Imb.Shopping.Form.dll

### Rotina: PESSOAS

* **[Ticket: DTCGI\_INTSYNC-2959]** Ajuste sessão ao salvar prospect

Arquivo: Imb/pvi

### Rotina: PROPOSTA - COMISSÃO

* **[Ticket: DTCGI\_INTSYNC-3380]** Ajuste na edição de comissão antiga

Arquivo: Imb/pvi

## 12.1.2602.168

### Rotina: Sem Rotina Específica

* **[Ticket: 28084835 / TINPAD001-22456]** Ajustes para exibir relatório de IR e Ficha Financeira para comprador desativado no PDC.

Arquivos: RM.Imb.Venda.Contrato.Server.dll; RM.Imb.Relatorio.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

* **[Ticket: 28084835 / TINPAD001-22456]** Ajustes ao obter contratos não estão sendo listados quando o parâmetro de limitar acesso de comprador estiver marcado.

Arquivos: FrameHTML/RM.Imb.ImbControllerWebApi.dll

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-25421]** Processo de Renegociação de Saldo de Boleto restante

Arquivos: RM.Imb.Shopping.Form.dll; RM.Imb.Shopping.Service.dll; RM.Imb.Shopping.Data.dll; RM.Imb.Shopping.Intf.dll; RM.Imb.Shopping.IService.dll

### Rotina: ITEM DE COBRANÇA

* **[Ticket: 27317998 / TINREV001-26268]** Foram adicionadas as colunas Coligada e Código do Cliente/Fornecedor nas visões de apuração de condomínio das funcionalidades Condomínio Individualizado e Fechamento por Competência.Nos processos “Gerar Lançamento Financeiro” das funcionalidades “Fechamento Individualizado” e “Fechamento por Competência”, ao utilizar os agrupamentos “Cliente/Fornecedor”, “Cliente/Fornecedor e Cálculo” ou “Cliente/Fornecedor e Item de Cobrança”, caso existam registros de um mesmo cliente/fornecedor vinculados a mais de um contrato de locação, os lançamentos financeiros serão gerados de forma individualizada para cada contrato.

Arquivos: RM.Imb.Cond.Fechamento.Data.dll; RM.Imb.Cond.Fechamento.Form.dll; RM.Imb.Cond.Fechamento.Intf.dll; RM.Imb.Cond.Fechamento.Service.dll

### Rotina: PROPOSTA - MINUTAS

* **[Ticket: 27163478 / DTCGI\_INTSYNC-3024]** PI - Melhoria para tratamento de imagens ui na impressão word para PDF de documentos Minutas e Propostas - Utilizar de Fontes que não existam registradas, instaladas no servidor onde esta a instalação do P

Arquivo: Imb/pvi

### Rotina: SINCRONIZAR

* **[Ticket: 28539025 / DTCGI\_INTSYNC-3361]** [RM] - Ajuste no sincronismo do portal de imóveis de "Empreendimentos" e "Componente x Modalidade" em base oracle

Arquivo: RM.Imb.Integracao.Server.dll

## 12.1.2602.170

### Rotina: MÓDULO DE COBRANÇA

* **[Ticket: DTCGI\_INTSYNC-3456]** Ajuste em exibição de mensagem de retorno no cancelamento de adiantamento de PIX na proposta

Arquivo: Imb/portalgestaoimoveis

### Rotina: PROPOSTA

* **[Ticket: 28134317 / DTCGI\_INTSYNC-3306]** [RM] - Ajuste no sincronismo de componente x modalidade

Arquivo: RM.Imb.Integracao.Server.dll

### Rotina: PROPOSTA - MINUTAS

* **[Ticket: 28169217 / DTCGI\_INTSYNC-3463]** [RM] - Ajuste na validação VPL da proposta para sincronizar corretamente a regra de modalidade da venda com a proposta. Cenário: O mesmo esta ocorrendo quando existem componentes na regra zerados por comissão do cliente

Arquivos: RM.Imb.Venda.Regra.Data.dll; RM.Imb.Venda.Contrato.Server.dll

* **[Ticket: 28169217 / DTCGI\_INTSYNC-3463]** Ajuste para ativação de minutas do empreendimento

Arquivo: Imb/pvi

### Rotina: SINCRONIZAR

* **[Ticket: 28539025 / DTCGI\_INTSYNC-3361]** [RM] - Ajuste no sincronismo do portal de imóveis quando a exclusão de sub-unidades

Arquivo: RM.Imb.Integracao.Server.dll

## 12.1.2602.171

### Rotina: Sem Rotina Específica

* **[Ticket: 28934360 / TINREV001-26557]** Foi realizado um ajuste no Portal Imobiliário para os casos em que o contrato de locação possui mais de um imóvel vinculado.

Arquivo: Imb/portal-imobiliario

### Rotina: PESSOAS

* **[Ticket: 28433997 / DTCGI\_INTSYNC-3321]** Ajuste na exclusão de Lead no portal de imóveis

Arquivo: Imb/pvi

### Rotina: REAJUSTE REVITALIZADO

* **[Ticket: 28362119 / TINPAD001-22537]** Ajuste no processo agendado de reajuste global de vendas.

Arquivo: RM.Imb.Venda.Reajuste.Data.dll

### Rotina: USO EXTERNO DE API / WEBSERVICE

* **[Ticket: TINPAD001-22659]** RD Marketing - Ajuste de chamada de API informando o tenantId para provisionamento automatico do iPaaS

Arquivos: RM.Imb.RDStation.Marketing.SmartLink.Intf.dll; RM.Imb.RDStation.Marketing.SmartLink.Server.dll

* **[Ticket: TINPAD001-22676]** melhoria no distrato para contabilizar na data atual quando o período contábil estiver fechado

Arquivo: RM.Imb.Menu.dll

## 12.1.2602.173

### Rotina: ALUGUEL - PDC

* **[Ticket: TINREV001-26570]** Foi realizado um ajuste no Portal Imobiliário para validar as permissões de acesso às funcionalidades de Atendimento, Segunda Via de Boleto, Financeiro, Documentos e Relatórios. A partir dessa alteração, os menus sem permissão não serão exibidos e o acesso às funcionalidades será permitido somente aos usuários que possuírem as respectivas permissões configuradas em seu perfil.

Arquivos: RM.Imb.Cadastros.IServer.dll; RM.Imb.Cadastros.Server.dll

* **[Ticket: TINREV001-26570]** Foi realizado um ajuste no Portal Imobiliário para validar as permissões de acesso às funcionalidades de Atendimento, Segunda Via de Boleto, Financeiro, Documentos e Relatórios.

Arquivo: Imb/portal-imobiliario

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-26536]** Processo de Renegociação de Saldo de Boleto

Arquivo: RM.Imb.Shopping.Service.dll

* **[Ticket: TINREV001-26584]** Processo de Renegociação de Saldo de Boleto

Arquivos: RM.Imb.Shopping.Service.dll; RM.Imb.Shopping.Form.dll

### Rotina: VENDA - DISTRATO

* **[Ticket: 28495000 / TINPAD001-22565]** melhoria no distrato para contabilizar na data atual quando o período contábil estiver fechado

Arquivos: RM.Imb.Cobranca.Server.dll; RM.Imb.Venda.Calc.CalculosBase.Intf.dll; RM.Imb.Parametros.Form.dll; RM.Imb.Parametros.Intf.dll; RM.Imb.Parametros.Data.dll; RM.Imb.Venda.Calc.Calculos.Proc.dll

## 12.1.2602.174

### Rotina: FINANCEIRO - LANÇAMENTOS - COBRANÇA PARTILHADA

* **[Ticket: TINREV001-26580]** Processo de Renegociação de Saldo de Boleto

Arquivo: RM.Imb.Shopping.Service.dll

### Rotina: USO EXTERNO DE API / WEBSERVICE

* **[Ticket: TINPAD001-22659]** RD Marketing - Ajuste no parametro do conversor de integração

Arquivo: RM.Imb.RDStation.Marketing.SmartLink.Server.dll

### Rotina: VENDA - PDC

* **[Ticket: TINPAD001-22600]** ocultar botão Alterar Empreendimento em paginas com campo próprio

Arquivo: Imb/portalcliente

## 12.1.2602.175

### Rotina: VENDA - DISTRATO

* **[Ticket: 28683784 / TINPAD001-22591]** Melhoria no processo de baixa do financeiro para identificar o tipo de baixa e uma fórmula pra identificar a origem do processo que chamou a fórmulaNova Função de Fórmula pra identificar a origem do processo do Liquido que chamou a fórmulaMelhoria no processo da apuração de competência para não chamar a validação da competência quando for baixa de borderô

Arquivos: RM.Imb.Aluguel.ConfissaoDivida.Service.dll; RM.Imb.Financeiro.Server.dll; RM.Imb.Venda.Financeiro.IServer.dll; RM.Imb.Aluguel.ConfissaoDivida.IService.dll; RM.Imb.Venda.Financeiro.Server.dll; RM.Imb.Financeiro.IServer.dll

# TOTVS Manutenção

## 12.1.2602.100

### Rotina: ORDEM DE SERVIÇO

* **[Ticket: TOPORCAPLAN001-29654]** Teste Sistemico - Manutenção de Equipamentos

Arquivos: RM.Mnt.PlanoManut.Data.dll; RM.Mnt.ObjOficina.Data.dll; RM.Mnt.ObjOficina.Form.dll; RM.Mnt.OrdemServico.Form.dll

## 12.1.2602.102

### Rotina: ORDEM DE SERVIÇO

* **[Ticket: TOPORCAPLAN001-29654]** Excluir uma OS já cancelada melhoria

Arquivos: RM.Mnt.ObjOficina.Form.dll; RM.Mnt.OrdemServico.Form.dll; RM.Mnt.ObjOficina.Data.dll

## 12.1.2602.104

### Rotina: ORDEM DE SERVIÇO

* **[Ticket: TOPORCAPLAN001-29654]** Excluir uma OS já cancelada melhoria

Arquivo: RM.Mnt.OrdemServico.Form.dll

## 12.1.2602.106

### Rotina: ORDEM DE SERVIÇO

* **[Ticket: TOPORCAPLAN001-29654]** Excluir uma OS já cancelada melhoria

Arquivo: RM.Mnt.OrdemServico.Form.dll

## 12.1.2602.111

### Rotina: OBJETO DE MANUTENÇÃO

* **[Ticket: 26432741 / TOPORCAPLAN001-29699]** Ajuste na validação de datas ao associar Patrimonio ao Objeto de Manutenção.

Arquivos: RM.Mnt.Utils.Intf.dll; RM.Mnt.ObjOficina.Service.dll; RM.Mnt.ObjOficina.Data.dll

## 12.1.2602.114

### Rotina: OBJETO DE MANUTENÇÃO

* **[Ticket: 26736930 / TOPORCAPLAN001-29809]** Manutenção de Equipamentos - excluir plano de manutenção

Arquivo: RM.Mnt.PlanoManut.Data.dll

## 12.1.2602.130

### Rotina: OBJETO DE MANUTENÇÃO

* **[Ticket: 27157610 / TOPORCAPLAN001-30026]** Produto não disponível no Processo de Apropriação Direta de Produto(s)

Arquivos: RM.Mnt.ApropriacaoDireta.Form.dll; RM.Mnt.OrdemServico.Form.dll

## 12.1.2602.144

### Rotina: OBJETO DE MANUTENÇÃO

* **[Ticket: 27466184 / TOPORCAPLAN001-30214]** Base de homologação - Objeto de manutenção

Arquivo: RM.Mnt.ObjOficina.Form.dll

## 12.1.2602.152

### Rotina: OBJETO DE MANUTENÇÃO

* **[Ticket: 27724372 / TOPORCAPLAN001-30337]** Filtro no filtro de inicialização de Planos de Manutenção

Arquivo: RM.Mnt.PlanoManut.Data.dll

## 12.1.2602.153

### Rotina: ORDEM DE SERVIÇO

* **[Ticket: 27362259 / TOPORCAPLAN001-30378]** informar o Calculo de Horas com base em mão de obra

Arquivos: RM.Mnt.Cadastros.Intf.dll; RM.Mnt.Cadastros.Data.dll; RM.Mnt.OrdemServico.Data.dll; RM.Mnt.PlanoManut.Data.dll

## 12.1.2602.166

### Rotina: ORDEM DE SERVIÇO

* **[Ticket: 27724436 / TOPORCAPLAN001-30547]** Visualização de Preventivas canceladas no "Vencimento de Planos(s) de Manutenção".

Arquivo: RM.Mnt.PlanoManut.Data.dll

## 12.1.2602.175

### Rotina: OBJETO DE MANUTENÇÃO

* **[Ticket: 28049753 / TOPORCAPLAN001-30652]** Obras e projetos - manutenção - OS integração com patrimônio.

Arquivos: RM.Mnt.ObjOficina.Service.dll; RM.Mnt.ApropriacaoDireta.Form.dll

# TOTVS Planejamento e Controle da Produção

## 12.1.2602.100

### Rotina: CONTRATO DE VENDA

* **[Ticket: DFRWFOUNDATION-29232]** Implementando Interface IRMSDataServer

Arquivo: RM.PCP.ItemOrdem.Service.dll

## 12.1.2602.137

### Rotina: PROCESSO PRODUTIVO SIMPLES

* **[Ticket: DRMMATERIAIS-8510]** Ajuste na classificação de componentes ao faturar movimento de estrutura

Arquivos: RM.PCP.Estruturas.Intf.dll; RM.PCP.Estruturas.Data.dll

# TOTVS Processo Seletivo

## 12.1.2602.100

### Rotina: GESTÃO DE ESTOQUE, COMPRAS E FATURAMENTO

* **[Ticket: 26395150 / DEDUPACMEN-8421]** Otimização no processo de geração de movimento para a taxa de inscrição os dados município e estado do serviço ficam inconsistentes quando a tributação do item para o ISS está configurado para procurar alíquota diferente de município.

Arquivo: RM.EduPS.Facade.Server.dll

### Rotina: MATRÍCULA VIA VENDA ONLINE DE CURSOS

* **[Ticket: DEDUCAPCOM-9703]** "Implementada a restrição de exibição do itinerário formativo para processos seletivos da modalidade Venda Online

Arquivo: RM.EduPS.Cadastros.Form.dll

### Rotina: MATRICULAR PROCESSO SELETIVO RM

* **[Ticket: 26216786 / DEDUCAPCOM-10067]** Ajustes: Dados do aluno não estavam sendo sobreescritos durantes a matricula

Arquivo: RM.EduPS.Cadastros.Server.dll

## 12.1.2602.101

### Rotina: ENVIO DE MENSAGENS

* **[Ticket: DEDUCAPCOM-10173]** Ajustes: Dados do aluno não estavam sendo sobreescritos durantes a matricula 2602(adicionando comentario) \_2

Arquivo: RM.EduPS.Cadastros.Server.dll

### Rotina: MATRICULAR PROCESSO SELETIVO RM

* **[Ticket: 26181695 / DEDUCAPCOM-10121]** Ajuste na validação de candidato estrangeiro para validar o preenchimento do passaporte

Arquivo: RM.EduPS.Cadastros.Server.dll

## 12.1.2602.105

### Rotina: GERAÇÃO DE MOVIMENTO

* **[Ticket: DEDUPACMEN-8431]** Ajuste código indicador da operação para reforma tributária

Arquivos: RM.EduPS.Lib.Intf.dll; RM.EduPS.Processos.Data.dll

## 12.1.2602.106

### Rotina: PROCESSOS DE APURAÇÃO - CHAMADA DE CANDIDATO APROVADO

* **[Ticket: 26605889 / DEDUCAPCOM-10175]** Ajustes nos nomes do processo de importar notas do enem

Arquivo: RM.EduPS.Processos.Form.dll

## 12.1.2602.107

### Rotina: ANEXOS - AREA DE INTERESSE OFERTADA

* **[Ticket: DEDUCAPCOM-10025]** Atuação em débito técnico interno

Arquivo: RM.EduPS.dll

## 12.1.2602.116

### Rotina: PAGAMENTO COM CARTÃO

* **[Ticket: 26552263 / DEDUPACMEN-8540]** Ajustes apis portal do processo seletivo

Arquivo: RM.EduPS.API.dll

### Rotina: PARÂMETROS DO SISTEMA

* **[Ticket: 26302532 / DEDUCAPCOM-10282]** Ajustes: Data de nascimento do responsavel retrocedendo um dia 2506

Arquivo: RM.EduPS.Cadastros.Server.dll

## 12.1.2602.117

### Rotina: INSCRIÇÃO DE CANDIDATO

* **[Ticket: 26074958 / DEDUCAPCOM-10275]** Ajuste no processo seletivo para validar se existem candidatos diferentes com mesmo CPF no processo seletivo.

Arquivo: RM.EduPS.Inscricoes.Server.dll

## 12.1.2602.120

### Rotina: SOLICITAÇÃO DE ESPECÍFICO - FÁBRICA

* **[Ticket: 26986807 / DEDUCAPCOM-10340]** Ajustaremos o sistema para omitir informações sensíveis do banco de dados em casos que as APIs apresentem mensagens de não conformidades não tratadas

Arquivo: RM.EduPS.Rest.Server.dll

## 12.1.2602.123

### Rotina: SOLICITAÇÃO DE ESPECÍFICO - FÁBRICA

* **[Ticket: 26986807 / DEDUCAPCOM-10340]** Feito ajuste no tratamento de exceção para exibir mensagem de validação no login.

Arquivo: RM.EduPS.Rest.Server.dll

## 12.1.2602.125

### Rotina: ALTERAR DADOS PESSOAIS

* **[Ticket: DEDUCAPCOM-10371]** Ajustes para esconder processos relacionados a movimento (nota fiscal) no processo seletivo

Arquivos: RM.EduPS.Inscricoes.Form.dll; RM.EduPS.Cadastros.Form.dll

## 12.1.2602.131

### Rotina: UPLOAD DE DOCUMENTOS/ARQUIVOS

* **[Ticket: DEDUCAPCOM-10407]** Ajustes de segurança

Arquivos: RM.EduPS.Cadastros.Server.dll; RM.EduPS.Rest.Server.dll

## 12.1.2602.132

### Rotina: ASSOCIAÇÃO DE BOLSA

* **[Ticket: 27274418 / DEDUCAPCOM-10443]** Ajuste para permitir alterar a aplicação da bolsa no concurso de bolsas

Arquivo: RM.EduPS.Cadastros.Data.dll

## 12.1.2602.136

### Rotina: INSCRIÇÕES

* **[Ticket: DEDUCAPCOM-10408]** Ajustes de segurança

Arquivos: FrameHTML/RM.EduPS.WebAPI.dll

### Rotina: PROCESSOS - GERAÇÃO DE MOVIMENTO

* **[Ticket: 27388499 / DEDUCAPCOM-10483]** Ajustes para voltar com a opção de geração de movimento

Arquivos: RM.EduPS.Cadastros.Form.dll; RM.EduPS.Inscricoes.Form.dll

## 12.1.2602.137

### Rotina: INSCRIÇÃO

* **[Ticket: 27334892 / DEDUCAPCOM-10470]** Ajuste na validação de mensgens de retorno na inscrição do portal do Processo Seletivo.

Arquivo: RM.EduPS.Rest.Server.dll

## 12.1.2602.141

### Rotina: NFS-E - CONSULTA AUTORIZAÇÃO/CANCELAMENTO

* **[Ticket: 27631535 / DEDUPACMEN-8734]** Otimização no processo de geração de movimento por caixa, por competência e para a taxa de inscrição do candidato os dados do destinatário do consumidor do serviço quando o aluno/candidato e o responsável financeiro são as mesmas pessoas.

Arquivo: RM.EduPS.Facade.Server.dll

## 12.1.2602.143

### Rotina: GESTÃO DE ESTOQUE, COMPRAS E FATURAMENTO

* **[Ticket: 27673218 / DEDUPACMEN-8752]** Otimização no processo de geração de movimento para a taxa de inscrição do candidato quando na sua inscrição em 2 ou mais áreas de interesse gerar somente um movimento.

Arquivo: RM.EduPS.Processos.Data.dll

## 12.1.2602.147

### Rotina: PAGAMENTO COM CARTÃO

* **[Ticket: 27890076 / DEDUPACMEN-8782]** Ajuste validação usuário api do resumo de pagamento PIX

Arquivos: FrameHTML/RM.EduPS.WebAPI.dll

## 12.1.2602.161

### Rotina: GERAÇÃO DE LANÇAMENTOS

* **[Ticket: DEDUPACMEN-8556]** Otimização no processo de movimentações financeiras das disciplinas para a geração de lançamento

Arquivos: RM.EduPS.dll; RM.EduPS.Facade.Intf.dll; RM.EduPS.Facade.Server.dll

## 12.1.2602.165

### Rotina: INSCRIÇÕES

* **[Ticket: DEDUCAPCOM-10409]** Ajustes para validações da integridade dos dados portal do processo seletivo

Arquivos: FrameHTML/RM.EduPS.WebAPI.dll

## 12.1.2602.168

### Rotina: MATRÍCULA VIA CENTRAL DO CANDIDATO

* **[Ticket: DEDUCAPCOM-10410]** Adequação de segurança - API Processo Seletivo - Matrícula e Central do Candidato

Arquivos: FrameHTML/RM.EduPS.WebAPI.dll

## 12.1.2602.173

### Rotina: ANEXOS - AREA DE INTERESSE OFERTADA

* **[Ticket: 27646209 / DEDUCAPCOM-10542]** Ajuste na identificação de PS de venda on line na área ofertada

Arquivo: RM.EduPS.Cadastros.Data.dll

# TOTVS Segurança e Medicina do Trabalho

## 12.1.2602.110

### Rotina: CAT - OCORRÊNCIAS DE ACIDENTE DE TRABALHO

* **[Ticket: DRHSSTPT-1251]** Adequações do CNPJ alfanumérico para o processo trabalhista smartview

Arquivos: RM.Smt.Utils.Intf.dll; RM.Smt.Utils.Server.dll; RM.Smt.Cadastros.Form.dll

## 12.1.2602.112

### Rotina: CAT - OCORRÊNCIAS DE ACIDENTE DE TRABALHO

* **[Ticket: DRHSSTPT-1251]** Ajuste CNPJ alfanumérico emitente CAT

Arquivos: RM.Smt.Cadastros.Form.dll; RM.Smt.Cadastros.Data.dll

## 12.1.2602.113

### Rotina: CAT - OCORRÊNCIAS DE ACIDENTE DE TRABALHO

* **[Ticket: DRHSSTPT-1251]** Ajuste CNPJ alfanumérico emitente CAT

Arquivo: RM.Smt.Cadastros.Form.dll

## 12.1.2602.114

### Rotina: CAT - OCORRÊNCIAS DE ACIDENTE DE TRABALHO

* **[Ticket: DRHSSTPT-1251]** Ajuste CNPJ alfanumérico emitente CAT

Arquivo: RM.Smt.Utils.Server.dll

## 12.1.2602.124

### Rotina: EXAMES

* **[Ticket: 26886919 / DRHSSTPT-1905]** Ajustes na vinculação do exame audiométrico.

Arquivos: RM.Smt.Parametros.Data.dll; RM.Smt.Parametros.Form.dll

## 12.1.2602.130

### Rotina: CARGOS

* **[Ticket: 24548396 / DRHSSTPT-1196]** Disponibilização do campo Registro de Qualificação de Especialista no cadastro do Profissional da Saúde

Arquivos: RM.Smt.Cadastros.Data.dll; RM.Smt.Cadastros.Intf.dll; RM.Smt.Cadastros.Form.dll

## 12.1.2602.131

### Rotina: EVENTO S-2240

* **[Ticket: 26975739 / DRHSSTPT-1949]** Ajuste na análise e obtenção das avaliações de risco para o evento S-2240.

Arquivo: RM.Smt.Cadastros.Data.dll

## 12.1.2602.132

### Rotina: EVENTO S-2240

* **[Ticket: 26588788 / DRHSSTPT-1875]** Ajuste na análise e obtenção das avaliações de risco para o evento S-2240.

Arquivo: RM.Smt.Cadastros.Data.dll

## 12.1.2602.133

### Rotina: ATESTADOS

* **[Ticket: 27154962 / DRHSSTPT-1997]** Ajuste na persistência de atualização de atestados oriundos de acionamento via webService.

Arquivo: RM.Smt.Pessoa.Data.dll

## 12.1.2602.134

### Rotina: CAT - OCORRÊNCIAS DE ACIDENTE DE TRABALHO

* **[Ticket: 27292863 / DRHSSTPT-2058]** Ajuste na validação do número de inscrição do local do acidente da CAT.

Arquivo: RM.Smt.Cadastros.Form.dll

## 12.1.2602.135

### Rotina: CAT - OCORRÊNCIAS DE ACIDENTE DE TRABALHO

* **[Ticket: 27309701 / DRHSSTPT-2045]** Ajuste na validação do número de inscrição do local do acidente da CAT.

Arquivo: RM.Smt.Cadastros.Form.dll

## 12.1.2602.142

### Rotina: PRÉ-ATESTADO

* **[Ticket: 26980753 / DRHSSTPT-1935]** Correção em campo de Status de Aprovação do Pré-Atestado para aplicar Auto Filtro e Ordenação pelo campo

Arquivos: RM.Smt.Pessoa.Data.dll; RM.Smt.Pessoa.Intf.dll

## 12.1.2602.144

### Rotina: APURAR E FINALIZAR ELEIÇÃO

* **[Ticket: 26646314 / DRHSSTPT-1778]** Ajuste para que a apuração da eleição da CIPA com fórmula visual seja executada.

Arquivo: RM.Smt.Cipa.Intf.dll

## 12.1.2602.145

### Rotina: WEBSERVICE E DATASERVICE

* **[Ticket: 27475609 / DRHSSTPT-2140]** Ajuste no dataserver da cat para acionamento via api WorkAccidentOccurrence

Arquivo: RM.Smt.Cadastros.Data.dll

## 12.1.2602.152

### Rotina: ATESTADOS

* **[Ticket: 28239534 / DRHSSTPT-2213]** Correção em query de persistência de Atestado para executar em Oracle

Arquivo: RM.Smt.Pessoa.Data.dll

### Rotina: WEBSERVICE E DATASERVICE

* **[Ticket: 27992921 / DRHSSTPT-2216]** Correção em query de persistência de Atestado para executar em Oracle

Arquivo: RM.Smt.Pessoa.Data.dll

## 12.1.2602.157

### Rotina: QUIRONS

* **[Ticket: DRHSSTPT-1748]** Ajuste para acesso a API hazardmeasurement.

Arquivo: RM.Smt.Cadastros.Data.dll

## 12.1.2602.158

### Rotina: ASSISTENTE DE AGENDAMENTO AUTOMÁTICO

* **[Ticket: 27297488 / DRHSSTPT-2043]** Melhoria no agendamento de exames para não marcar exames no mesmo horário

Arquivos: RM.Smt.Clinico.Intf.dll; RM.Smt.Clinico.Data.dll; RM.Smt.Clinico.Form.dll

## 12.1.2602.168

### Rotina: ATESTADOS

* **[Ticket: DRHSSTPT-2317]** Ajuste na API sickNote a fim de aplicar ajustes de segurança de acesso.

Arquivo: RM.Smt.Api.dll

## 12.1.2602.170

### Rotina: ATESTADOS

* **[Ticket: 28873139 / DRHSSTPT-2314]** Ajuste no dataserver de Atestado para a correta persistência das informações de auditoria.

Arquivo: RM.Smt.Pessoa.Data.dll

* **[Ticket: 28874839 / DRHSSTPT-2315]** Melhoria na persistência de Atestado via Soap

Arquivo: RM.Smt.Pessoa.Data.dll

## 12.1.2602.174

### Rotina: FONTES GERADORAS

* **[Ticket: 27192804 / DRHSSTPT-2059]** Ajuste no PPP para a não impressão de riscos ergonômicos e mecânicos

Arquivo: RM.Smt.Relatorio.Data.dll
