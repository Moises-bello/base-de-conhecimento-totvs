---
article_id: 38333677013143
category: GPE - eSocial - Periódicos
content_hash: adc7116c2da45acc3888d4826ed762ea8e6f8e48d22d611d8f7f12719947e412
fetched_at: '2026-06-28T22:45:07.378156+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - Código da ocorrência: 195 Descrição:
  O somatório de todas as rubricas de todos os demonstrativos referenciados nos grupos
  de "Informacoes de Pagamento", cujos campos de Codigo de Incidencia de IR'
type: support-article
updated_at: '2026-06-24T14:41:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38333677013143-RH-Linha-Protheus-GPE-eSocial-S-1210-C%C3%B3digo-da-ocorr%C3%AAncia-195-Descri%C3%A7%C3%A3o-O-somat%C3%B3rio-de-todas-as-rubricas-de-todos-os-demonstrativos-referenciados-nos-grupos-de-Informacoes-de-Pagamento-cujos-campos-de-Codigo-de-Incidencia-de-IR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38333663400215) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 195 Descrição: O somatorio de todas as rubricas de todos os demonstrativos referenciados nos grupos de "Informacoes de Pagamento", cujos campos de Codigo de Incidencia de IR nos eventos de Rubrica iguais a 31, 32, 33 e 34 e tipo de rubrica iguais a 2 e 4, devera ser maior ou igual ao somatorio do valor das rubricas cujo tipo de rubrica sejam iguais a 1 e 3.Incidencias identificadas com inconsistencias:Incidencia 33, somatorio -XXXX Acao Sugerida:Verifique o resultado do somatorio conforme os codigos de incidencia e tipo de rubrica informados acima.  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Gere o relatório do evento de pagamento, [**S-1200 filtrado por CPF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE)ou [**S-2299**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299);  
2. Filtre pela coluna IRRF esocial as incidencias de retenção de IRRF 31, 32, 33 e 34  
3. Verifique o tipo da verba, se é 1-Provento | 2-Desconto | 3-Base (Provento) | 4-Base (Desconto)  
4. Ao verificar a verba com incidencia errada, ajuste através do cadstro de verbas, na aba esocial, campo IncIRRF  
5. Confirme a alteração com competencia igual ou anterior do evneto de pagamento  
6. Transmita o S-1010  
7. Retifique o S-1200 que contém a verba com incidencia errada  
  
Verifique o artigo para auxiliar na retificação: [RH - Linha Protheus - GPE - eSocial - Como retificar ou reprocessar os Totalizadores (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254-RH-Linha-Protheus-GPE-eSocial-Como-retificar-ou-reprocessar-os-Totalizadores-DCTFWEB-no-eSocial?source=search)  
  
Veja o video de exemplo de conferência!  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
