---
article_id: 360016144171
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 6482bebfd368a67edf17837b0ecd6b14b8022207a9e395750005a008ce9afd4c
fetched_at: '2026-06-28T22:42:05.366886+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar o registro F100 por Documentos de Saída
type: support-article
updated_at: '2022-09-15T21:34:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016144171-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F100-por-Documentos-de-Sa%C3%ADda
---

**Dúvida**Como gerar o registro F100 por documentos de Saída?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Crie no **Configurador** na **Tabela genérica 42** uma espécie de documento  
Exemplo: ND NOTA DE DESPESA;  
  
2. Crie uma Série na **Tabela genérica 01** do **Configurador.**Exemplo -> 999  
  
3. Vincule a série (criada na **Tabela 01**) a espécie (criada na **Tabela 42**) no parâmetro **MV\_ESPECIE.**Exemplo: **MV\_ESPECIE**: 999=ND;  
  
4. Informe a série no parâmetro **MV\_DCSSPD.**Exemplo: **MV\_DCSSPD**=999. Observação: Caso utilize mais de uma série no parâmetro a separação será por "BARRA". Exemplo: **MV\_DCSSPD**=999/022/A;  
  
5. Verifique o conteúdo dos parâmetros que devem estar preenchidos conforme abaixo;  
**MV\_1DUPREF** = **SF2**->**F2\_SERIE** -> Padrão para considerar as séries do parâmetro **MV\_ESPECIE**.  
**MV\_1DUPNAT** = **SA1**->**A1\_NATUREZ** ou **SC5**->**C5\_NATUREZ**Lembrando que se o conteúdo do parâmetro **MV\_1DUPNAT** = SC5->**C5\_NATUREZ** deverá ser informado natureza no pedido de venda campo Natureza **C5\_NATUREZ**6. Crie a natureza, preencha os campos:  
Apur. Pis (**ED\_APURPIS**)=DEBITO;  
Apur. Cofins (**ED\_APURCOF**)=DEBITO;  
% Ap. PIs (**ED\_PCAPPIS**) = 1,65;  
% Ap. Cofins (**ED\_PCAPCOF**) = 7,60;  
Tipo Naturez (**ED\_TIPO**) = 2 - Analítico;  
Cond Naturez (**ED\_COND**) = Receita;  
Tp Reg (**ED\_TPREG**) = Não cumulativo;  
CST Cofins (**ED\_CSTCOF**) = 01;  
CST Pis (**ED\_CSTPIS**)= 01;  
Ind Cmulat (**ED\_INDCMLT**) = Não cumulativo.  
  
7. Crie o TES:  
O TES não fara escrituração de nenhum livro fiscal:  
Livro fiscal ICMS/IPI/ISS = Não -> Não deverá ser gerado livro pois a nota não tem escrituração fiscal "Para não gerar C100";  
Gera Duplic. **(F4\_DUPLIC)** = SIM;  
Calcula Pis e Cofins **(F4\_PISCOF)** = Ambos;  
Credito de Pis/Cofins **(F4\_PISCRED)**= Debita;   
Sit Trib Pis **(F4\_CSTPIS)** = Igual informado Natureza;   
Sit Trib Cof **(F4\_CSTCOF)** = igual informado na natureza.  
  
8. Fature a nota fiscal com a série criada na tabela 01 conforme orientação 2 para ser vinculado a espécie criada na tabela 42;  
  
9. Processe apuração da EFD Contribuições;  
Geração da apuração -> Perguntas da Wizard que devem estar preenchidas.  
Livro = asterisco (\*);  
Tributos: 1 - PIS/COFINS ou 3 - PIS/COFINS/CPRB;  
Regime PIS COFINS: 1 - N. Cumul.Comp , 2 - Cumulativo ou 4 -Não cumulativo/Cumulativo;  
Opção Gravação = 1 - Agrupada;  
Cod. Receita Demais Operações = ?;  
Indicador Natureza PJ = ? Exemplo -> 00 - Pessoa Jurídica em geral (Não participante SCP);  
Indicador Regime Cumulativo = 1 - Consolidado ou 2 - Individualizado.  
  
10. Gere o arquivo **EFD Contribuições** na última opção do sub - menu da rotina **FISA001;**  
Geração do arquivo da EFD Contribuições -> Perguntas da Wizard que devem estar preenchidas.  
Livro = asterisco (\*);  
Regime PIS/COFINS = 1 - N. Cumulativo, 2 - Cumulativo ou 3 - N. cumulativo/Cumulativo;  
Indicador Situação Especial = ? Exemplo -> 0 - Abertura;  
Indicador Natureza PJ = ? Exemplo -> 00 - Pessoa Jurídica em geral (Não participante SCP);  
Atividade Preponderante =? Exemplo -> 0 - Industria ou Equiparado Industrial;  
Indicador Regime Cumulativo = 9 - Competência Detalhada;  
Indicador NFe/Cupom = 2 -Individualizado.  
  
Importante: Caso essas perguntas não estejam preenchidas o sistema não alimentará a tabela CL2 e consequentemente os registros F100 não serão gerados.

Anexo, vídeo do processo.
