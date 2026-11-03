---
article_id: 360061738693
category: GPE - eSocial - Periódicos
content_hash: c3f66f51df5db3b708ab121022c06eda7cb358450d08ebec800dde49f67596f9
fetched_at: '2026-06-28T22:45:09.140542+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 / S-1210 - Inss incorreto quando
  existe rescisão e 13º salário ou erro 726 no S-1210
type: support-article
updated_at: '2025-07-21T14:45:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061738693-RH-Linha-Protheus-GPE-eSocial-S-2299-S-1210-Inss-incorreto-quando-existe-rescis%C3%A3o-e-13%C2%BA-sal%C3%A1rio-ou-erro-726-no-S-1210
---

**Ocorrência**O valor do INSS (previdência) ficar incorreto no eSocial / DCTFWEB, no mês que houve calculo de rescisão e de 13º salário 2ª parcela.  
Erro 726 na transmissão do S-1210, no mês que houve calculo de rescisão e de 13º salário 2ª parcela.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Esse erro pode ocorrer por alguns motivos:  
1º Cenário onde a data de desligamento da rescisão ocorreu após a data de pagamento do roteiro 132 no cadastro do período, onde estava sendo enviado no evento S-2299 a chave de pagamento ideDmDev referente ao roteiro 132 indevidamente.  
  
2º Não existe no calculo da rescisão a verba de ID **1661** **- Base dedutora INSS 13º**,  que é para  situações em que o cálculo da rescisão ocorre após o pagamento da 2ª parcela e não foi deduzido o INSS correto no governo.  
  
3° Cenário onde a data de desligamento da rescisão ocorreu anterior a data de pagamento do roteiro 132 no cadastro de período, nesse caso é necessário que execute o passo 3 e 3.1 da solução.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. **Cenário onde a data de desligamento é posterior a data de pagamento do roteiro 132 no cadastro de períodos:**  
  
Aplicar o pacote de **Expedição Continua RH** disponível na pagina **Entregas Legais,** *link* abaixo:   
  
<https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>   
  
2. Após aplicar o pacote, verifique se existe a verba de ID **1661** **- Base dedutora INSS 13º** no cadastro de verbas e no calculo de rescisão no modulo Gestão de Pessoal (SIGAGPE). Caso não exista execute os procedimento da documentação disponível no *link*: <https://tdn.totvs.com/x/gqLlGg> e caso já existe siga para o passo 2.1  
**OBS:**   
**- Na documentação do TDN acima, deve ser somente realizado o procedimento para criação da verba de ID 1661 (não é necessário aplicar o pacote), e seguir os procedimentos de parametrização da verba, ela deve ser criada conforme a documentação e transmitida para o eSocial com data de inicio de validade do mês de referência que foi feito o desligamento.**   
**- Também deve se seguido os procedimentos para inclusão do ID 1661 no calculo da rescisão.**  
  
2.1 Após efetuado os ajustes dos itens acima, caso já tenha transmitido o evento S-1210 do trabalhador com problema, deve ser feita a exclusão para conseguir encaminhar o evento S-2299, caso não tenha enviado siga para o próximo passo 2.2.  
[RH - Linha Protheus - GPE - eSocial - S-3000 - Como realizar a exclusão de um Evento Periódico S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027742231-RH-Linha-Protheus-GPE-eSocial-S-3000-Como-realizar-a-exclus%C3%A3o-de-um-Evento-Peri%C3%B3dico-S-1200?source=search)  
  
2.2 Caso a folha esteja aberta no GPE, realize a exclusão da rescisão e encaminhe o evento S-3000 para o eSocial, após realize o cálculo novamente e encaminhe o S-2299 para o governo.  
  
2.3 Caso a folha esteja fechada no GPE, acesse no módulo TAF o menu > Atualizações > Eventos Esocial > Não periódicos > Desligamento e realize a exclusão da rescisão, será criado um evento S-3000, transmita para o governo. Após acesse no GPE o cálculo da rescisão como **Visualizar** e > Outras Ações > Integrar com o TAF.  
  
2.4 Acesse a rotina de geração dos eventos periódicos no modulo Gestão de Pessoal (SIGAGPE) pelo menu > Miscelânea > eSocial > Eventos periódicos e realize a integração do evento S-1210 filtrando pelo trabalhador com problema e encaminhe para o TAF após encaminhe para o governo.  
  
3. **Cenário onde a data de desligamento é anterior a data de pagamento do roteiro 132 no cadastro de períodos.**Nesse cenário provavelmente foi enviado o **S-1200 do 13° salário** para o eSocial e no evento **S-2299** também esta gerando as informações de **13° salário** ocasionando duplicidade das informações.  
  
Deve ser verificado se foi enviado as informações de 13°(roteiro 132) nos 2 eventos citado acima, caso sim deve ser realizado o ajuste no evento S-2299 excluindo a chave ideDmDev referente ao roteiro 132.  
  
Para realizar o ajuste, acesse no módulo TAF o menu >Atualizações > Eventos Esocial > Não periódicos > Desligamento, após localize o trabalhador e acesse o S-2299 como "**Alterar**", sem seguida acessa a aba "**Verbas Rescisórias**" e delete a chave de pagamento com final 132  
  
![Kyb1sYCTSP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001788722)  
  
3.1 Após efetuado o ajuste no S-2299, deve ser ajustado também o evento S-1210, pois o mesmo esta sendo enviando com a chave de pagamento 132 com o tipo de pagamento 2 (**Pagamento de verbas rescisórias conforme apurado em {dmDev} do S-2299**).  
  
Para realizar o ajuste, acesse no módulo TAF o menu > Atualizações > Eventos Esocial > Periódicos > Pgto. Rend. Trab. (**TAFA407**) localize o trabalhador e acesse o evento como "**Alterar**" após localize o tipo de pagamento que esta com a chave IdeDmDev com final 132 e altere para o tipo de pagamento 1 (**Pagamento de remuneração conforme apurado em {dmDev} do S-1200**), no GRID "**Detalhamento dos pagamento**" informe no período de referencia o conteúdo "**2020**" para o ideDmDev com final 132.  
  
![TjqV0yqE22.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100687474)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Artigos Calculo 13º Salario](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes) 

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
