---
article_id: 33722284603415
category: RH – DIRF
content_hash: 197f068f4990d7f4a9b4e568f8b980a1c976479cbd282c54fc64e7de3fb3847b
fetched_at: '2026-06-28T22:44:06.942828+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como será gerado o Informe de Rendimentos em 2026
  ano calendário 2025
type: support-article
updated_at: '2026-02-11T11:43:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33722284603415-RH-Linha-Protheus-GPE-Como-ser%C3%A1-gerado-o-Informe-de-Rendimentos-em-2026-ano-calend%C3%A1rio-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33722284566423) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como será gerado o Informe de Rendimentos em 2026 ano calendário 2025?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
  
A partir do ano-base 2025, a Declaração do Imposto de Renda Retido na Fonte (DIRF) passará a ser gerada automaticamente com base nos dados mensais enviados via eSocial.  
No entanto, em um período de transição entre os sistemas, **as empresas ainda são responsáveis pela geração e emissão do Informe de Rendimentos.** e para este ciclo atual, o processo deve ser realizado integralmente pelo SIGAGPE.

O procedimento para a geração do Informe permanece inalterado, os dados da DIRF e do Informe de Rendimentos são extraídos das tabelas SR4/SRL.

A partir deste ano, essas tabelas serão utilizadas **exclusivamente**para o Informe, porém procedimento de [**Geração de Dados da DIRF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012-RH-Linha-Protheus-GPE-Passo-a-Passo-para-gerar-dados-gerar-Arquivo-DIRF)**continua sendo****imprescindível**. (Na documentação→   [**Geração de Dados da DIRF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012-RH-Linha-Protheus-GPE-Passo-a-Passo-para-gerar-dados-gerar-Arquivo-DIRF) seguir até o passo 5)

Esses valores refletem fielmente o cálculo mensal do Imposto de Renda Retido na Fonte (IRRF) que transita pela folha de pagamento, garantindo a precisão dos dados declarados.  
  
Após a geração de dados, o usuário pode alterar ou incluir informações na Manutenção de Dados, lembrando que os dados devem ser corrigidos também no eSocial

Feito isso, se necessário, imprima os Informes através da rotina de Impressão do Informe, conforme a documentação: [Geração do Informe de Rendimentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007796462-RH-Linha-Protheus-GPE-Como-emitir-Informe-de-Rendimento)

A conferência poderá ser realizada de três formas:

1. Relatório de conferência de IRRF ([Painel de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=781873283))
2. Monitor de Conferência de Informações Complementares do IRRF ([Conferência S-5002 - Relatório de IRRF Dados Complementares](https://tdn.totvs.com/x/mR_QPQ))
3. Ficha Financeira - Inclusão de novas Incidências ([Ficha Financeira com dados do eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=1032857822))  
   Esse passo é muito importante porque o campo RV\_INCIRF deve ter a respectiva configuração do campo RV\_DIRF

   
Verique nossa documentação sobre[**Informe de Rendimento**](https://tdn.totvs.com/display/public/PROT/Informe+de+Rendimentos+e+DIRF#integ-integ3)  
  
  
**Saiba Mais**

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37729787696279-RH-Linha-Protheus-GPE-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-a-Entrega-Informe-de-Rendimento-2026-Ano-Calend%C3%A1rio-2025)  
[Informações e atualizações sobre a Entrega Informe de Rendimento 2026 (Ano-Calendário 2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37729787696279-RH-Linha-Protheus-GPE-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-a-Entrega-Informe-de-Rendimento-2026-Ano-Calend%C3%A1rio-2025)    
<https://tdn.totvs.com/display/public/ConSeg/DIRF+-+Informe+de+Rendimento>  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
