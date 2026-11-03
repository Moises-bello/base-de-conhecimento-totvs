---
article_id: 360008847432
category: eSocial - Tabelas/Não Periódicos
content_hash: 70fabe60ed332ce4e2921ec2a5141eed6f5be7e729a6e12cbe3afa21cc0f5c3a
fetched_at: '2026-06-28T22:47:10.191763+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial  - Cadastro do evento S-1070 Tabela de Processos Administrativos/Judiciais
type: support-article
updated_at: '2024-09-17T11:36:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008847432-RH-RM-FOP-eSocial-Cadastro-do-evento-S-1070-Tabela-de-Processos-Administrativos-Judiciais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24443141974807) Tempo aproximado para leitura: 00:02:30 min  
  
Dúvida**Como cadastrar as informações que compõem o evento S-1070 - Tabelas de Processos Administrativos/Judiciais?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da versão 12.1.23  
  
**Solução**O evento S-1070 é utilizado para inclusão, alteração e exclusão de registros na Tabela de Processos Administrativos/Judiciais do empregador/contribuinte/órgão público, de entidade patronal com representação coletiva, de trabalhador contra um dos órgãos governamentais envolvidos no projeto do eSocial e que tenha influência no cálculo das contribuições, dos impostos ou do FGTS, e de outras empresas, quando influenciem no cumprimento das suas obrigações principais e acessórias. As informações consolidadas desta tabela são utilizadas para validação de outros eventos do eSocial e influenciam na forma e no cálculo dos tributos devidos e FGTS.

Não devem ser informados nesse evento os processos judiciais que envolvam matéria trabalhista, sejam reclamatórias trabalhistas, sejam processos que envolvam servidores públicos e seus correspondentes órgãos públicos.

**• Cadastro do processo jurídico**  
Para cadastrar as informações que compõem o evento S-1070 siga os passos abaixo: 

1. No TOTVS Gestão de Pessoas acesse **Gestão Organizacional |** **Processos Jurídicos | Processos Jurídicos** e inclua ou edite o processo desejado;  
2. Certifique-se de que o parâmetro **Considerar Processo no eSocial** esteja marcado;  
3. Verifique a necessidade de preenchimento dos anexos do processo;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045463893)

4. Após salvar o processo, será gerado um gatilho do S-1070 para transmissão do governo.

**•** **Processo Judicial** **x Cadastros do sistema**Após cadastrar o processo, faça a associação do processo seguindo as necessidades da empresa de acordo com os modelos a seguir:

- **Cadastro de Seções** (Processo Judicial no evento S-1005)  
1. No cadastro da Seção, acesse aba **eSocial,**informe os processos de acordo com o seu tipo (**Processo alteração alíquota RAT** ou **Processo alteração alíquota FAP**);  
2. Informe os processo de terceiros em **Anexos | Processo Judicial de Terceiros/Outras Entidades.**   
 **- Cadastros de Eventos** (Processo Judicial no evento S-1010)  
1. Acesse **Administração de Pessoal | Eventos** , marque ao tipo de incidência que será suspensa;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044392234)

2. Em seguida, informe o processo judicial sobre a incidência em **Anexos | Processo de Suspensão de Incidência.** 

**- Cadastro de Funcionários** (Processo Judicial no evento S-2200/ S-2206)1. Para vincular o **Processo Judicial** ao funcionário, acesse **Administração de Pessoal | Funcionários** e selecione o funcionário desejado;2. Em seguida selecione **Anexos | Folha de Pagamento | Processos Judiciais do Funcionário** e informe o processo.  
  
- **Cadastro de Lotação Tributária** (Processo Judicial no evento S-1020)  
1. Para vincular o **Processo Judicial** em uma Lotação Tributária, acesse **eSocial | Lotação Tributária**;  
2. Em seguida selecione **Anexos | Processo Judicial de Terceiros** e informe o processo.

**Importante**Para **suspensão** **parcial**, caso o contribuinte possua decisão judicial sobre determinada rubrica para a não incidência parcial de contribuição previdenciária, ou seja, apenas para que não haja o recolhimento de parte da contribuição previdenciária (ex: retirada da incidência apenas para a cota patronal e RAT, mantendo o recolhimento sobre terceiros/outras entidades), deve-se informar o processo no eSocial normalmente e a suspensão correta de cada código de receita deve ser realizada diretamente na DCTFWeb.

**Saiba mais**Para mais informações sobre processos jurídicos acesse:  
      • [Processos Jurídicos](http://tdn.totvs.com/pages/releaseview.action?pageId=452719540)   
      • [Mapeamento do S-1070](http://tdn.totvs.com/display/public/LRM/Evento+S-1070)
