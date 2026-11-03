---
article_id: 360018448812
category: GPE - eSocial - Periódicos
content_hash: d388ac303e6756dac4a75f38852d145c3346e5d9b4aba080f56c4fb7617190b8
fetched_at: '2026-06-28T22:45:08.911353+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Como é formado o relacionamento
  entre os eventos S-1210 e S-1200 e suas chaves de identificação ideDmDev
type: support-article
updated_at: '2025-07-24T13:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018448812-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-%C3%A9-formado-o-relacionamento-entre-os-eventos-S-1210-e-S-1200-e-suas-chaves-de-identifica%C3%A7%C3%A3o-ideDmDev
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27702737094423)Tempo aproximado para leitura: **00:02:00min  
  
Dúvida**  
S-1210 - Como é formado o relacionamento entre os eventos **S-1210** e **S-1200** e suas chaves de identificação *ideDmDev*?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No evento **S-1200** existe a coluna **Iden Dem Pgt** (*tag ideDmDev*) que contém a chave do recibo de pagamento criado no momento da geração dos eventos periódicos. E no evento **S-1210** na coluna **Ident Dem Vl** (*tag ideDmDev*)  existe a mesma chave que está no S-1200 que pertencente ao mesmo mês de referencia. O evento S-1200 é enviando sempre antes do evento S-1210 do mesmo mês de referencia.  
O que deve ficar claro nesses dois eventos é que nem sempre a **chave** do evento **S-1210** estará no mesmo mês de apuração do **S-1200**.   
Esse diferença é comum em empresas de regime de **caixa** onde o pagamento da folha ocorre no próximo mês. Para as empresas regime competência onde a folha é paga dentro do mês de apuração as chaves de pagamento ideDmDev ficam iguais no evento S-1200 e S-1210 do mesmo período de apuração.  
  
Para que as informações fiquem corretas no **eSocial** o **S-1210** tem 2 tags:  
  
1. tag ***perApur*** (identifica o mês da geração);  
  
2. tag***perRef*** (que identifica a qual competência da folha (**S-1200**) pertence a chave e valor).  
  
Assim através da tag *perRef* (coluna **Per. Referen**) o governo consegue localizar que já foi enviado um S-1200 no mês anterior para o casos de regime de caixa.  
  
Obs: Existem cenários que a tag *perRef* não é obrigatório, para entender mais verifique as validações do leiaute.  
  
**Essa informação está detalhada no [leiaute vigente do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica) nos tópicos abaixo:**

* **S-1200:** *tag perApur* - Informar o mês/ano (formato AAAA-MM) de referência das informações.  
    
  **Obs:** Essa data é definida no campo Competência da rotina eventos periódicos e gravada no TAF no campo **Per.Apuração**.
* **S-1200:** *tag ideDmDev -*Identificador atribuído pela empresa para o demonstrativo de pagamento. O empregador poderá preencher este campo utilizando-se de um identificador padrão para todos os trabalhadores, no entanto, havendo mais de um pagamento relativo a um mesmo período de competência devem ser utilizados identificadores diferentes para cada um dos demonstrativos. Validação: Deve ser um identificador único dentro da mesma competência para cada um dos demonstrativos de pagamento do trabalhador.  
   **Obs:** Essa chave é criada no sistema de forma automática e composta pelos dados da FILIAL + DATA DE PAGAMENTO + PERÍODO + ROTEIRO.
* **S-1210:** *tag perApur* - Informar o mês/ano (formato AAAA-MM) de referência das informações.  
   **Obs:** Essa data é definida no campo Competência da rotina eventos periódicos e gravada no TAF no campo **Per.Apuração**.
* **S-1210:** *tag perRef* - Informar a competência à qual se refere a folha de pagamento no formato AAAA-MM, se for relativa a folha de pagamento normal (mensal, quinzenal, etc.) ou AAAA, se for relativa a folha de 13° salário. Validação: Informação obrigatória se {*tpPgto*} = [1,5]. Não pode haver informação nos demais casos. Deve estar no formato AAAA-MM ou AAAA.  
    
  **Obs:** Essa data é criada no sistema de forma automática ao gerar o evento S-1210 através da rotina eventos periódicos e gravada no TAF no campo **Per.Referen**.
* **S-1210:** *tag ideDmDev* -Identificador atribuído pela fonte pagadora para o demonstrativo de valores devidos ao trabalhador conforme definido em S-1200, S-1202, S-2299 ou S-2399. Validação: Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202, S-2299 ou S-2399 no campo {*ideDmDev*}, obedecendo a relação: Se {*tpPgto*} = [1], em S-1200; Se {*tpPgto*} = [2], em S-2299; Se {*tpPgto*} = [3], em S-2399; Se {*tpPgto*} = [5], em S-1202.  
    
  **Obs:** Essa chave é criada no sistema de forma automática e composta pelos dados da FILIAL + DATA DE PAGAMENTO + PERÍODO + ROTEIRO.   
    
  **Saiba Mais**Para saber mais consulte os links abaixo:   
  [MP - GPE - eSocial - S-1210 - Erros 723, 724, 726 no retorno do evento transmitido ao governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024125112-MP-GPE-eSocial-S-1210-Erros-723-724-726-no-retorno-do-evento-transmitido-ao-governo?source=search)  
  [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
  [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
  [Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  

  Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

  *Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
