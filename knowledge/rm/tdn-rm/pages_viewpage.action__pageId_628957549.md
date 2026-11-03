---
content_hash: b8831439a5d6df4f5de01d2f8ec8ab13c7aef65ac433cc63531ce9e01c97f7b1
fetched_at: '2026-06-29T00:11:05.305729+00:00'
page_id: '628957549'
product: rm
source: tdn-rm
title: Nota Técnica nº 02/2021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628957549
version: 24
---

Objetivo:

Devido ao novo [Cronograma eSocial](https://www.in.gov.br/en/web/dou/-/portaria-conjunta-seprt/rfb/me-n-71-de-29-de-junho-de-2021-329487308) publicado no 29/06/2021 e a [Nota Técnica](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-0-02-2021.pdf) divulgada no dia 06/07/2021, adequamos o produto para atender o leiaute S-1.0, conforme liberações abaixo:

---

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2Alterações - 1a. LiberaçãoAlterações no sistema - Parte 1false

**A partir das Versões:**

* 12.1.29.283
* 12.1.31.199
* 12.1.32.136
* e Superiores.

Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:

1) S-1200 e S-2299: Campo {dia} – alteradas descrição e validação

**Observação:** Será gerado como zero a tag caso não tenha nenhum horário vinculado na convocação.

2) S-1200, S-2299 e S-2399: Campo {codRubr} – alterada validação.

**DE**: b) cuja natRubr em S-1010 seja igual a [1801, 9209, 9210, 9220], desde que perApur >= [2021-05] (se indApuracao = [1]) ou perApur >= [2021] (se indApuracao = [2]).

**PARA**: b) cuja natRubr em S-1010 seja igual a [1801, 9220], desde que perApur >= [2021-07] (se indApuracao = [1]) ou perApur >= [2021] (se indApuracao = [2]).

Será gerado erro caso tenha lançamento de um evento no envelope com as rubricas acima.

3) S-1200, S-2299 e S-2399: Campo {indApurIR} – alterada validação.

Informação obrigatória e exclusiva se perApur >= [2021-07] (se indApuracao = [1]) ou se perApur >= [2021] (se indApuracao = [2])

**Atenção:**Tag indApurIR só será gerada após essa data de apuração no sistema.

4) S-1299: Campo {indExcApur1250} – alterada validação

Não informar se perApur >= [2021-07] ou se indApuracao = [2]. Preenchimento obrigatório caso o campo tenha sido informado em fechamento anterior do mesmo período de apuração.

Menu RH | Folha de Pagamento | eSocial | Período de Apuração

Foi criado o campo "**Exclui informação sobre aquisições de produção Rural"**, ao selecionar esse campo o sistema irá gerar a nova tag <indExcApur1250> no evento S-1299.

**Importante:**Essa tag deverá ser enviada somente em caso de necessidade de exclusão ou retificação das informações enviadas de aquisição rural através do eSocial, ou seja, anterior a 19/07/2021.

As retificações  a partir de 19/07/2021 deverão ocorrer pelo evento **R-2055** no REINF.

**Exemplo:** Caso haja necessidade de uma exclusão/retificação das informações enviadas de aquisição rural no evento S-1250 dos períodos anteriores a competência 07/2021, deverá reabrir o período de apuração desejado (envio do evento S-1298) e após reenviar o evento S1299 com a tag <indExcApur1250>.

Mais informações sobre a alteração do S-1250 para o R-2055 acesse: [Gerar Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=506387467).

5) S-2200: Campo {dtIniCessao} – alterada validação da alínea c)

c) Se cadIni = [N], deve ser anterior à data da transferência ou alteração do CPF do empregado (sucessaoVinc/dtTransf ou dtAltCPF) e igual ou posterior a [2021-07-19]. Não informar se tpAdmissao = [1] ou se tpProv for diferente de [5, 8, 10].

6) S-2200, S-2205 e S-2300: Campo {tmpResid} – alterada validação

Preenchimento obrigatório quando houver trabalhador com (dtAdm ou dtExercicio ou dtInicio) no Registro de Eventos Trabalhistas - RET >= [2021-07-19].

7) S-2230: Grupo {perAquis} – alterada condição

 O (se codMotAfast = [15] E (o código de categoria no RET for igual a [1XX, 301, 302, 303, 304, 306, 307, 309, 310, 312, 410] com {tpRegTrab} em S-2200/S-2300 = [1] OU o código de categoria no RET for igual a [401] com tpRegTrab em S-2300 = [1] ou não informado) E dtIniAfast >= [2021-07-09]); N (nos demais casos)

 8) Tabela 03

Após a execução do atualizador no cadastro de eventos o campo natureza da rubrica será alterado:

1901- Juros e/ou atualização monetária

2903- Vestuário e equipamentos

1619- Ajuda compensatória - Programa Emergencial de Manutenção do Emprego e da Renda

6119- Indenização rescisória - Programa Emergencial de Manutenção do Emprego e da Renda

9) Tabela 16 – alterada descrição dos códigos [200020100, 200020300, 200020500, 200020700].

Após a execução do atualizador no campo fonte geradora na CAT as descrições serão:

200020100- Aprisionamento em, sob ou entre objetos em movimento convergente

200020300- Aprisionamento em, sob ou entre objeto parado e outro em movimento

200020500- Aprisionamento em, sob ou entre dois ou mais objetos em movimento

200020700 -Aprisionamento em, sob ou entre desabamento ou desmoronamento

10) Tabela 18

Após a execução do atualizador no DE/PARA de afastamentos do eSocial no parametrizador a descrição:

37- Suspensão temporária do contrato de trabalho nos termos do Programa Emergencial de Manutenção do Emprego e da Renda

11) Tabela 27

Após a execução do atualizador no campo procedimento as descrições:

1432- Exame oftalmológico com avaliação de retina e/ou cristalino

0530- ECG (Eletrocardiograma) convencional de até 12 derivações

0531- ECG (Eletrocardiograma) de alta resolução

0536- EEG (Eletroencefalograma) de rotina

0646- Gad-Ab-antidescarboxilase do ácido glutâmico

1098- Rotina (sumário) de urina.

Códigos **excluídos** que não devem ser visualizados:

0885- Métodos diagnósticos por imagem não especificados na tabela

1106- Sumário de urina

12) S-1200 e S-2299: Campo {tpAcConv} – incluída validação

13) S-2200 e S-2205: Campo {infoCota} – alterada validação

Preenchimento obrigatório e exclusivo se tpRegTrab = [1]. Somente pode ser informado [S] se pelo menos um dos campos a seguir estiver preenchido com [S]: defFisica, defVisual, defAuditiva, defMental, defIntelectual e reabReadap. Esta validação não deve ser realizada quando se tratar de evento enviado em versão do leiaute anterior a S-1.0.

3Alterações - 2a. LiberaçãoAlterações no sistema - Parte 2false

**A partir das Versões:**

* 12.1.29.299
* 12.1.31.218
* 12.1.32.153
* e Superiores.

14) S-1299: Campo {transDCTFWeb}

Menu RH | Folha de Pagamento | eSocial | Período de Apuração

Foi criado o campo "DCTFWeb -  Transmissão Imediata da DCTFWeb" ao selecionar esse campo o sistema irá gerar a nova tag <transDCTFWeb> no evento S-1299.

15) Tabela 01 – incluído código [501] - Dirigente sindical - Segurado especial 

Menu RH | Folha de Pagamento | Administração de Pessoal | Funcionário

Na Aba Registro liberado novo codigo de categoria

Ao gerar admissão do funcionário sistema gera o evento S-2300 com sucesso

Ao lançar envelope gera corretamente o evento S-1200
