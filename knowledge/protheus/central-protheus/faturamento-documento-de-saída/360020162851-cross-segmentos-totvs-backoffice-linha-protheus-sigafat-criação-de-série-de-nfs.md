---
article_id: 360020162851
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: be8a7c4d798451fd65b349b7ba6945db55bb768f9bd86f7d4b06c49d817b1688
fetched_at: '2026-06-28T22:38:45.105213+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos -TOTVS Backoffice (Linha Protheus) - SIGAFAT - Criação de série
  de NFs para utilizar em Documentos de Saída
type: support-article
updated_at: '2025-05-21T14:39:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020162851-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-de-s%C3%A9rie-de-NFs-para-utilizar-em-Documentos-de-Sa%C3%ADda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Criação de série de NFs para utilizar em Documentos de Saída.  
  
**Ambiente**Cross Segmentos -TOTVS Backoffice (Linha Protheus)-SIGAFAT- Todas as versões.  
  
**Solução**Realize a verificação do parâmetro **MV\_TPNRNFS** desta Filial:

* Se estiver com conteúdo = 1, significa que seu controle de Numeração é realizado pela Tabela **SX5**;
* O correto é que a **SX5** seja exclusiva. Ou seja, cada Filial tenha a sua **SX5**. Ou em casos específicos, utilizar o Ponto de Entrada **CHGX5FIL** para trabalhar com **SX5** compartilhada de forma que, ao menos a Tabela 01 seja exclusiva.

**Procedimento para Criação da Serie:****1 -** Através do módulo **"Configurador" (SIGACFG)** siga o caminho:  
     Base de dados > Dicionário > Bases de Dados > Tabelas Genéricas;  
E na tabela 00 chave 01, SERIES DE N. FISCAIS.

**2 -** Altere manualmente, com a seta para baixo é possível incluir nova linha para registrar uma nova série/número que deseja iniciar;   
Para que sejam demonstrados (na Filial em questão) no momento de Preparar o Documento de Saída.

![20211227_162950.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4417229738647/20211227_162950.gif)

**3 -** Configure o parâmetro **MV\_ESPECIE**:MV\_ESPECIE: UNI=NF; 001=SPED   
Se faturar com a série UNI, a espécie da nota será NF, se faturar com série 001, a espécie da        nota será SPED e mediante esta espécie serão efetuados os tratamentos cabíveis de Fiscal, SPED PIS/COFINS e NFe.

**OBS**: Para **MDFe** não é necessário registrar o parâmetro **MV\_ESPECIE**, pois não é um documento que gera livro fiscal ou tem calculo de imposto.

Caso o limite de tamanho do parâmetro **MV\_ESPECIE** não atenda à necessidade, utilize a Tabela **SN** para substituir o **MV\_ESPECIE**.   
Se a numeração é exclusiva, então, - Tabelas **SF2** e **SD2** também devem estar com modo de acesso exclusivo.  
O ID nas tabelas **SPED** devem ser diferentes entre Filial e Matriz (Configurações da Rotina NFESEFAZ). Se necessário, consulte a Equipe de Suporte **SPED** / **TSS**.

**Saiba Mais:**

- **Criação de série de NFs para utilizar em Documentos de Saída:** <https://tdn.totvs.com/x/WU1tDQ>

- **Utilização da tabela SN (SX5) para cadastro de série/espécie de Nota Fiscal Saída (MV\_ESPECIE):** <https://tdn.totvs.com/x/zykmDg>
