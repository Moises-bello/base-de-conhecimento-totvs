---
article_id: 360025643274
category: GPE - eSocial - Periódicos
content_hash: 9664eaff35a2cafb5d0cb53fc5623a1ae3dca394a915e409571a41a36d3ac40f
fetched_at: '2026-06-28T22:45:09.049480+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1299 - Inconsistência do RET - 691
  - Descrição: Nao deve existir evento de admissao parcial sem o correspondente evento
  de admissao'
type: support-article
updated_at: '2025-07-25T20:16:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025643274-RH-Linha-Protheus-GPE-eSocial-S-1299-Inconsist%C3%AAncia-do-RET-691-Descri%C3%A7%C3%A3o-Nao-deve-existir-evento-de-admissao-parcial-sem-o-correspondente-evento-de-admissao
---

**Ocorrência**Nao deve existir evento de admissao parcial sem o correspondente evento de admissao cuja "data de admissão" seja anterior ou igual ao período de apuração da folha de pagamento."  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**O erro ocorre devido haver um evento de admissão preliminar S-2190 que não está associado a um evento S-2200.  
  
No evento S-2200 tem uma Tag onde vai a informação do número de recibo do evento S-2190 e o TAF alimenta automaticamente esse campo.  
 **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039873474)**Em algumas situações o TAF não alimenta a Tag mencionada, isso **normalmente** ocorre por que:  
  
1. O evento S-2190 foi informado diretamente no portal do eSocial;  
  
2. Quando o evento S-2190 tem informações divergentes do evento S-2200, por exemplo, no S-2190 foi informada uma data de admissão e no evento S-2200 foi informada outra;  
  
3. Quando foi enviado um evento S-2190 por engano, por exemplo, quando na realidade o registro do Trabalhador é um S-2300 e isso só é percebido posteriormente.  
 **Solução****Solução do item 1.** Sugerimos que entre em contato diretamente ao RET  (Governo) através dos canais de comunicação disponíveis através do portal do eSocial, pois talvez seja necessário excluir o evento diretamente via portal, por onde ele foi criado, mas as consequências são de responsabilidade exclusiva da Empresa.  
  
Uma segunda possibilidade de correção é trazer esse evento S-2190 para o TAF e retificar o S-2200, caso deseje auxílio com essa tratativa entre em contato com o Suporte do TAF - Protheus.  
**Solução do item 2.** No Leiautes do eSocial o Sistema traz a informação transcrita abaixo:  
  
"Informar o número do recibo do evento S-2190 - Admissão de Trabalhador - Registro Preliminar, caso o mesmo tenha sido enviado. Validação: **Se informado, deve ser um recibo de entrega válido e as informações de CPF, Data de Nascimento e Data de Admissão informadas no evento correspondente devem ser iguais às informações prestadas neste evento.** Se não informado, verificar a existência de evento de admissão preliminar (S-2190) para o mesmo CPF e que não tenha evento de admissão correspondente. Caso exista, rejeitar este evento de admissão."  
  
Você deverá analisar qual é o evento divergente e realizar a tratativa, pode ter situações que será necessário excluir um dos eventos, mas os riscos e consequências devem ser analisados por cada Empresa. **Solução do item 3.** No MOS - Manual de orientações do eSocial no evento S-2190 existe a seguinte descrição:  
 **"Conceito do evento:** Este evento é opcional, a ser utilizado quando não for possível enviar todas as informações do evento “S-2200 – Cadastramento Inicial e Admissão/Ingresso de Trabalhador” até o final do dia imediatamente anterior ao do início da respectiva prestação do serviço. Para tanto, deve ser informado: CNPJ/CPF do empregador, CPF do trabalhador, data de nascimento e data de admissão do empregado. É imprescindível o envio posterior do evento S-2200 para complementar as informações da admissão e regularizar o registro do empregado."No conceito não há menção do S-2300, sendo assim, nesse cenário também sugerimos que entre em contato diretamente ao RET  (Governo) através dos canais de comunicação disponíveis através do portal do eSocial, pois talvez seja necessário excluir o evento S-2190, mas as consequências são de responsabilidade exclusiva da Empresa.  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
