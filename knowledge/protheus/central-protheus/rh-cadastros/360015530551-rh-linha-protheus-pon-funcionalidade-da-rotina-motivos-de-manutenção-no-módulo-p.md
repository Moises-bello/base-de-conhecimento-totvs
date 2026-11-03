---
article_id: 360015530551
category: RH - Cadastros
content_hash: 061dab56336b953291c572891fcd04d9af1fef9fb5ea7949b3b461c001aba74f
fetched_at: '2026-06-28T22:44:52.997319+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Funcionalidade da rotina Motivos de Manutenção
  no Módulo Ponto Eletrônico
type: support-article
updated_at: '2026-06-09T21:25:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015530551-RH-Linha-Protheus-PON-Funcionalidade-da-rotina-Motivos-de-Manuten%C3%A7%C3%A3o-no-M%C3%B3dulo-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34988490336151) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Qual a funcionalidade da rotina **Motivos de Manutenção** no Módulo Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O Motivo de manutenção: **Atualizações - Cadastro do Ponto - Motivos Manutenção,** tem a **função de classificar o tipo da marcação** no momento da leitura e após a leitura quando é feita a manutenção. Isso porque, com a portaria 1510, a geração do arquivo magnético AFDT - Arquivo Fonte de Dados Tratados ou Portaria 671, arquivo AEJ - Arquivo Eletrônico de Jornada, tem que levar em cada um de seus registros a classificação da marcação, dizendo se ela é **Original** ou **Informada**.  
  
Para o bom funcionamento do módulo **16-SIGAPON** ao implantar e configurar o módulo deverá efetuar o primeiro acesso nesta rotina para que os motivos sejam criados automaticamente.  
  
**Detalhamento do Processo**  
Ao acessar a rotina, já existirá ou criará os 4 tipos de motivos, que são de padrão do sistema e não é possível excluí-los. Para Incluir um novo motivo, basta clicar em **Incluir** e cadastre conforme *help* do campo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32613274356887)  
  
As **marcações Originais são as marcações vindas do arquivo AFD** – Arquivo Fonte de Dados, coletadas do **REP – Registrador Eletrônico de Ponto**, e podem ser classificadas pelo sistema de duas formas que sinalizam que são **Originais: Com Motivo Registro** em branco e o tipo de registro **"O"**, ou **Rejeição Automática (marcações desprezadas)**  
  
**Veja mais detalhes sobre cada motivo gravado na SP8:**

**- Rejeição Automática**: quando existirem marcações repetidas ou com intervalos de tempo determinado pelo **MV\_DESPMIN** (definição de intervalo de tempo em que as marcações devem ser consideradas como repetidas. Por exemplo: marcação às 08:00 e 08:01 — será considerada apenas a primeira, a segunda ficará como Rejeição Automática). Ou ainda, se a marcação existir no AFD, porém não existir nenhum funcionário cadastrado no sistema com o mesmo PIS do funcionário do AFD.  
**- Inclusão Automática**: marcações com Legenda **A** — Marcação Automática conforme cadastro da Regra de Apontamento e execução da rotina de Leitura/Apontamento.  
**- Inclusão Manual**: são marcações incluídas com Legenda **I** — Marcações informadas pelo usuário através das rotinas de Integrados ou Marcações; ou Legenda **G** — Gerado através da rotina de Miscelânea - Geração de Marcações.  
**- Exclusão Manual**: marcações originais excluídas manualmente e utilizadas com o motivo Exclusão Manual.  
  
Caso o usuário queira incluir novos tipos com descrições mais apropriadas para sua empresa, basta fazer a inclusão conforme sua necessidade.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Significado das legendas do campo P8\_FLAG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050554994-RH-Linha-Protheus-PON-Significado-das-legendas-do-campo-P8-FLAG)
