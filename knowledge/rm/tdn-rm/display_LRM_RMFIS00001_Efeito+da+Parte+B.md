---
content_hash: 4298995cc03386fa859522411f4a6e0c7d59b3b6999a9441cb8a7ec4d496aad4
fetched_at: '2026-06-29T00:08:34.142924+00:00'
page_id: '274648271'
product: rm
source: tdn-rm
title: RMFIS00001_Efeito da Parte B
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_Efeito+da+Parte+B
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO FISCAL |
| **Versões:** | 12.1.16 |
| **Ocorrência:** | Efeito na Parte B |
| **Ambiente:** |  |
| **Passo a passo:** | **Efeito na Parte B**  *Exemplo de aplicabilidade:*  Vamos supor que a empresa realizou uma provisão de ações trabalhistas em janeiro de 2016. Então, lá na contabilidade, foi feito o seguinte lançamento:   * D – Provisões (Resultado) * C – Provisões (Passivo)                                360.000,00     **Primeiro momento:** adição do valor da provisão não dedutível para fins tributários.   1. Parametrização do Item Tributário referente à adição da provisão 2. Conferindo os valores: observe que no Anexo “Detalhamento da Apuração”, foi gerado o item com o valor para o primeiro trimestre: 3. Com o Período de Apuração encerrado, selecione o período e execute o processo “**Gerar Lançamentos Automáticos (Efeito na Parte B)**” 4. Todos os Itens Tributários parametrizados com algum efeito na Parte B do Lalur e que gerou valor na apuração serão apresentados na tela seguinte: 5. Selecione a conta que vai receber o lançamento ou crie uma nova. No nosso exemplo, vamos criar uma nova para aproveitar e dar algumas dicas quanto à correta inclusão da conta: 6. Ao finalizar a inclusão da conta, ela irá aparecer para seleção. Selecione e clique em “Ok”.           **IMPORTANTE!**   * Se o valor a ser controlado na Parte B for proveniente de uma **Adição** na Parte A:   + A conta da Parte B terá natureza de “**Exclusão**”. * Se o valor a ser controlado na Parte B for proveniente de uma **Exclusão** na Parte A:   + A conta da parte B terá Natureza de “**Adição**”. * Se for referente à **Prejuízo** apurado no período:  1. * A conta da parte B terá Natureza de “**Prejuízo Fiscal**”     7. Finalize o processo      8. Conferindo a Conta e o lançamento na Parte B:    Se for preciso reabrir os Período de Apuração, o sistema irá excluir os lançamentos criados.    Seguindo nosso exemplo, vamos imaginar que, em outubro de 2016, 50% da despesa provisionada foram efetivados e, portanto, deve-se baixar o saldo da conta, lá na Parte B do Lalur.  **Segundo momento:** reversão contábil da provisão e, por consequência, baixa do saldo na Parte B do Lalur.  Na contabilidade:   * D – Provisões (Passivo) * C – Disponibilidades (Ativo)                       180.000,00     9. No Evento Tributário, Grupo de Exclusões:   10. Conferindo a parametrização através da Simulação:          11. Veja que foi apurado Prejuízo Fiscal no 4º Trimestre do ano:            12. Depois de encerrar o Período de Apuração, execute o Processo “**Gerar Lançamentos Automáticos (Efeito na Parte B)**”.            13. Conferindo...        Todo esse processo gera efeito na rotina da Escrituração Contábil Fiscal – ECF, na geração dos Registros M300 e M350.  Os Registros M300 e M350, quando o Item Tributário estiver parametrizado para afetar a Parte B do Lalur através da constituição de saldo na conta ou da baixa do saldo da conta, serão gerados com o indicador de relacionamento “3 – Com Conta da parte B e Conta Contábil” (Campo 5 - IND\_RELACAO).  Serão gerados, também, registros “filhos” M305/M355 e M310/M360 contendo, respectivamente, a conta da Parte B que foi movimentada e a conta contábil, ambas parametrizadas no Item Tributário. |
| **Observações:** | **Caso a opção "Gerar Lançamentos Automáticos(Efeito na Parte B), não esteja disponível/visível, é devido a permissão do usuário/perfil. Acesse: Serviços Globais -> Segurança - Perfis - Selecione e edite o perfil do seu usuário no Sistema Gestão Fiscal -> [02] Obrigações Principais -> [02.02] Apuração ->  [02.02.01] Período de Apuração -> [02.02.01.09] Gerar Lançamentos Automáticos - Lalur B.** |
