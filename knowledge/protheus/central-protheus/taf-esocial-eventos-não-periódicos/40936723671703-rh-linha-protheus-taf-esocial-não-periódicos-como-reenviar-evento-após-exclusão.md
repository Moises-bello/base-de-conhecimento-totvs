---
article_id: 40936723671703
category: TAF - eSocial - Eventos Não Periódicos
content_hash: a44d3865ba4c4b0ca9968d3873e7ecf7a6b6febeca0b888d5b3a54d8bd8049d9
fetched_at: '2026-06-28T22:45:18.068226+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Não Periódicos - Como reenviar evento
  após exclusão realizada diretamente no Portal eSocial?
type: support-article
updated_at: '2026-06-03T13:17:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40936723671703-RH-Linha-Protheus-TAF-eSocial-N%C3%A3o-Peri%C3%B3dicos-Como-reenviar-evento-ap%C3%B3s-exclus%C3%A3o-realizada-diretamente-no-Portal-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40936785854743) Tempo aproximado para leitura: **HH:15:00 min**  
  
**Dúvida**  
Como reenviar um evento ao eSocial através do TAF quando a exclusão foi realizada diretamente no Portal eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Não Periódicos - S-3000 (TAFA269) - todas as versões

**Solução**

**Atenção:**   
*Ressaltamos que o processo de exclusão dos eventos direto no governo (Portal do eSocial) é uma ação não recomendada, pois o sistema fica incompleto, causando inconsistências quando precisar integrar e transmitir um novo registro.*  
  
Caso tenha realizado essa ação, não recomendada, por exemplo, excluiu diretamente no governo os evento S-1200, S-1210 - Será necessário ajustar as informações no TAF antes de realizar uma nova integração e transmissão.  
  
Neste cenário, existe no TAF eventos S-3000 rejeitados. pois os eventos de origem (Ex.: S-1200/S-1210) já foram excluídos direto no Portal do eSocial.  
  
**1. Localizar o evento S-3000 rejeitado**

Identifique no TAF o evento **S-3000** que se encontra com status de rejeição.

**2. Realizar o ajuste de recibo**

Execute o procedimento de ajuste de recibo para o evento S-3000, conforme link abaixo:

[RH - Linha Protheus - TAF - eSocial - Funcionalidades - Como realizar ajuste de recibo do eSocial no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672)  
**Observação:** Pode ser informado um número de recibo fictício para o ajuste, por exemplo: **123456**.

**3. Ajustar o status de exclusão**

Após o ajuste do recibo, realize o ajuste do status de exclusão do evento S-3000, conforme link abaixo:  
[RH - Linha Protheus - TAF - eSocial - NÃO PERIÓDICOS - Como ajustar status de exclusão no TAF - S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055468253)

**4. Integrar novamente os eventos**

Após a conclusão dos ajustes, realize a integração dos eventos:  
Exemplo: S-1200, S-1210

**IMPORTANTE**

Não disponibilizamos procedimentos de ajuste via **APSDU**, pois a execução incorreta desses procedimentos pode comprometer a integridade da estrutura do ambiente **TAF/Protheus**.

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
