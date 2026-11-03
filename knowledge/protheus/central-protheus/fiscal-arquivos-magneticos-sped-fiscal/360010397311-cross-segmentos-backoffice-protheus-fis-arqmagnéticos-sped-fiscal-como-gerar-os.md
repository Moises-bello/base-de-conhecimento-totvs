---
article_id: 360010397311
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: de6950a1f88d775a943eca2101235d8119b6b2479a665d59db3c379ee0311fbd
fetched_at: '2026-06-28T22:42:02.693656+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal  -
  Como gerar os registros C400, C405, C410, C420, C425, C460, C470, C490 e C495
type: support-article
updated_at: '2023-03-03T12:42:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010397311-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-os-registros-C400-C405-C410-C420-C425-C460-C470-C490-e-C495
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: 00:02:00 min

**Dúvida**

Como gerar os registros **C400, C405, C410, C429, C425, C460, C470, C490 e C495?**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Solução**

Os registros são gerados a partir do módulo **Controle de Lojas (SIGALOJA)** e é composto das estações cadastradas no Sistema.

**Cupom Fiscal Modelo 2D - Espécie ="CF"**

Para geração dos registros deve ser revisado configurações abaixo referente ao módulo **SIGALOJA**.

* A tabela **SLG** está compartilhada ou exclusiva, no caso, para gerar o registro esta tabela deve estar EXCLUSIVA;
* A tabela **SFI** está compartilhada ou exclusiva, no caso, para gerar o registro esta tabela deve estar EXCLUSIVA;
* A tabela **SLG** campo **LG\_SERPDV** está igual a campo na tabela **SFI FI\_SERPDV**;
* Verificar nas tabelas **SLG, SFI, SF3, SFT** se os campos **XX\_PDV** estão preenchidos com o mesmo conteúdo;
* Verificar na tabela **SFI** o campo **FI\_VALCON** deve estar maior que zero e um destes **FI\_BAS7**, **FI\_BAS12, FI\_BAS17, FI\_BAS18, FI\_BAS25** também deve estar maior que zero;
* Verificar se na tabela **SD2** o campo **D2\_SITTRIB** foi preenchido;
* Não efetuar o reprocessamento dos dados pela rotina loja (**LOJA300**) mas, sim, pela rotina dos livros fiscais (**MATA930**);

**Observações**

* Caso os parâmetros estejam configurados **MV\_LJGRMR=S** e **MV\_LJLVFIS=2** não será necessário a geração do reprocessamento da rotina **MATA930** para geração das informações do Livros Fiscais tabelas **SF3 e SFT**.
* As informações dos cupons serão geradas automaticamente nas tabelas **SF3** e **SFT** no momento do seu lançamento do cupom pelo modulo **SIGALOJA**.
* Caso parâmetro **MV\_LJGRMR=N** deverá ser gerado o reprocessamento pela rotina **MATA930** para geração das informações dos livros fiscais **SF3** e **SFT**.
* Com a correta gravação dos cupons na tabela **SF3** e **SFT** será levado as informações para arquivo **SPEDPFISCAL C400** e filhos.
* Verificar na tabela **SF3** e **SFT** se estes cupons não estão deletados e com a espécie **CF**;
* Verificar se todos os itens emitidos no período estão sendo gerados no arquivo magnético **SPEDFISCAL**.
* Comparar a tabela **SFI** com a Impressora fiscal.

 Após análise e campos correto deverá ser realizado a geração do arquivo **SPEDFISCAL** com a pergunta **Gera registro da ECF = Sim.**

*Wizard* **SPEDFISCAL**

Caminho: **Livros Fiscais / Miscelânea / Arquivos Magnéticos / SPEDFISCAL**

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A16%3A21.png?version=1&modificationDate=1467933380000&api=v2)

Para mais informações sobre o **Sped Fiscal***,* acessar o *link* abaixo:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
