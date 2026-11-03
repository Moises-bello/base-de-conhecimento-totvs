---
content_hash: 509e73662b31efbf90b78c140d680a7a52bd01955416aeaa4ad3865213c272bd
fetched_at: '2026-06-29T00:09:34.039703+00:00'
page_id: '425459121'
product: rm
source: tdn-rm
title: Geração de Movimento para Inscrições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459121
version: 22
---

Este processo tem objetivo de realizar a geração, regeração, cancelamento ou exclusão de um movimento do TOTVS Gestão de Estoque, Compra e Faturamento referente ao serviço de inscrição no TOTVS Processo Seletivo.   
O acesso à esta funcionalidade pode ser feito através da tela de cadastro de Processos Seletivos ou anexo dos candidatos inscritos.

false⚠️ ATENÇÃO: ADEQUAÇÃO À REFORMA TRIBUTÁRIA (Vigência 01/01/2026)

Em conformidade com a **Reforma Tributária (EC 132/2023)** e regulamentações complementares, alertamos que a partir de **1º de Janeiro de 2026** inicia-se a fase de transição com a cobrança dos novos tributos **IBS** (Imposto sobre Bens e Serviços) e **CBS** (Contribuição sobre Bens e Serviços).

Para garantir a conformidade fiscal e o correto funcionamento da integração **TOTVS Educacional x Backoffice** neste novo cenário, é imprescindível a validação dos seguintes **impactos imediatos e pontos de atenção**:

1. **Cadastros Base da Reforma** Realize os cadastros fiscais estruturais conforme detalhado na documentação técnica de referência. 📄 **Acesse:** [Guia de Cadastros Base - Reforma Tributária](https://tdn.totvs.com/pages/viewpage.action?pageId=925352283)
2. **Parametrização da Regra Tributária** Foi incluído no parâmetros de integração com o Gestão de Estoque Compras e Faturamento um campo para preenchimento da **regra tributaria** [Guia de Parametrização](https://tdn.totvs.com/pages/viewpage.action?pageId=425458275&draft=true)
3. **Destinatário do Serviço:** Do Candidato, torna-se obrigatória a correta informação dos campos **Nome**, **Nacionalidade** e **Endereço completo**. Adicionalmente, o **CPF** será exigido sempre que a nacionalidade estiver definida como **brasileira**.

   1. **Impacto:** Estes dados são utilizados para identificar o **Local da Operação** e preencher os **dados do destinatário/tomador do serviço**. A ausência dessas informações causará rejeição na transmissão da nota. 📄 **Acesse:** [Destinatário do Serviço](https://tdn.totvs.com/pages/releaseview.action?pageId=1012511875)

      false📩 Envio de Dados do Destinatário do Serviço

      **1. Quando o módulo Processo Seletivo está configurado para enviar os dados do Responsável Financeiro** na integração com o Gestão de Estoque Compras e Faturamento: O envio dependerá exclusivamente da opção selecionada no momento da execução do processo:

      * **Parâmetro Marcado:** Se a opção *"Envia dados do destinatário do serviço"* estiver marcada no processo de geração, os dados **serão enviados** para o movimento.
      * **Parâmetro Desmarcado:** Se a opção estiver desmarcada, os dados **não serão enviados**.

      **2. Quando o módulo está configurado para enviar os dados do Candidato:**

      * **Para todos os cenários:** Os dados do Destinatário do Serviço **nunca** serão enviados para o movimento, independentemente de qualquer outra marcação.
      > **Resumo de Regra:** As informações do destinatário do serviço só são transmitidas se o módulo do Processo Seletivo estiver parametrizado para usar o *Responsável Financeiro* e o usuário ativar explicitamente a opção durante a *Geração do Movimento*.

      **Patches disponíveis:** 12.1.2506.308 · 12.1.2510.234 · 12.1.2602.149

      A partir dos patches 12.1.2506.299 · 12.1.2510.224 · 12.1.2602.142 , os dados do destinatário do serviço serão enviados apenas nos casos em que o aluno e o responsável financeiro **não forem a mesma pessoa**.
4. **Local da Operação**

   1. Áreas Ofertadas com o parâmetro `usa local de prova online` **marcado**, o local da operação enviado será o município do endereço do candidato
   2. Áreas Ofertadas com o parâmetro `usa local de prova online` **desmarcado**, o local da operação enviado será o município do endereço da Filial

Atenção

Nas versões iguais ou superiores a **12.1.2502.292, 12.1.2506.262, 12.1.2510.181 e 12.1.2602.105**foi disponibilizado um ajuste contemplando o envio do **Código Indicador da Operação,** campo obrigatório para envio da NFS-e considerando as regras de envio do Layout Nacional

O preenchimento do campo no movimento para exibição na Nota será feito respeitando a seguinte regra:

* Local prova online da área ofertada estiver desmarcado: Preenche com **030101** (Estabelecimento do fornecedor)
* Local prova online da área ofertada estiver marcado: Preenche com **030102** (Local diverso do estabelecimento do fornecedor)

📅 As alterações sistêmicas e validações abaixo serão aplicadas exclusivamente para **documentos emitidos a partir de 01/01/2026**. Certifique-se de que seu ambiente esteja atualizado para as **versões iguais ou superiores** a: **12.1.2502.262**, **12.1.2506.222** e **12.1.2510.151**

A partir das versões **12.1.2502.268, 12.1.2506.229 e 12.1.2510.158,** foi implementado o parâmetro **'Validar campos do layout nacional'** no processo de geração de movimento. Quando desmarcado, o sistema não exigirá o preenchimento dos campos obrigatórios do layout nacional. Vale ressaltar que este parâmetro será descontinuado assim que o governo tornar obrigatório o destaque do **IBS e CBS** na NFS-e.

**Importante**: Para que seja possível executar este processo é preciso que a integração esteja habilitada nos .  
Durante a execução do processo será possível realizar:

* Geração/Regeração de Movimentos: Gera o movimento baseado no boleto da inscrição e/ou regera caso já exista e o processo esteja parametrizado. Neste passo do processo será possível definir:

1. O tipo de movimento.   
2. A data de emissão do movimento   
3. Caso queira selecionar um dia fixo do mês que esteja entre a emissão e o vencimento do lançamento, preencha "Dia fixo relacionado ao mês\ano da data de emissão do movimento.  
4. Se permite regeração de movimentos, caso haja a necessidade de atualizar os movimentos já gerados. Desmarque caso só tenha a necessidade de gerar novos movimentos.  
5. Se gera movimentos para boletos de valor líquido zero caso seja desejável emitir movimentos para lançamentos com 100% de desconto.

* Exclusão de Movimentos: Exclui todos os movimentos relacionados as inscrições selecionadas, sejam ativos ou cancelados.
* Cancelar Movimentos: Cancela o movimento ativo de cada inscrição selecionada.

 Veja também

---

[Boletim Técnico - Geração de Movimentos](http://tdn.totvs.com/display/rm/EDUPS_BT_GeracaoMovimento_REQ000187.pdf)
