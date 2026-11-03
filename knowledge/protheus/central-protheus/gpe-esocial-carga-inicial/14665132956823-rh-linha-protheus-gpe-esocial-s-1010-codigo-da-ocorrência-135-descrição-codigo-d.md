---
article_id: 14665132956823
category: GPE - eSocial - Carga Inicial
content_hash: 843eaa255c7865ac1f40e188948cf8d7455e0357dcdc4c1565ccc975ffffc062
fetched_at: '2026-06-28T22:45:03.236383+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1010 - Codigo da ocorrência: 135 Descrição:
  Codigo de incidencia tributaria da rubrica para o IRRF invalido'
type: support-article
updated_at: '2023-05-17T21:00:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14665132956823-RH-Linha-Protheus-GPE-eSocial-S-1010-Codigo-da-ocorr%C3%AAncia-135-Descri%C3%A7%C3%A3o-Codigo-de-incidencia-tributaria-da-rubrica-para-o-IRRF-invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**Sequência: 000001 - Tipo: Erro - Codigo da ocorrência: 135 Localização: /eSocial/evtTabRubrica/infoRubrica/inclusao/dadosRubrica/codIncIRRF Descrição: Codigo de incidencia tributaria da rubrica para o IRRF invalido.Acao Sugerida: O valor informado no campo devera existir na Tabela 21 - Codigos de Incidencia Tributaria da Rubrica para o IRRF.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**  
Normalmente este erro ocorre quando é informado um código invalido na incidência IRRF <codIncIRRF>  
É necessário realizar a alteração com base nos códigos vigentes na **Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF**  do leiaute eSocial. Importante que a Tabela S138 no Protheus esteja atualizada.  
  
Exemplo de um código que foi descontinuado: Código 00 - Término em 30/06/2021

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14664896827543) Fonte: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1.1-nt-01-2023/tabelas.html#21>

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1010 - Qual incidência IRRF utilizar nas rubricas para rendimentos não considerados na tributação de IRPF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024934113-RH-Linha-Protheus-GPE-eSocial-S-1010-Qual-incid%C3%AAncia-IRRF-utilizar-nas-rubricas-para-rendimentos-n%C3%A3o-considerados-na-tributa%C3%A7%C3%A3o-de-IRPF?source=search)  
[RH - Linha Protheus - GPE - eSocial - Quais foram as alterações no sistema para atender a Nota Técnica eSocial S-1.1 Nº 01/2023](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13431260251927)  
[RH - Linha Protheus - GPE - eSocial - S-1010 - Após a transmissão dos eventos iniciais (carga inicial), como enviar um único registro para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341633)  
  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)

[LEIAUTES DO ESOCIAL SIMPLIFICADO V. S-1.1 (consolidados até Nota Técnica 01/2023)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-1-01-2023-pdf.zip)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)
