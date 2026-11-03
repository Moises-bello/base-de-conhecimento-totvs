---
article_id: 39722542737303
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 41e54f38c17bbbf62104939038b9dfdb9ce7eca5bc9927307882bd890150fff9
fetched_at: '2026-06-28T22:39:09.687471+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Performance na rotina
  de Cadastro de Produtos MATA010
type: support-article
updated_at: '2026-04-16T11:47:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39722542737303-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Performance-na-rotina-de-Cadastro-de-Produtos-MATA010
---

A performance da rotina de Cadastro de Produtos (MATA010) no TOTVS Protheus depende da atualização dos artefatos, validação de se existe uso de Pontos de Entrada, e configuração adequada dos parâmetros MV\_CADPROD e MV\_FACAUTO. É recomendado validar atualizações, desativar customizações que prejudiquem desempenho, ajustar parâmetros para evitar processamento desnecessário e analisar logs para identificar causas de lentidão persistente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39722515635351) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Como melhorar a performance de processamento (inclusão, alteração, visualização e exclusão) na rotina de Cadastro de Produtos (MATA010)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A performance da rotina de Cadastro de Produtos (MATA010) pode estar diretamente ligada à atualização dos artefatos do sistema, mas também sofre influencia do uso de customizações (Pontos de Entrada) e configuração de parâmetros chave como: **MV\_CADPROD** e **MV\_FACAUTO**).

**Para manter uma performance saudavel na rotina, valide os pontos a seguir:**

**Atualização de Artefatos:** Certifique-se de que o fonte da rotina MATA010 e os artefatos gerais estejam atualizados. A performance possui ligação direta com o layout da rotina e a interface de menus que atuam com o framework (exemplo: utilização da webapp.dll e campos memo).

[- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) | [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [WebApp](https://tdn.totvs.com/display/tec/WebApp+-+Configurando+nativamente+o+Application+Server+como+servidor+Web)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
- [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)  
- [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)

**Pontos principais:**

1. **Geração Automática do Código dos Produtos (B1\_COD):**

   É comum a utilização de Pontos de Entrada para o sequenciamento automático do campo B1\_COD, o que pode prejudicar a performance se não for devidamente otimizado. Realize um teste com os Pontos de Entrada desativados para avaliar o comportamento do sistema isoladamente.

   Caso não possua Pontos de Entrada, avalie se não existe alguma Função de Usuário nos campos chave como B1\_COD ou B1\_DESC ([Tratamento correto para controle de numeração B1\_COD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16660636353047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tratamento-correto-para-controle-de-numera%C3%A7%C3%A3o-B1-COD)).
2. **Parâmetro MV\_CADPROD:**

   Avalie a real necessidade de possuir todas as integrações com as tabelas envolvidas na rotina, evitando amarrações desnecessárias, é possível reduzir a quantidade de tabelas processadas.

   **Atenção (Módulo AGRO):** O uso do conceito de dados do Agronegócio (AGRO) neste parâmetro faz com que a rotina **MATA010** carregue os modelos de tabelas como **NCR, NC7, NCI, NCA, NCK e NCC**. Isso onera o tempo de processamento. **Caso não utilize o módulo AGRO, certifique-se de desconsiderar esta configuração no parâmetro.**

   Lista geral das tabelas usadas com o conceito de uso do "**AGRO**" no parametro: [Agro - Linha Protheus - AGR - Tabelas Referentes ao Agronegócio para o Cadastro de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041363273-Agro-Linha-Protheus-AGR-Tabelas-Referentes-ao-Agroneg%C3%B3cio-para-o-Cadastro-de-Produtos)

   **Saiba mais sobre o MV\_CADPROD:** [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilidade e configuração do parâmetro MV\_CADPROD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD)
3. **Parâmetro** **MV\_FACAUTO****:**   
   Verifique a necessidade de utilizar a amarração tributária diretamente no cadastro do produto. Se não for necessário, desative o parâmetro. A amarração pode ser realizada posteriormente pelo Contábil.

   **Saiba mais sobre o MV\_FACAUTO:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como cadastrar o perfil de participante ou dar Manutenção?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25948625830935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-cadastrar-o-perfil-de-participante-ou-dar-Manuten%C3%A7%C3%A3o)

**Outros Parâmetros e Validações:**

* **Parâmetro MV\_VEICULO:** Caso não utilize a integração, preencha o parametro com N. Saiba mais sobre o conceito do parametro aqui: [Parâmetro MV\_VEICULO](https://tdn.totvs.com/x/lx48Mw)
* **Parâmetro MV\_LJGRINT:** Caso não utilize a integração, preencha o parametro com F. Saiba mais sobre o conceito do parametro aqui: [Parâmetro MV\_LJGRINT](https://tdn.totvs.com/x/4soYIQ)
* **Parâmetro MV\_PIMSINT :** Caso não utilize a integração, preencha o parametro com F. Saiba mais sobre o conceito do parametro aqui: [MV\_PIMSINT - Habilita a integração Protheus x Pims Grãos](https://tdn.totvs.com/x/qeMKDg)
* **Parâmetro MV\_HISTTAB :** Caso não utilize a integração, preencha o parametro com F. Saiba mais sobre o conceito do parametro aqui: [Parâmetro MV\_HISTTAB](https://tdn.totvs.com/x/XwI0Mw)
* **Parâmetro MV\_A010FAC:** Valide a necessidade de campos adicionais, se de fato é necessario possuir ou não. Saiba mais: [Parâmetro MV\_A010FAC](https://tdn.totvs.com/x/N870E)

**Análise de Logs:**

Caso o ambiente esteja totalmente atualizado, sem impacto de Pontos de Entrada e com os parâmetros ajustados, mas a lentidão persista, gere um **LogProfiler** e um **DBTrace** durante o processo de baixa performance.  
**Encaminhe estes logs para análise de suporte, juntamente com os dados da Central de Diagnósticos** (para validação das atualizações aplicadas) e se possivel um vídeo demonstrando o comportamento passo a passo:

* [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como gerar o LogProfiler e Dbtrace?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-gerar-o-LogProfiler-e-Dbtrace)
* [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

**Saiba Mais**

[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
