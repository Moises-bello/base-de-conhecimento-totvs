---
article_id: 360016074472
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: a75b40931b61830c236db655c992c23c20635a32cc3a645db8f79335c8c948cb
fetched_at: '2026-06-28T22:42:05.360858+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar o registro F100 por Documentos de Entrada
type: support-article
updated_at: '2025-11-18T20:41:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016074472-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F100-por-Documentos-de-Entrada
---

**Dúvida**Como gerar o registro F100 por documentos de Entrada?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
 **Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Crie no **Configurador** na **Tabela Genérica 42** uma espécie de documento.  
Exemplo: ND - NOTA DE DESPESA;  
  
2. Informe a espécie criada no parâmetro **MV\_DOCSPD**Exemplo: **MV\_DOCSPD**=ND  
Observação:  
Caso utilize mais de uma espécie no parâmetro a separação será por "BARRA"  
Exemplo: **MV\_DOCSPD** = ND/REC/BOL;  
  
3. Verifique o conteúdo do parâmetro   
**MV\_2DUPNAT**=**SA2**->**A2\_NATUREZ**;  
  
4. Crie a natureza, preencha os campos:  
Apur. Pis (**ED\_APURPIS**)=Crédito;  
Apur. Cofins (**ED\_APURCOF**)=Crédito;  
% Ap. PIs (**ED\_PCAPPIS**) = 1,65;  
% Ap. Cofins (**ED\_PCAPCPF**) = 7,60;   
Tipo Naturez (**ED\_TIPO**)= 2 Analítico;  
Cond Naturez (**ED\_COND**) = Despesa;  
Tp Reg (**ED\_TPREG**) = Não cumulativo;   
CST Cofins (**ED\_CSTCOF)** = 50 a 66;  
CST Pis (**ED\_CSTPIS**) = 50 a 66;  
Ind Cmulat (**ED\_INDCMLT**) = Não cumulativo.  
  
**Observação:** Para preenchimento do campo **15 NAT\_BC\_CRED** do registro **F100**, preencha campo da **Natureza preenchido (campo ED\_CLASFIS)** o registro alimentará o título da **SE2** e o campo **CL2\_CODBCC** da tabela **CL2**.  
  
5. Crie uma **TES**:  
Livro fiscal ICMS/IPI/ISS (**F4\_LFICM**) = Não -> Não deverá ser gerado livro, pois a nota não tem escrituração fiscal "Para não gerar C100";  
Gera Duplic. (**F4\_DUPLIC**) = Sim;  
Calcula Pis e Cofins (**F4\_PISCOF**) = Ambos;   
Credito de Pis/Cofins (**F4\_PISCRED**)= Credita;   
Sit Trib Pis (**F4\_CSTPIS**) = Igual CST informado na Natureza;   
Sit Trib Cof (**F4\_CSTCOF**) = Igual CST informado na Natureza.  
  
6. Gere uma nota com a espécie criada;  
  
7. Processe a apuração da **EFD Contribuições**, de acordo com as perguntas da *Wizard* abaixo:  
**Livro = asterisco (\*);**  
**Tributos: 1 - PIS/COFINS ou 3 - PIS/COFINS/CPRB;**  
**Regime PIS COFINS: 1 - N. Cumul.Comp , 2 - Cumulativo ou 4 -Não cumulativo/Cumulativo;**  
**Opção Gravação = 1 - Agrupada;**  
**Cód. Receita Demais Operações;**  
**Indicador Natureza PJ = ? Exemplo -> 00 - Pessoa Jurídica em geral (Não participante SCP);**  
**Indicador Regime Cumulativo = 1 - Consolidado ou 2 - Individualizado.**  
  
8. Gere o arquivo **EFD Contribuições**, de acordo com as perguntas da *Wizard* abaixo:   
**Livro = asterisco (\*);**  
**Regime PIS/COFINS = 1 - N. Cumulativo, 2 - Cumulativo ou 3 - N. cumulativo/Cumulativo;**  
**Indicador Situação Especial = ? Exemplo -> 0 - Abertura;**  
**Indicador Natureza PJ = ? Exemplo -> 00 - Pessoa Jurídica em geral (Não participante SCP);**  
**Atividade Preponderante =? Exemplo -> 0 - Industria ou Equiparado Industrial;**  
**Indicador Regime Cumulativo = 9 - Competência Detalhada;**  
**Indicador NFE/Cupom = 2 -Individualizado.**  
  
**Observação:**  
Caso essas perguntas não estejam preenchidas o sistema não alimentará a tabela **CL2** e consequentemente os registros **F100** não serão gerados.  
A tabela **CL2** é gerada após o processamento da **Apuração do EFD Contribuições**.
