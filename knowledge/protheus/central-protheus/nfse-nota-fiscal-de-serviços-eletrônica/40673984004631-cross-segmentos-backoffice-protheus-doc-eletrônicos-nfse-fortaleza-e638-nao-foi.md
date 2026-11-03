---
article_id: 40673984004631
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6a95cfcb773d0344d30c0a83215e72fc57a60ae81e6ddc33658aaa2b76a186d0
fetched_at: '2026-06-28T22:39:57.449397+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Fortaleza
  - E638 (Nao foi possivel processar o RPS, pois nao foram informados os campos obrigatorios
  referentes ao IBS/CBS, conforme regras de validacao do layout da NFS-e)
type: support-article
updated_at: '2026-05-22T19:23:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40673984004631-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Fortaleza-E638-Nao-foi-possivel-processar-o-RPS-pois-nao-foram-informados-os-campos-obrigatorios-referentes-ao-IBS-CBS-conforme-regras-de-validacao-do-layout-da-NFS-e
---

**Ocorrência**  
Ao realizar a transmissão de um RPS para a prefeitura de Fortaleza, está sendo retornado a seguinte rejeição:  
  
***<Codigo>**E638**</Codigo>***  
***<Mensagem>**Nao foi possivel processar o RPS, pois nao foram informados os campos obrigatorios referentes ao IBS/CBS, conforme regras de validacao do layout da NFS-e**.</Mensagem>***  
***<Correcao>**Preencha as informações obrigatorias referentes ao IBS/CBS e reenvie o lote.**</Correcao>***  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Causa**  
Essa rejeição ocorre pois as tags de IBS/CBS não estão sendo geradas.  
  
**Solução**  
A partir da semana do dia 18/05 **se tornou obrigatório o envio das informações de IBS/CBS** no XML da nova versão de layout **(2.00)** da prefeitura de Fortaleza.  
  
Com isso, se fará necessário a configuração de cálculo de IBS/CBS dentro do Configurador de Tributos, tal como Indicador de Operação, CST e cClassTrib, além do NBS.  
  
Além disso, é necessário **validar se o parâmetro MV\_RTC56 está com a data correta** (ou seja, menor ou igual a data atual), permitindo assim que o rdmake NFSEXMLENV monte as informações corretamente e o TSS posteriormente replique no layout da prefeitura, exemplo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40674203594647)  
  
**Lembrando que qualquer dúvida sobre essa antecipação dessa obrigatoriedade, o fisco da prefeitura deverá ser acionado.**  
  
**IMPORTANTE**  
Dúvidas na escrituração, cálculos de IBS/CBS ou utilização do Configurador de Tributos, a equipe fiscal deverá ser acionada.
