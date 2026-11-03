---
article_id: 37540495344151
category: NFSE - Nota Fiscal de Serviço Nacional
content_hash: 01596bee9eab3f3c53c8f6ba8f65520290f5f2b2679e60c564a50b93b08dab0b
fetched_at: '2026-06-28T22:39:54.400867+00:00'
product: protheus
section_id: 33955617231639
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE Barueri - 817
  - Campo Código Indicador da operação de fornecimento não informado e/ou fora dos
  padrões estabelecidos no layout
type: support-article
updated_at: '2026-04-11T14:30:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37540495344151-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Barueri-817-Campo-C%C3%B3digo-Indicador-da-opera%C3%A7%C3%A3o-de-fornecimento-n%C3%A3o-informado-e-ou-fora-dos-padr%C3%B5es-estabelecidos-no-layout
---

**Ocorrência**  
Ao realizar a transmissão de uma nota no novo layout de Barueri ocorre a rejeição **"817 - Campo Código Indicador da operação de fornecimento não informado e/ou fora dos padrões estabelecidos no layout".**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Essa rejeição ocorre pois o campo com o **Indicador da Operação** não está sendo devidamente preenchido no Registro 4 dentro TXT transmitido para a prefeitura de Barueri:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37540495316631)

Fonte: <https://www.barueri.sp.gov.br/nfe/Manuais/RPS_Layout-v4.2.pdf?321>   
  
**Solução**  
Para correção, deverão ser realizados **todos os procedimentos** abaixo na seguinte ordem:  
  
**Atualizações**  
  
**TSS**  
Aplicação do patch no RPO do TSS: [12.1.2410](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1164047) ou [12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224026).  
  
Inclusão dos arquivos .CFG e .INI na pasta SYSTEM do TSS: [link.](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1077361)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541023641239)  
  
**Pontos de Atenção**  
  
**1**: Deverá extrair da pasta 'Barueri-SP:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39677372487959)  
  
**2:**O arquivo **nfse\_3505708\_hom.cfg** contempla o novo layout da prefeitura, caso queira também enviar no novo layout em ambiente de produção, deverá realizar uma cópia desse arquivo e renomeá-lo de: nfse\_3505708\_hom.cfg para: nfse\_3505708.cfg e substituir o arquivo já existente na pasta, ficando os três arquivos atualizados:  
  
**nfse\_3505708.cfg** -> Utilizado para o ambiente de produção  
**nfse\_3505708\_hom.cfg** -> Utilizado para o ambiente de homologação  
**nfse\_3505708\_ini** -> Arquivo auxiliar utilizado para ambos os ambientes  
  
Inclusão do arquivo arquivo **tss\_nfse\_tipos\_v2.00.xsd** na pasta **SCHEMAS**do TSS: 12.1.2410: <https://r.totvs.io/p/1244003> ou 12.1.2510: <https://r.totvs.io/p/1243999>.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37544799888407)  
  
**[AMBIENTES COM TSS CLOUD COMPARTILHADO JÁ CONTEMPLAM AS ATUALIZAÇÕES DO TSS].**  
  
**PROTHEUS**  
Expedição continua Protheus com os fontes atualizados até o dia 26/02:  
12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>   
12.1.2510: <https://suporte.totvs.com/portal/p/10098/download?e=1224039>

NFSEXMLENV 02/04/2026:

12.1.2410: <https://r.totvs.io/p/1245348> (Aplicar pacote PTM e compilar no RPO do Protheus).  
12.1.2510: <https://r.totvs.io/p/1245349> (Aplicar pacote PTM e compilar no RPO do Protheus).

Modelo de Transmissão deve ser configurado igual à Prefeitura .  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39141181277591)  
Se certificar de estar configurando o Wizard.cfg por completo dentro da rotina FISA022 com a opção **"3-Web Service":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37557239900055)

**Configurações**  
  
Após todas as atualizações serem realizadas (TSS e Protheus), o Indicador de Operação **deverá ser amarrado nas Regras de Escrituração de IBS e CBS dentro do Configurador de Tributos**, conforme documentação abaixo:  
- <https://tdn.totvs.com/pages/releaseview.action?pageId=1016684365>   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37542633491863)

**Preparação da Nota**  
  
Deverá **gerar uma nova nota do zero**, verificando se o cálculo de IBS e CBS está sendo realizado, juntamente com o Indicador de Operação na tabela CJ3:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541686639255)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541686642711)

**Transmissão da Nota**  
  
Com isso, o comportamento de transmissão será:  
  
XML\_TSS  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541686644503)

XML\_ERP  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37541670562199)  
  
TXT (XML\_LOTE na SPED053)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37543784356631)

**IMPORTANTE**  
Lembrando que esse **código deve ser válido e vinculado ao NBS e cClassTrib.**  
Correlação entre Item de Serv., NBS, cClassTrib e cIndOp:  
- <https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc>  
Caso contrário, a **rejeição será a mesma, tanto para notas sem a montagem dessa informação quanto com a montagem, porém com conteúdo incorreto.**
