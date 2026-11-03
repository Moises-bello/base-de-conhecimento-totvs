---
article_id: 360024628231
category: GPE - eSocial - Periódicos
content_hash: 9c321d3c8f8ff5fa2a4790089d785d37e335beeb42a0cd681dab0226136379f6
fetched_at: '2026-06-28T22:45:09.843151+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5001 - Como conferir as divergências
  encontradas entre o INSS apurado pelo governo e o relatório do TAF (TAFR120)
type: support-article
updated_at: '2025-11-17T13:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024628231-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-conferir-as-diverg%C3%AAncias-encontradas-entre-o-INSS-apurado-pelo-governo-e-o-relat%C3%B3rio-do-TAF-TAFR120
---

**Ocorrência**Como conferir as divergências encontradas entre o **INSS** apurado pelo governo e o relatório do TAF (*TAFR120*).

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 11.80  
  
**Causa**Quando existe diferença entre o INSS apurado pelo governo e o gerado no sistema, o problema geralmente esta relacionado com a incidência e/ou data de validade da rubrica. O erro pode estar no Governo ou TAF.  
  
**Solução**Para verificar as divergências é necessário que o usuário entenda o funcionamento da validade/vigência inicial das rubricas e a composição do relatório gerado no TAF.

Abaixo descrevo com exemplos o roteiro resumido para analise. Para acessar a documentação completa do relatório consulte o link [TAF - Relatório de Conferencia S-5001](http://tdn.totvs.com/x/zDF-Fw)

**1. Validade de Rubrica:**O governo faz o calculo dos valores de acordo com a incidência e data inicial (validade) da rubrica, ou seja, se houver uma alteração de incidência em 02/2019 o governo vai apurar os valores de acordo com a nova incidência para as folhas a partir de 02/2019, para as folhas anteriores a incidência considerada continuara sendo a antiga.

No TAF a validade pode ser verificada através do cadastro de rubricas (*TAFA232*). Segue exemplo da mesma rubrica com validades diferente no TAF e RET:

Incidências no cadastro do TAF consideradas a partir de 05/2018.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022910091/mceclip9.png)

Incidências no cadastro do TAF consideradas de 01/2018 a 04/2018.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022909871/mceclip8.png)

* Tela de rubricas página do RET:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022909191/mceclip6.png)

**2. Incidências das rubricas e **natureza****

Esse relatório pode ser acessado direto no TAF no caminho atualizações > relatórios > Conferencia > **INSS Base de Calculo**. Abaixo a composição dos valores demonstrados nas principais colunas.

* **Coluna TAF Base de INSS:**São valores da verba de base de calculo que está no TAF, para ser apresentado no relatório a verba deve ter Natureza de Rubrica **9901** no TAF.
* **Coluna Governo Base de INSS:**O governo retorna com a soma de todas as verbas que estão com incidência 11 no campo Cd.Inc.CP (**CodIndCP**) que foram envidas no evento S-1200 no TAF formando a base de calculo.

**Exemplo:**  
Salario (CodIndCP 11 ) = 200,00  
Falta (CodIndCP 11 ) = 50,00

Retorno do Governo será 150,00 (Base INSS)

* **Coluna TAF Valor (desconto) INSS:**Nessa coluna é gerada a verba de desconto de INSS cujo a incidência Cd.Inc.CP (**CodIndCP**) seja **31** no TAF.
* **Coluna Governo Valor (desconto) INSS:**O governo utiliza o valor da base apurada com a soma das incidências **11** e aplica a alíquota de acordo com a tabela.

**Exemplo:**  
Salario (CodIndCP 11 ) = 200  
Falta (CodIndCP 11 ) = 50

Retorno do Gorveno 150,00 (Base INSS) \* 8% = 12,00

* **Coluna TAF Base de INSS 13º:**São valores da verba de base de calculo que está no TAF, para ser apresentado no relatório a verba deve ter Natureza de Rubrica **9901** no TAF.
* **Coluna Governo Base de INSS 13º :**O governo retorna com a soma de todas as verbas que estão com incidência **12** no campo Cd.Inc.CP (CodIndCP) no TAF formando a base de calculo.
* **Coluna TAF Valor (desconto) INSS 13º:**Nessa coluna é gerada a verba de desconto de INSS cujo a incidência Cd.Inc.CP (**CodIndCP**) seja **32** no TAF.
* **Coluna Governo Valor (desconto) INSS 13º:**O governo utiliza o valor da base apurada com a soma das incidências **12** e aplica a alíquota de acordo com a tabela.

Exemplos:

Relatório Retorno S-5001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022899551/mceclip3.png)

Valores no RET (governo)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022887911/mceclip2.png)

**3. Observações:**

1. Quando houver informação de remuneração em período anterior (ex: Dissidio) ({infoPerAnt} em S-1200 não será refeito o calculo no RET, o governo vai assumir o valor descontado na folha;
2. Os valores de diferenças de 13º salario pago na folha de dezembro devem ter natureza 5005 (13º salário complementar);
3. Para desligamentos, o Governo retorna o valor de INSS Folha e INSS 13º Salário consolidados em um mesmo campo, sendo assim, mesmo havendo base de cálculo e recolhimento de INSS sobre 13º salário na rescisão (evento S-2299), os valores serão somados aos valores de Base de Cálculo e INSS mensal e apresentados nas respectivas colunas "Governo".

**4. Importante:**  
Para verificar como corrigir divergência de **incidências** entre Governo, TAF e GPE consulte o artigo: [S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512)

Caso o erro não seja solucionado com as conferencias acima encaminhe as evidencias abaixo para analise do suporte técnico:

* Informar a qual grupo a empresa pertence no **eSocial**, ex: 1º grupo > 78 milhões, 2º grupo < 78 milhões, 3º grupo optante pelo simples;
* Arquivo *XML* do **GPE** e **TAF**. Consulte o link [Como exportar XML de eventos do esocial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006744012;);
* Arquivo com data de todo os fontes. Consulte o link [Como gerar arquivo com a data de todos os fontes?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024518391);
* Print ou vídeo parâmetro MV\_DTCGINI;
* Print ou vídeo do evento S-1200 aba demonstrativo de verbas onde é apresentado o campo **Iden Dem Pgt** e todas as **rubricas**;
* Print ou vídeo de todas as rubricas geradas no S-1200 que estão no site do governo demonstrando as incidências e data de validade;
* Print ou vídeo relatório S-5001 link [TAF - Relatório de Conferencia S-5001](http://tdn.totvs.com/x/zDF-Fw);
* Tabelas SRV e C8R.

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
