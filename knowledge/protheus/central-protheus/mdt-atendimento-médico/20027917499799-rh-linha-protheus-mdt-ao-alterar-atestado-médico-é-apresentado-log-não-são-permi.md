---
article_id: 20027917499799
category: MDT - Atendimento Médico
content_hash: 6ce9797274c0045272363ada1ec97bb53e20265d73a8b7328789343c86ea630b
fetched_at: '2026-06-28T22:44:20.501389+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Ao alterar Atestado Médico é apresentado log "Não
  são permitidos períodos anteriores ao dia xx/xx/xxxx"
type: support-article
updated_at: '2025-09-02T17:19:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20027917499799-RH-Linha-Protheus-MDT-Ao-alterar-Atestado-M%C3%A9dico-%C3%A9-apresentado-log-N%C3%A3o-s%C3%A3o-permitidos-per%C3%ADodos-anteriores-ao-dia-xx-xx-xxxx
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20027917471255) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao alterar Atestado Médico, é apresentado log: AJUDA:PN230INCON- "Não são permitidos períodos anteriores ao dia xx/xx/xxxx".  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20027944302103)  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**

Este log ocorre porque, no momento da inclusão do atestado médico (**Atualizações > Atendimento Médico > Atestado Médico**), o parâmetro **MV\_NG2IPON** estava desabilitado (valor **2 – Não**), permitindo o lançamento apenas da data de início do afastamento.

Possivelmente, após a inclusão do registro, o parâmetro foi habilitado (alterado para **1 – Sim**), o que ativa a validação completa do atestado, tornando obrigatória a informação de **início e fim** do afastamento.

Caso essas informações não estejam preenchidas, o sistema apresenta o log mencionado neste artigo.

**Solução**

Para que seja possível realizar a alteração, é necessário desabilitar o parâmetro **MV\_NG2IPON**, definindo-o como **2 – Não**. Dessa forma, o sistema permitirá informar apenas a **data fim** do atestado.

No entanto, caso o usuário deseje utilizar a **integração entre o MDT e o PONTO**, o parâmetro deve permanecer habilitado (**1 – Sim**), tornando obrigatória a informação das **datas de início e fim** do afastamento.

**Importante**: A integração entre os módulos MDT e PON tem objetivo de abonar apenas algumas horas, ou no máximo 1 (um) dia. Para atestado superior a isto, deve ser utilizado apenas o preenchimento e integração do GPE (aba Afastamentos), pois o funcionário estará afastado e não precisará do abono no ponto eletrônico quando estiver afastado por motivos de saúde.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056829034519)  
  
Para localizar o parâmetro **MV\_NG2IPON**, acesse o módulo Configurador no menu Ambiente - Cadastro - Parâmetro, e efetue a pesquisa:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20056829038871)  
  
Consulte documentações relacionados:  
[Integração do Atestado Médico com o Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025162074-MP-MDT-Integra%C3%A7%C3%A3o-do-Atestado-M%C3%A9dico-com-o-Ponto-Eletr%C3%B4nico)  
[Como lançar Atestado Médico integrado com Gestão de Pessoal](Como%20lan%C3%A7ar%20Atestado%20M%C3%A9dico%20integrado%20com%20Gest%C3%A3o%20de%20Pessoal)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
