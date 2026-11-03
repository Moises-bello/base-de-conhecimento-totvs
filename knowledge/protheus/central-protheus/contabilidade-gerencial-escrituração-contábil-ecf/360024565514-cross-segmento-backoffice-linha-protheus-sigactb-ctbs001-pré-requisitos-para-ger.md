---
article_id: 360024565514
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: e747f448c9946fc5c62a89f4de7502a69fa5d6089e9bfe70f433a25a8cbeb571
fetched_at: '2026-06-28T22:40:47.291971+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Pré requisitos
  para geração da ECF
type: support-article
updated_at: '2025-06-30T20:20:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pr%C3%A9-requisitos-para-gera%C3%A7%C3%A3o-da-ECF
---

**Dúvida**

Quais os Pré-Requisitos para entrega da ECF  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade gerencial– A partir da versão 12  
  
**Solução**

**1°** **Passo: Ambiente Contábil atualizado**

Para garantir o correto funcionamento do sistema, é fundamental que o ambiente esteja devidamente atualizado. Por favor, consulte a documentação abaixo para obter informações sobre os requisitos de atualização:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - Pacote de atualização da ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32551679139735-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-da-ECF-2025-leiaute-11)

**2° Passo: Integração Contábil x TAF**  
Para que o sistema possa integrar os movimentos da Contabilidade (Módulo 34) com o TAF (Módulo 84), é necessário seguir os procedimentos descritos na documentação a seguir:  
  
[CTBS001 - ECF - Parâmetros de Integração do módulo contábil para o módulo do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072)

**3°** **Passo:** **Calendário contábil (CTBA010)**

Apuração trimestral: É necessário ter um Calendário Contábil trimestral com 4 períodos. Caso você já possua um calendário anual, é preciso incluir um calendário trimestral separado, sem amarração da moeda.

Apuração Anual: É necessário ter um Calendário Contábil Anual com 12 períodos.

**4°** **Passo: Plano de contas (CTBA020)**

* Os seguintes campos devem está preenchidos, CT1\_NATCTA ,CT1\_NTSPED ,CVN\_CLASSE e CVD\_NATCTA
* O mapeamento do plano de conta referencial é facultativo, se optar por fazer o relacionamento segue link com modelos:  
    
  [ECF - arquivos modelos - plano referencial / visões gerenciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008505768)  
  [CTBA025- Plano Referencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007547712)

**5°** **Passo: Cadastro do Contabilista (CTBA015)**Através da rotina CTBA015 o sistema possibilita cadastro o contabilista para gerar o registro J930 e 0930

**6**° **Passo : Cadastro do participante (CTBA016)**Neste cadastro são armazenados os dados dos responsáveis pela movimentação contábil da empresa, tais como sócios, acionistas, proprietários, entre outros, que respondem pela empresa.

**7°** **Passo : Cadastro da Visão Gerencial (CTBA161)**O sistema utiliza a visão gerencial fornecida para gerar o Balanço Patrimonial e o Demonstrativo de Resultado. Caso a visão gerencial não seja informada, o sistema utilizará o plano referencial vinculado ao plano de contas.  
 **Atenção:** Caso a visão gerencial esteja cadastrada de forma incorreta, isso resultará em erros durante a validação da ECF. Abaixo, fornecemos alguns links que explicam como realizar a parametrização corretamente.  
  
[CTBA161 - Arquivos modelos Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252)

[Como importar Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672)

[CTBA161 /CTBA130 - Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012)

[ECF - É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491)

**8° Passo:** **Validações de ambiente**

* O compartilhamento das tabelas de cadastros CTG, CTO, CQD e CTE devem ser iguais;
* O compartilhamento das tabelas de movimentos/saldos CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ07 CQ8, CQ9, CT2 e CTC devem ser iguais;
* As tabelas do TAF C10 e CH5 devem ter o mesmo compartilhamento das tabelas CT1, CVD e CVN;
* O compartilhamento das tabelas do CTB devem estar conforme a tabela De/Para das Tabelas CTx para CSx para elaboração ECD:  
    
  [ECD - Tabelas ECD e ECF compartilhamento;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572)  
  [ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411)
* Verifique o tamanho dos campos das entidades Conta contábil, Centro de Custo, Item Contábil e Classe Valor   
  [Alteração do tamanho das entidades contábeis;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251)  
  [CTBA211 - Grupo de perguntas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028526532)
* Os campos CTT\_CUSTO, CTD\_ITEM, CTH\_CLVL e CT1\_CONTA consultado via APSDU na tabela SX3 devem ter o mesmo tamanho do informado no respectivo grupo de campos.

**9° Passo: Conferencia dos dados**

* Imprima no período que irá realizar a apuração e confira os dados dos relatórios, Razão Contábil (CTBR400), Balancete (CTBR040), DRE (CTBR510) e Balanço Patrimonial (CTBR500).
* Verifique apuração de resultados se foi executada e se as conta de receita e despesa foram zeradas
* Ao consultar a chave LP na rotina Dados Auxiliares CTB (CTBA007) deve conter 1 registro de apuração com final Z, para o ano de apuração

**10° Passo: Tratamento de Performance**Para que o sistema tenha mais performance no momento em que está gerando a ECF, será necessário habilitar as procedures dinâmicas.  
  
[Habilitar procedures dinâmica na geração da ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632)

**11° Passo : Configuração de acordo com o regime tributário** 

* [ECF – Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431)
* [ECF – Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711)
* [ECF – Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052)
* [ECF – Imune ou isenta como gerar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974)
* [ECF - Arquivo Fracionado e ou Situação Especial (Extinção, Fusão, Incorporação, Transformação...)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007208532)

**12° Passo: Geração Lalur**A fim de garantir que o sistema produza corretamente as informações do Livro de Apuração do Lucro Real (LALUR) e posteriormente realize sua devida apuração, é necessário seguir a documentação a seguir:

[Lalur - Cadastro, apuração e integração com o ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831)

[ECF - Lalur](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571)

Saiba mais:  
[Cross Segmento Backoffice Linha Protheus - SIGACTB ECF CADASTRO DE CALENDÁRIO CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024569414)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF – O que avaliar quando J050 e J051 não é gerado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771)  
[Cross Segmento - Backoffice Linha Protheus -SIGACTB - ECD e ECF - CTBA015 REGISTRO J930 e 0930: Identificação dos Signatários da Escrituração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020083171)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Compartilhamento de Tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007377851)   
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - BLOQUEIO DE ALTERAÇÃO DE COMPARTILHAMENTO A PARTIR LIB versão 20181015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA211- Como realizar Apuração de resultados dentro do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472)
