---
article_id: 360039554533
category: GPE - eSocial - Periódicos
content_hash: 3b87b8c9d4b8d419f39ef9833bda3393a3e6c9e45833ebe86360425641a63567
fetched_at: '2026-06-28T22:45:07.493476+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial  -  S-1200/S-1210 - Para que serve o Mnemônico
  P_ESOCMV
type: support-article
updated_at: '2025-07-22T12:17:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039554533-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Para-que-serve-o-Mnem%C3%B4nico-P-ESOCMV
---

**Dúvida**Como gerar um evento com todas as informações por CPF? Como aglutinar os eventos periódicos?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
 **Solução**Para que o sistema aglutine as informações por CPF, para geração dos eventos Periódicos, é necessário que o Mnemônico **P\_ESOCMV**  esteja habilitado (**P\_ESOCMV** = **.T.** ).  
  
Via de regra só é permitido **transmitir para o governo 1 (um) evento S-1200** por **CPF** na competência, caso o usuário tente transmitir 2 (dois) S-1200 para o mesmo CPF dentro do mesmo empregador o governo retorno com o erro "106 - Descrição: Foi Localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, CPF do Trabalhador, Período de Apuração".  
  
Para esses casos o **S-1200 deve ser aglutinado** sempre que existir **mais de um pagamento para o CPF** no **mesmo mês**, esse procedimento deve ocorrer mesmo que o CPF esteja em filiais diferentes, sendo que o sistema só vai gerar 2 (dois) S-1200 se o CPF estiver em Filiais com a RAIZ de CNPJ diferente (8 primeiros dígitos), porque nesse caso é considerado 2 empregadores para o eSocial.  
  
Caso tenha mais de um S-1200 no mesmo mês e se depare com o erro 106 é necessário ajustar o mnemônico, excluir o S-1200 e gerar novamente.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-3000 - Como realizar a exclusão de um Evento Periódico S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027742231-RH-Linha-Protheus-GPE-eSocial-S-3000-Como-realizar-a-exclus%C3%A3o-de-um-Evento-Peri%C3%B3dico-S-1200)  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar funcionários com múltiplos vínculos no evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013550551-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-funcion%C3%A1rios-com-m%C3%BAltiplos-v%C3%ADnculos-no-evento-S-1200)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
