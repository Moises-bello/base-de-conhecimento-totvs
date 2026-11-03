---
article_id: 360024677334
category: Avaliação e Pesquisa de Desempenho (SIGAAPD)
content_hash: 99f90e7148fbf98b77cd87dcc936b000669eed575a21b9e24a2422d982523b9a
fetched_at: '2026-06-28T22:42:53.774209+00:00'
product: protheus
section_id: 206956088
source: central-protheus
title: RH - Linha Protheus - APD - Como conferir relacionamento do funcionário com
  o participante
type: support-article
updated_at: '2026-06-26T14:24:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024677334-RH-Linha-Protheus-APD-Como-conferir-relacionamento-do-funcion%C3%A1rio-com-o-participante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41516543349143)Tempo aproximado para leitura:**00:05:00** min  
  
**Dúvida**  
Como conferir relacionamento do funcionário com o participante?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Avaliação e Pesquisa de Desempenho – Todas as versões  
  
**Solução**  
As rotinas utilizadas para o relacionamento são:  
  
- **Cadastro de funcionários** (*SRA*), no módulo SIGAGPE acesse a rotina Atualizações > Funcionários > Funcionários;  
- **Cadastro de Participantes** (*RD0*), no módulo SIGAAPD acesse a rotina Atualizações > Participantes > Cadastro;  
- **Relacionamento Funcionários X Participantes** (*RDZ*), essa tabela é interna do sistema.  
  
Para acesso ao App Meu RH, é obrigatório os registros como **Funcionário, ou Autônomo, na tabela SRA**, assim como **Cadastro de Participantes - tabela RD0.**  
  
Caso a pessoa tenha somente o cadastro de participante e, não seja um funcionário da Empresa, **não irá conseguir utilizar o App Meu RH.**  
  
A consulta pode ser realizada no modulo através da rotina Consulta - Cadastro - Genéricos  
  
**1.**  Pesquisa pela tabela SRA, exporte o arquivo CSV ou confira em tela se preferir.  
Na tabela SRA, faça um filtro pelo CPF **(RA\_CIC)** do funcionário. O filtro deve ser realizado pelo CPF para avaliarmos se existe mais de um registro.  
Guarde a numeração da matricula do funcionário e avalie se existe mais de um registro com esse mesmo CPF (transferido, demitido, etc).   
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9826541143319)  
  
A consulta pode ser realizada no modulo através da rotina Consulta - Cadastro - Genéricos  
  
**2.**  Pesquisa pela tabela RD0, exporte o arquivo CSV ou confira em tela se preferir.  
Na tabela RD0, faça um filtro pelo CPF **(RD0\_CIC)** do funcionário. O filtro deve ser realizado pelo CPF para avaliarmos se existe mais de um registro. Guarde o código do participante**(RD0\_CODIGO)**.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9826595098647)  
  
A consulta pode ser realizada no modulo através da rotina Consulta - Cadastro - Genéricos  
  
**3.**  Pesquisa pela tabela RDZ,  exporte o arquivo CSV ou confira em tela se preferir.  
Na tabela RDZ, faça um filtro pelo "código" do participante **(RDZ\_CODRD0).** Ao localizar o registro analise o campo RDZ\_CODENT **(correspondente a "filial+matrícula" do funcionário).**  
  
Em meu exemplo Filial 0001 + Matricula 000001 o campo Código esta correto 0001000001.  
Em seu ambiente deve avaliar se o campo (RDZ\_CODENT) está apontando corretamente para o código da filial e matricula do funcionário.  
  
**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9826613931543)**  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[**Como relacionar os Participantes**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255013-MP-MEU-RH-Como-relacionar-os-Participantes?source=search)  
[**Trabalhadores com mais de um Vínculo/Cadastro (mesmo CPF) no módulo "07 - SIGAGPE"**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043733314)  
[**Artigos sobre Avaliação Pesquisa e Desempenho**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206956088-RH-Avalia%C3%A7%C3%A3o-e-Pesquisa-de-Desempenho)
