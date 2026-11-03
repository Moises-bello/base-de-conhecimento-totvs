---
article_id: 36622113994135
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 31a391d88d5813de8da2f034b37c8de22de5b66f81911eb0f818e0c42b513974
fetched_at: '2026-06-28T22:39:56.310238+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Barueri/SP
  - Layout v4.2
type: support-article
updated_at: '2026-06-08T13:27:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36622113994135-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Barueri-SP-Layout-v4-2
---

**Dúvida**  
Quais são as informações montadas através dos Registro 4 e 5 no novo layout v4.2 da prefeitura de Barueri?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

| Campo | Obrigatório | Tipo | Tamanho | Posição Inicial | Posição Final | Observações / Instruções |
| --- | --- | --- | --- | --- | --- | --- |
| Enquadramento do Prestador do serviço no 'Simples Nacional' | S | Numérico | 1 | 2 | 2 | Descrição do campo e instruções de preenchimento alterados (vide no layout). |
| Regime de Apuração Tributária pelo Simples Nacional do Prestador do Serviço | S\* | Numérico | 1 | 3 | 3 | Descrição do campo e instruções de preenchimento alterados (vide no layout). |
| Código NBS | S | Numérico | 9 | 61 | 69 | Campo passou a ser obrigatório incondicionalmente. |
| Código indicador da operação de fornecimento | S | Numérico | 6 | 515 | 520 | Código conforme tabela de Código indicador da operação de fornecimento, disponível em: <https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc> |
| Código de Classificação Tributária do IBS e da CBS | S | Numérico | 6 | 521 | 526 | Código conforme tabela de Classificação Tributária (IBS / CBS). A tabela está disponível no portal indicado no documento: <https://dfe-portal.svrs.rs.gov.br/DFE/ClassificacaoTributaria> |
| Código de Situação Tributária IBS/CBS | S | Numérico | 3 | 527 | 529 | Indicar o código de situação tributária do IBS/CBS. Tabela de referência disponível no portal de Classificação Tributária indicado no documento. |
| Operação de uso ou consumo pessoal | S | Numérico | 1 | 530 | 530 | Indicar se a operação da NFS-e é de uso ou consumo pessoal. 0 = Não 1 = Sim. |
| Indicador do Destinatário do Serviço | S | Numérico | 1 | 531 | 531 | 0 – Destinatário é o próprio tomador/adquirente identificado na NFS-e (tomador = adquirente = destinatário);  1 – Destinatário não é o próprio adquirente (pode ser outra pessoa ou estabelecimento diferente do indicado como tomador) |

Documentação oficial: <https://www.barueri.sp.gov.br/nfe/Manuais/RPS_Layout-Novidades-v4.pdf?4321>   
Documentação do Produto sobre o Registro 5: <https://tdn.totvs.com/pages/releaseview.action?pageId=1058932213>   
  
**Atualizações**  
  
**TSS**  
Aplicação do patch no RPO do TSS: [12.1.2410](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1164047) ou [12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224026).  
  
Inclusão dos arquivos .CFG e .INI na pasta SYSTEM do TSS: [link.](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1077361)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38003535761047)  
  
**Pontos de Atenção**  
  
**1**: Deverá extrair da pasta 'Barueri-SP:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39401212713751)  
  
**2:** O arquivo **nfse\_3505708\_hom.cfg** contempla o novo layout da prefeitura, caso queira também enviar no novo layout em ambiente de produção, deverá realizar uma cópia desse arquivo e renomeá-lo de: nfse\_3505708\_hom.cfg para: nfse\_3505708.cfg e substituir o arquivo já existente na pasta, ficando os três arquivos atualizados:  
  
**nfse\_3505708.cfg** -> Utilizado para o ambiente de produção  
**nfse\_3505708\_hom.cfg** -> Utilizado para o ambiente de homologação  
**nfse\_3505708\_ini** -> Arquivo auxiliar utilizado para ambos os ambientes  
  
Inclusão do arquivo arquivo **tss\_nfse\_tipos\_v2.00.xsd** na pasta **SCHEMAS** do TSS: 12.1.2410: <https://r.totvs.io/p/1244003> ou 12.1.2510: <https://r.totvs.io/p/1243999>.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38003535765015)  
  
**[AMBIENTES COM TSS CLOUD COMPARTILHADO NÃO CONTEMPLAM ESSAS ATUALIZAÇÕES/CONFIGURAÇÕES da PMB004 - Versão PMB002 atualmente configurada].**  
  
**PROTHEUS**  
Aplicação do Expedição Continua no RPO:  
12.1.2410: [link para download](https://suporte.totvs.com/portal/p/10098/download#detail/1171486)  
12.1.2510: [link para download](https://suporte.totvs.com/portal/p/10098/download?e=1224039)  
  
Aplicação do Pacote Pontual e Compilação do rdmake NFSEXMLENV no RPO:  
12.1.2410: [link para download](https://r.totvs.io/p/1247193)  
12.1.2510: [link para download](https://r.totvs.io/p/1247194)  
  
**Observação**  
Para o Registro 4, é necessário também informar o Indicador de Operação: <https://tdn.totvs.com/pages/releaseview.action?pageId=1016684365>.
