---
article_id: 10658585102871
category: NFe - Nota Fiscal Eletrônica
content_hash: ecd842177983c322d82732bcdedee54ba910410f6dae38cc5edf593efdc11f8a
fetched_at: '2026-06-28T22:40:05.058992+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 495 Rejeição: CPF
  do Emitente com Série incompatível'
type: support-article
updated_at: '2025-06-30T19:19:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10658585102871-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-495-Rejei%C3%A7%C3%A3o-CPF-do-Emitente-com-S%C3%A9rie-incompat%C3%ADvel
---

**Dúvida**Como solucionar a 495 Rejeição: CPF do Emitente com Série incompatível  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

– Série difere da faixa para ***emitente CPF: 890-899 e 910-969***

***1. Criar**série da nota **890-899 e 910-969 para emitente com CPF conforme o link abaixo:***

Realize a verificação do parâmetro **MV\_TPNRNFS** desta Filial:

* Se estiver com conteúdo = 1, significa que seu controle de Numeração é realizado pela Tabela **SX5**;
* O correto é que a **SX5** seja exclusiva. Ou seja, cada Filial tenha a sua **SX5**. Ou em casos específicos, utilizar o Ponto de Entrada **CHGX5FIL** para trabalhar com **SX5** compartilhada de forma que, ao menos a Tabela 01 seja exclusiva.

**Procedimento para Criação da Serie:****1 -** Através do módulo **"Configurador" (SIGACFG)** siga o caminho:  
     Base de dados > Dicionário > Bases de Dados > Tabelas Genéricas;  
E na tabela 00 chave 01, SERIES DE N. FISCAIS.

**2 -** Altere manualmente, com a seta para baixo é possível incluir nova linha para registrar uma nova série/número que deseja iniciar;   
Para que sejam demonstrados (na Filial em questão) no momento de Preparar o Documento de Saída.

![20211227_162950.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33157177966615)

**3 -** Configure o parâmetro **MV\_ESPECIE**:MV\_ESPECIE: UNI=NF; 001=SPED   
Se faturar com a série UNI, a espécie da nota será NF, se faturar com série 001, a espécie da        nota será SPED e mediante esta espécie serão efetuados os tratamentos cabíveis de Fiscal, SPED PIS/COFINS e NFe.

**OBS**: Para **MDFe** não é necessário registrar o parâmetro **MV\_ESPECIE**, pois não é um documento que gera livro fiscal ou tem calculo de imposto.

Caso o limite de tamanho do parâmetro **MV\_ESPECIE** não atenda à necessidade, utilize a Tabela **SN** para substituir o **MV\_ESPECIE**.   
Se a numeração é exclusiva, então, - Tabelas **SF2** e **SD2** também devem estar com modo de acesso exclusivo.  
O ID nas tabelas **SPED** devem ser diferentes entre Filial e Matriz (Configurações da Rotina NFESEFAZ). Se necessário, consulte a Equipe de Suporte **SPED** / **TSS**.

**Saiba Mais:**

- **Criação de série de NFs para utilizar em Documentos de Saída:**<https://tdn.totvs.com/x/WU1tDQ>

- **Utilização da tabela SN (SX5) para cadastro de série/espécie de Nota Fiscal Saída (MV\_ESPECIE):**<https://tdn.totvs.com/x/zykmDg>

2. Após isso, ***exclua a nota e gere novamente.***

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10658474405399)
