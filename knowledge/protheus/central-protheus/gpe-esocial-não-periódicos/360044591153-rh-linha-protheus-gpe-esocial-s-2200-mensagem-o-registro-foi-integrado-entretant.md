---
article_id: 360044591153
category: GPE - eSocial - Não Periódicos
content_hash: 121f37ba5a786c26440e068ff33f911eb9b5e707560cb88b08ff188bbd17ff62
fetched_at: '2026-06-28T22:45:04.534414+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Mensagem "O registro foi integrado,
  entretanto sem a tag <estCiv>. O Est. Civil do trab. não corresponde a nenhuma categoria
  válido do eSocial"
type: support-article
updated_at: '2026-06-16T13:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044591153-RH-Linha-Protheus-GPE-eSocial-S-2200-Mensagem-O-registro-foi-integrado-entretanto-sem-a-tag-estCiv-O-Est-Civil-do-trab-n%C3%A3o-corresponde-a-nenhuma-categoria-v%C3%A1lido-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262162502679) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Mensagem "O registro foi integrado, entretanto sem a tag <**estCiv**>. O Est. Civil do trab. não corresponde a nenhuma categoria válido do eSocial".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esse erro ocorre devido ao **campo estado civil** (RA\_ESTCIVI) estar preenchido com a opção **M** "União Estável" ou **O** "Outros".  
  
**Solução**  
A opção de estado civil **união estável** e **outros** foi retirada do leiaute do eSocial desde a versão 2.2.02. Por esse motivo o sistema não envia o estado civil se estiver vinculado a uma dessas duas opção.  
Para ajuste o campo **estado civil** deve ser preenchido no cadastro do funcionário com uma das opções disponíveis no leiaute de acordo com o De/Para abaixo.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060615073)  
  
Exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059706374)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
