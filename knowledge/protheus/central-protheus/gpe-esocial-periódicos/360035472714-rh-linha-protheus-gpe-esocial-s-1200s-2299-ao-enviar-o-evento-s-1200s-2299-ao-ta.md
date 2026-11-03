---
article_id: 360035472714
category: GPE - eSocial - Periódicos
content_hash: 80e06c93d069ed1b6d4af3d01bc43a27e8458fe5f69cf3e7fd0bc6f1074e392c
fetched_at: '2026-06-28T22:45:08.806731+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Ao enviar o evento S-1200/S-2299
  ao TAF é apresentada a mensagem: O valor ''X'' informado na tag codLotacao não existe
  na base dados'
type: support-article
updated_at: '2026-05-21T17:53:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035472714-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Ao-enviar-o-evento-S-1200-S-2299-ao-TAF-%C3%A9-apresentada-a-mensagem-O-valor-X-informado-na-tag-codLotacao-n%C3%A3o-existe-na-base-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33640482785943) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao enviar o evento S-1200/S-2299 ao TAF é apresentada a mensagem: "O valor 'X' informado na tag **codLotacao** não existe na base dados."  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Essa mensagem de erro ocorre no momento de integração do evento S-1200 ou S-2299, normalmente, devido a:

1. Existir algum Centro de Custo no cálculo da Folha que está gerando o evento S-1200 que ainda não foi enviado ao TAF/Middleware através do evento S-1020;
2. Ambiente Desatualizado;
3. Problema no "Compartilhamento / Modo de Acesso";
4. Problema na configuração do Complemento Cadastral do TAF;
5. Mudança no Complemento Cadastral do TAF após já ter enviado eventos de tabela (S-1005, S-1020, etc.) ao TAF;

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Transmitir ao TAF o evento S-1020 faltante.  
   [RH - Linha Protheus - GPE - eSocial - S-1020 - Após a transmissão dos eventos iniciais (carga inicial), como enviar um único registro de Lotação para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016403372-RH-Linha-Protheus-GPE-eSocial-S-1020-Ap%C3%B3s-a-transmiss%C3%A3o-dos-eventos-iniciais-carga-inicial-como-enviar-um-%C3%BAnico-registro-de-Lota%C3%A7%C3%A3o-para-o-TAF)
2. Atualize seu ambiente com as atualizações disponíveis em nossa página [eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais#).;
3. Verifique se o "Compartilhamento / Modo de Acesso" de suas tabelas está de acordo com o descrito no artigo  
   [MP - GPE - eSocial - Como deve ser definido o Compartilhamento de Tabelas SIGAGPE x SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004178832/);
4. Verifique se o Complemento Cadastral do TAF está de acordo com o descrito no artigo  
   [TAF - COMPLEMENTO CADASTRAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027279052-TAF-COMPLEMENTO-CADASTRAL-TAFA050-?source=search);

No caso da mudança da configuração do Complemento Cadastral do TAF sugerimos que consulte o seu Gerente de Contas da TOTVS e verifique a possibilidade de solicitar um analista "in loco" para validar a consistência dos dados de suas tabelas, pois essa mudança implica em tudo que já foi transmitido antes da mudança e o Sistema não consegue localizar essas informações.  
  
**Saiba Mais**Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página* [***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
