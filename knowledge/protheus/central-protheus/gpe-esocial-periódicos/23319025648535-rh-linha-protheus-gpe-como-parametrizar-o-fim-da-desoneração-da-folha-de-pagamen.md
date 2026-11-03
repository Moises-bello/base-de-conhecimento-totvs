---
article_id: 23319025648535
category: GPE - eSocial - Periódicos
content_hash: 025719e30903020449460a2e0301527c63e50afcb1afaca2832d20995103e19a
fetched_at: '2026-06-28T22:45:07.482545+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o fim da desoneração da folha
  de pagamento para o eSocial
type: support-article
updated_at: '2025-07-24T19:53:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23319025648535-RH-Linha-Protheus-GPE-Como-parametrizar-o-fim-da-desonera%C3%A7%C3%A3o-da-folha-de-pagamento-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23318981135383) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como parametrizar o fim da desoneração da folha de pagamento para o eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Essa pergunta foi respondida pelo governo com a divulgação do **item 10.37** no [Perguntas Frequentes eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes#:~:text=02/05/2024)-,Como,-ajustar%20as%20informa%C3%A7%C3%B5es)

No Protheus, para configurar de forma a atender a esse item, realize os seguintes passos:  
**1.** Ajuste o **S-1000** para retirar a opção pela desoneração (empresas e municípios). O novo S-1000 deverá ter o campo **{indDesFolha}=[0]**, com validade a partir do período de apuração **abril/2024**.  
  
**Para alterar**, acesse o módulo **Automação Fiscal** - Atualizações - Configurações TAF - Complemento Cadastral. Após alteração transmita para o eSocial o evento S-1000   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23318981137815)  
  
**2.** Em relação a desoneração aplicada às obras de construção civil com opção pelo recolhimento sobre a receita bruta (grupo [infoObra]), o evento S-1005 **não** deve ser alterado. Os ajustes serão feitos nas regras de cálculo das contribuições.  
  
**3.** Caso já tenha **fechado** a folha de **abril/2024** no **eSocial** será necessário:  
**3.1** Reabrir a folha no eSocial - [RH - Linha Protheus - GPE - eSocial - S-1298 - É possível reabrir o período no esocial através do GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025816453-RH-Linha-Protheus-GPE-eSocial-S-1298-%C3%89-poss%C3%ADvel-reabrir-o-per%C3%ADodo-no-esocial-atrav%C3%A9s-do-GPE)  
**3.2** No caso das empresas e OGMO (Órgão Gestor de Mão de Obra) , **excluir o S-1280** enviado acessando o painel eSocial no módulo Automação Fiscal e seguindo as orientações da imagem abaixo para exclusão do evento transmitido.  
Esse procedimento irá gerar o **evento S-3000** que deverá ser transmitido ao governo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23319025630487)  
  
**4.** Fechar a folha no eSocial novamente. [RH - Linha Protheus - GPE - eSocial - S-1299 - Como gerar o evento S-1299 (fechamento periódicos) para transmitir ao RET](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022286212-RH-Linha-Protheus-GPE-eSocial-S-1299-Como-gerar-o-evento-S-1299-fechamento-peri%C3%B3dicos-para-transmitir-ao-RET)  
  
**Importante**: Para ajuste no SIGAGPE utilize a documentação [RH - Linha Protheus - GPE - Como parametrizar o fim da desoneração da folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002094022-RH-Linha-Protheus-GPE-Como-parametrizar-o-fim-da-desonera%C3%A7%C3%A3o-da-folha-de-pagamento)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
