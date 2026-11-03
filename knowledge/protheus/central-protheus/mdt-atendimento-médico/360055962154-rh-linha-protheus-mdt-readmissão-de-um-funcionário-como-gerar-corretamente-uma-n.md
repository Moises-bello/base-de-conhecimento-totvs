---
article_id: 360055962154
category: MDT - Atendimento Médico
content_hash: 8b1c047fa8df538feb71146c6fcac958890ff40c323aba8776706849229edc9d
fetched_at: '2026-06-28T22:44:21.559619+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Readmissão de um funcionário como gerar corretamente
  uma nova ficha médica a nova matricula readmitida
type: support-article
updated_at: '2025-09-02T17:21:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055962154-RH-Linha-Protheus-MDT-Readmiss%C3%A3o-de-um-funcion%C3%A1rio-como-gerar-corretamente-uma-nova-ficha-m%C3%A9dica-a-nova-matricula-readmitida
---

**Dúvida**Em casos de  readmissão (recontratação ou contratação de um ex funcionário), como gerar corretamente uma nova ficha médica a nova matricula?  
Entenda como preencher a pergunta em seu cadastro: "Existe uma ficha médica para o funcionário com o mesmo número de CPF, inscrito na matricula XXXXXX, deseja alterar o relacionamento?"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões

**Solução**Todos os funcionários cadastrados na tabela **SRA** **(Cadastro de Funcionários)**, quando desligados da empresa ( com rescisão calculada) , ficam, automaticamente, bloqueados para uso em processamentos nas demais rotinas. Este controle é realizado pelo campo **(RA\_MSBLQL)**. Automaticamente a ficha Medica desta matricula estará bloqueada , ao termino do calculo da rescisão. Conforme imagem abaixo.  
  
![ficha_medica_bloqueada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360094938174)  
  
Em alguns casos existe uma readmissão desta matricula.  
Este processo é muito comum nas empresa, objetivo deste artigo é orientar como proceder em casos do tipo para gerar corretamente uma **nova ficha médica** a esta **nova matricula**.  
  
Ao realizar o cadastro do Funcionário readmitido o sistema irá validar o CPF e por já existir em sua base será apresentado a seguinte mensagem: " Existe uma ficha médica para o funcionário com o mesmo número de CPF, inscrito na matricula XXXXXX, deseja alterar o relacionamento?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097248533)  
  
Clicando em "**Não"** será criado uma nova matricula ao CPF readmitido.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094946134)  
  
E será criado uma nova ficha médica ao CPF readmitido.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094946234)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](%20%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)  
[MP - MDT - Inclusão automática de ficha médica ao realizar admissão do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028379252)
