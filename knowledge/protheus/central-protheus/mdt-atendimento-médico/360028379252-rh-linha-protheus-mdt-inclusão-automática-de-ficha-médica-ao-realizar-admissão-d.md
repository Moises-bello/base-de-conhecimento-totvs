---
article_id: 360028379252
category: MDT - Atendimento Médico
content_hash: 431f860bcad34b772465642267f2a0cf26677ea5402b24e5323ff077f28ddc0a
fetched_at: '2026-06-28T22:44:21.343851+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Inclusão automática de ficha médica ao realizar
  admissão do funcionário
type: support-article
updated_at: '2025-08-14T19:11:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028379252-RH-Linha-Protheus-MDT-Inclus%C3%A3o-autom%C3%A1tica-de-ficha-m%C3%A9dica-ao-realizar-admiss%C3%A3o-do-funcion%C3%A1rio
---

**Dúvida**Como efetuar inclusão automática de ficha médica ao realizar admissão do funcionário?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**No módulo Configurador, acesse o menu **Ambiente > Cadastros > Parâmetros** e filtre o parâmetro **MV\_NG2FICH**.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065466394)  
  
Ao deixar o parâmetro habilitado (1), e incluir funcionário no módulo SIGAGPE ***(*****Atualizações > Funcionários > Funcionários)**, ao finalizar o cadastro o registro é incluído automaticamente na Ficha Médica no módulo SIGAMDT **(Atualizações > Atendimento Médico > Ficha Médica).**  
  
**Observação:** É necessário preencher o CPF no cadastro do funcionário.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066480113)

OBS: O parâmetro de integração entre Medicina e Gestão de Pessoal deve estar ativo também **MV\_MDTGPE.**

Com o conteúdo do parâmetro MV\_NG2FICH igual a 1 (Sim), cadastrar um funcionário aciona a rotina de ficha médica conforme os cenários descritos logo abaixo:

**Cenário 1**

Ao cadastrar um funcionário pela rotina de Funcionários que nunca possuiu uma ficha médica, será criado uma nova ficha médica automaticamente.

**Cenário 2**

Ao cadastrar um funcionário pela rotina de Funcionários que já possuiu uma ficha médica, será realizado o questionamento ao usuário, se deseja criar uma nova ficha médica ou verificar se é possível utilizar a ficha médica já existente.

**Cenário 3**

Ao cadastrar um funcionário pelo ExecAuto que nunca possuiu uma ficha médica, será criado uma nova ficha médica automaticamente.

**Cenário 4**

Ao cadastrar um funcionário pelo ExecAuto que já possuiu uma ficha médica, será verificado se é possível utilizar a ficha médica já existente.  
  
O padrão do sistema é utilizar a ficha médica já existente para o funcionário em questão, convertendo as tarefas de candidato em tarefas de funcionário caso existam. No entanto, somente é possível a utilização de uma ficha médica já existente caso a mesma não tenha sido utilizada em cadastros importantes do sistema, caso contrário a ficha médica não será atualizada com as novas informações do cadastro do funcionário e não será criado uma nova ficha médica automaticamente.  
  
Confira também: [RH - Linha Protheus - MDT - Readmissão de um funcionário como gerar corretamente uma nova ficha médica a nova matricula readmitida](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055962154-RH-Linha-Protheus-MDT-Readmiss%C3%A3o-de-um-funcion%C3%A1rio-como-gerar-corretamente-uma-nova-ficha-m%C3%A9dica-a-nova-matricula-readmitida)

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Central de Artigos MDT eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
