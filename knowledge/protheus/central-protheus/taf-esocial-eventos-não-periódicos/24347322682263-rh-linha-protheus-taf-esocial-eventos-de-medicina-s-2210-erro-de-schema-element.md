---
article_id: 24347322682263
category: TAF - eSocial - Eventos Não Periódicos
content_hash: 7ecc8ece2617f2e0c397255e7a41df966717eac0d169bf0c4c6b9b46dedf48dc
fetched_at: '2026-06-28T22:45:17.977621+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos de Medicina - S-2210 - Erro
  de schema: Element ''{http://www.esocial.gov.br/schema/evt/evtCAT/v_S_01_02_00}nrOC'':
  [facet ''minLength''] The value has a length of ''0''; this underruns the allowed
  minimum length of'
type: support-article
updated_at: '2026-06-16T12:45:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24347322682263-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Medicina-S-2210-Erro-de-schema-Element-http-www-esocial-gov-br-schema-evt-evtCAT-v-S-01-02-00-nrOC-facet-minLength-The-value-has-a-length-of-0-this-underruns-the-allowed-minimum-length-of
---

**Ocorrência**

Erro de schema: Element '{http://www.esocial.gov.br/schema/evt/evtCAT/v\_S\_01\_02\_00}nrOC': [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'.

Element '{http://www.esocial.gov.br/schema/evt/evtCAT/v\_S\_01\_02\_00}nrOC': [facet 'pattern'] The value '' is not accepted by the pattern '.\*[^\s].\*'.

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos de Medicina - S-2210 - Comunicação de Acidente de Trabalho - CAT - Todas as versões

**Solução**  
O erro ocorre pois no XML não foi carregado as informações do médico ou dentista;  
Segue duas opções para preenchimento desses dados:

1. Preencher os campos referentes ao Médico/Dentista que emitiu o atestado dentro do evento S-2210, que está com inconsistência no TAF.  
  
Abra o registro para editar:  
[RH - Linha Protheus - TAF - eSocial - Medicina - S-2210 - Como acessar a Rotina de Comunicação de Acidentes de Trabalho no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008566602-RH-Linha-Protheus-TAF-eSocial-Medicina-S-2210-Como-acessar-a-Rotina-de-Comunica%C3%A7%C3%A3o-de-Acidentes-de-Trabalho-no-TAF?source=search)

Após, altere ou acrescente os dados do médico ou dentista:

**Entre na aba Comunicação de Acidente de Trabalho > sub-aba Atestado > campo Id Prof Saú**

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24347322663831)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24347322664983)

2. Ou, temos a opção de cadastrar o médico ou dentista pela rotina do cadastro de médicos no TAF:  
**Menu principal:**  
**Atualizações > Cadastros > Genéricos > Médicos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24347322666007)  
  
  
Nesta rotina, serão apresentados os registros de médicos e dentistas previamente cadastrados, com a opção de alterar ou excluir, se necessário, além da possibilidade de criar um novo registro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24347320386199)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24347322666903)

**ATENÇÂO:**

Caso opte por preencher por meio da **rotina de cadastro de médico,** em situações onde já possui eventos S-2210 inconsistentes, será necessário recriar o evento ou informar novamente o ID do profissional de saúde no evento S-2210, para que as informações registradas no cadastro de médico sejam corretamente vinculadas.

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:

[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
