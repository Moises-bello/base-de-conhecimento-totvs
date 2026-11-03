---
content_hash: 5ea850bad776e9c4d566b61f5b85a97c6bbebcfffbc9093803a1ac92ca5d44c7
fetched_at: '2026-06-29T00:11:06.029592+00:00'
page_id: '63275428'
product: rm
source: tdn-rm
title: RMCTB00007_Importação do Plano de Contas Referencial - Layout 2.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63275428
version: 3
---

|  |  |  |
| --- | --- | --- |
|  | **Produto:** TOTVS Gestão Contábil   **Versão:** 10.80 ou superior   **Processo:** Importação do Plano Referencial   **Sub-Processo:** SPED Contábil – SPED FCONT     ***Introdução***     Processo referente à Importação, Associação e Validação do 'Plano Referencial' para geração do SPED Contábil e (ou) SPED FCONT.       ***Desenvolvimento do Procedimento***     **Importação do Plano Referencial:**     1. Acesse 'Utilitários' / 'Conversões' / 'Importação por texto';   2. Na guia 'Arquivos' informe o diretório do arquivo do Plano de Contas Paralelo;   3. Na guia 'Parâmetros' informe no campo tamanho do código da conta o valor 40;   4. Na guia 'Plano de Contas Paralelo' preencha o código a descrição e a máscara de conforme o maior nível do plano referencial (ex: #.##.##.##.##.##.##);   5. 'Importar'.          **Associação do plano de contas Contábil com o Plano de contas da Referencial:**  1. Acesse 'Cadastros' / 'Plano de Contas Paralelo';  2. Selecione o Plano de Contas em questão;  3. 'Anexos' / 'Contas Paralelas';  4. Filtre e edite a Conta Referencial em questão;   5. Utilize as guias 'Associação do Plano Contábil' e 'Associação com Centro de Custo' para realizar a associação com a Conta Paralela editada.  **Validação do Plano de Contas Paralelo:**  1. Acesse 'Cadastros' / 'Plano de Contas Paralelo';  2. Selecione o Plano de Contas em questão;  3. 'Processos' / 'Validação da Associação do Plano Paralelo para o SPED Contábil'.    **Cópia de Associações:** Caso tenha realizado as associações entre o plano referencial e contábil no ano base anterior e deseja manter estas associações, é orientado realizar o seguinte procedimento, após a importação:  1. 'Cadastros' / 'Plano de Contas Paralelo';   2. Selecione o plano novo e acesse 'Processos' / 'Cópia de Associações do Plano Paralelo';   3. Indique o Plano Paralelo de Origem;   4. Indique o Plano Paralelo de Destino.     Vale ressaltar que caso uma ou mais Contas Contábeis não sejam efetivamente vinculadas, será necessário realizar o vínculo do 'Plano de Contas Contábil' com o 'Plano de Contas da Referencial', conforme processo citado anteriormente  ***Informações Adicionais:***     Os 'Campos', 'Anexos' e 'Processos' citados são definidos no perfil associado ao usuário.Observação: 'Cadastros' / 'Segurança' / 'Perfis' / 'Acesso a Menus' / 'RM Saldus' / 'Cadastros' / 'Plano de Contas Paralelo' |  |
