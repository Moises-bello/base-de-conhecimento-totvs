---
article_id: 4403785079831
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e051beb3394f59f351247bc242366d16e285f5b0666bd41ad40871a9f4901b45
fetched_at: '2026-06-28T22:38:30.022751+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de entrada
  na rotina "Parcerias (FATA400)"
type: support-article
updated_at: '2023-01-23T13:33:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403785079831-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-na-rotina-Parcerias-FATA400
---

**Dúvida**Quais são os pontos de entrada na rotina de **Contrato de Parceria** (FATA400)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões  
  
**Solução**

Os pontos de entrada da rotina de **Contrato de Parceria** (**FATA400**) são:

1. **FT400FIL** - Adiciona Filtro para registros no início da Função **- <https://tdn.totvs.com/x/boRn>**
2. **FT400COR** - Permite realizar alterações nas cores do *browse* do cadastro, representando o *status* do contrato. - **<https://tdn.totvs.com/x/wYgbCQ>**
3. **FT400CLOSE** - Ponto de entrada executado ao fechar contrato de parceria. - **<https://tdn.totvs.com/x/VgPMCg>**
4. **FT400DEL** - Validar a exclusão de um contrato de parceria - **<https://tdn.totvs.com/x/M5EbCQ>**
5. **FT400VCP** - Tela do contrato de parceria - **<https://tdn.totvs.com/x/GYZn>**
6. **FT400LOK** - Executado na validação da linha **- <https://tdn.totvs.com/x/coRn>**
7. **FT400TOK** - Valida confirmação da operação - **<https://tdn.totvs.com/x/dYRn>**
8. **FT400AGR -**Executa processamento antes de iniciar gravação - **<https://tdn.totvs.com/x/a4Rn>**
9. **FT400GRV -** Possibilita gravação de dados - **<https://tdn.totvs.com/x/b4Rn>**
10. **FT400BAR -** Inclui opções do usuário - **<https://tdn.totvs.com/x/bIRn>**
11. **FT400LEG** - Permite a adição de mais legendas caso seja necessário, de acordo com a regra do cliente - [**https://tdn.totvs.com/x/pwmDC**](https://tdn.totvs.com/x/pwmDC)
12. **FT400CON** -  Informar número do contrato - **<https://tdn.totvs.com/x/_YVn>**
13. **FT400VAL** - Valida preenchimento do aHeader - **<https://tdn.totvs.com/x/doRn>**
14. **FT400CAB** - Efetua alteração ou inclusão de dados nas variáveis -  **<https://tdn.totvs.com/x/bYRn>**
15. **FT400VLC** - Início do preenchimento do aCols **- <https://tdn.totvs.com/x/d4Rn>**
16. **FT400LIN** - Possibilita manipulação das informações - **<https://tdn.totvs.com/x/cYRn>**
17. **FT400PED** - Antecede gravação do pedido de Venda - **<https://tdn.totvs.com/x/dIRn>**
18. **FT400LIB** - Pós gravação do pedido de venda - **<https://tdn.totvs.com/x/cIRn>**
19. **FT400FLT**- Adição de filtro para Contrato - **<https://tdn.totvs.com/x/Q4Zn>**
20. **FT400MNU**- Insere novas opções no array aRotina - **<https://tdn.totvs.com/x/c4Rn>**
