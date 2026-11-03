---
article_id: 11117348172311
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: efda6c99327d9a3f3a6396d5fe3a00feb39db03137753f6b8474691a8bf27ea8
fetched_at: '2026-06-28T22:42:11.879337+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - GIA-SP - Tabela 3, CR=10, Campo
  CFOP_X_Q14 INVÁLIDO, Posição 3_X_114.
type: support-article
updated_at: '2024-06-04T14:41:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11117348172311-Cross-Segmentos-Backoffice-Protheus-TAF-GIA-SP-Tabela-3-CR-10-Campo-CFOP-X-Q14-INV%C3%81LIDO-Posi%C3%A7%C3%A3o-3-X-114
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:2:00 min**Ocorrência:**Na validação da **GIA SP** ocorre o erro: **Erro Tabela 3, CR=10, Campo CFOP\_X\_Q14 INVÁLIDO, Posição 3\_X\_114**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF – Nova GIA –  A partir da versão 12.1.27

**Causa**O erro ocorre pois foi gerado o registro **CR=10** com **CFOP** interestadual e não foi gerado o registro **CR=14****– Detalhes Interestaduais**.   
  
**Solução**  
Para solucionar o incidente siga o procedimento abaixo para corrigir o erro de validação na **GIA-****SP** registro **CR=10** e **CR=14**:

1. Identifique o **CFOP** que está ocorrendo essa situação. O mesmo consta na **posição 03** até a **posição 06** da linha informada na mensagem de erro;
2. Depois, identifique as NF de entrada ou saída referente a esse **CFOP** e então verifique a **UF** informado nas tabelas **SFT/SF3** campo **FT\_ESTADO** e **F3\_ESTADO**, a **Unidade de Federação** deve ser diferente da **UF = SP** da empresa que está gerando o arquivo da **GIA-SP**, pois este **CFOP** é para entrada ou saída para fora do estado, grupo de **CFOPs**  2 e 6 relativas às entradas e saídas interestaduais.  
     
   **Manual da GIA-SP - Registro CR=14 – Detalhes Interestaduais - pagina 17**.  
     
   <https://portal.fazenda.sp.gov.br/servicos/gia/Downloads/pre_formatado_ngia_v0210_gia0801.pdf>
3. Após ajustes, realize novamente a **integração no TAF**;
4. Acesse a **Central de Obrigações (TAFOBRIG)**, e gere novo arquivo da **GIA-****SP** e valide novamente, o erro de validação não será mais apresentado.  
     
   Caso identifique o campo **C20\_UF** em branco, edite a NF no **TAF** e preencha esse campo. Caso identifique os campos **C1H\_UF** ou **C1H\_CODMUN** em branco, acesse o cadastro desse Participante no **TAF** e preencha os campos.

Caso os campos do **Cadastro de Clientes/Fornecedores** estejam em branco na origem, preencha também para evitar que o erro ocorra em novas integrações.

Caso as inconsistências persistam após as validações, abra uma solicitação para o Suporte da TOTVS.
