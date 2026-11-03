---
article_id: 360047351593
category: eSocial - Cadastros
content_hash: 646b92602c694b9dcded90dd6862f9c341a615e53a04004639abc5135e49cdec
fetched_at: '2026-06-28T22:47:14.588972+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RM - eSocial - MP 936 - Cadastro e geração do Benefício Extraordinário Mensal
  - B.E.M.
type: support-article
updated_at: '2022-12-06T15:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047351593-RM-eSocial-MP-936-Cadastro-e-gera%C3%A7%C3%A3o-do-Benef%C3%ADcio-Extraordin%C3%A1rio-Mensal-B-E-M
---

**Dúvida**  
Como realizar o cadastro do **Benefício Extraordinário Mensal** (B.E.M.) e a geração do relatório para importação no sistema **Empregador Web**?  
  
**Ambiente**  
RM - eSocial - A partir dos *Patches*12.1.25.268, 12.1.26.213, 12.1.27.166 e 12.1.28.102  
  
**Solução**  
Para o recebimento do **Benefício Emergencial**, caberá ao empregador informar o Ministério da Economia a redução da jornada de trabalho e de salário, ou a suspensão temporária do contrato de trabalho, no prazo de dez dias a contar da data do acordo individual ou coletivo.

O Benefício Emergencial de Preservação do Emprego e da Renda (**B.E.M.**) será pago quando houver acordos entre trabalhadores e empregadores nas situações de:  
      - redução proporcional de jornada de trabalho e de salário;  
      - suspensão temporária do contrato de trabalho.

• **Cadastro do B.E.M.**  
Para cadastrar o B.E.M. siga os passos abaixo:

1. No módulo TOTVS Folha de Pagamento acesse o menu **Administração de Pessoal | Funcionários**;  
2. Edite o funcionário em desejado e acesse o menu lateral **Informações Contratuais | Registro**;  
3. Selecione a aba **B.E.M** e preencha as informações.

Veja abaixo detalhes sobre cada campo do cadastro:

![](https://tdn.totvs.com/download/attachments/545641381/image2020-4-15_11-5-38.png?version=1&modificationDate=1586959538187&api=v2)

**Tipo de adesão**: Irá receber o tipo de redução, podendo ser **Suspensão de Contrato** ou **Redução de Jornada**.  
**Data do acordo**: Irá receber a data do acordo da redução jornada/salário.  
**Percentual de Redução da Jornada**: Irá receber o percentual utilizado para redução de jornada/salário.  
**Dias de duração do acordo**: Irá receber a quantidade de dias que irá durar a redução de jornada. Este campo não limita a quantidade estabelecida na MP, ficando a cargo do usuário observar as regras para preenche-lo.  
**Valor Reduzido**: Irá receber o salário que foi reduzido: Exemplo: funcionário com salário de R$ 2000,00 e teve a redução de 25%. Este campo recebe o valor de R$ 500,00. Caso o tipo de recebimento do funcionário seja **H - Horista** ou **P - Horista (Professor)**, deverá deixar o campo zerado.

• **Geração do arquivo B.E.M.**  
Para gerar o arquivo B.E.M, foi disponibilizado pela TOTVS o **Layout B.E.M (versão Oficial).TotvsGen** conforme a especificação do Ministério da Economia e do Trabalho, que deve ser gerado pelo recurso **Gerador de Saídas**.   
Siga os passos abaixo para geração do arquivo:

1. Para fazer a importação do layout acesse **Gestão | Gerador de Saídas | Processo | Importar Layout**;  
1.1. Na tela que será aberta, clique em **Adicionar Objetos**;  
1.2. Busque pelo arquivo **Layout B.E.M (versão Oficial).TotvsGen** que por padrão se encontra na pasta **TOTVS\CorporeRM\ObjetosGerenciais\Layout** e execute o processo;  
2. Após a importação, para gerar o arquivo selecione o layout, clique em **Processo | Geração de Saídas**.   
2.1. Na etapa **Seleção do Layout** informe o layout importado na etapa 1 e o diretório de destino onde o arquivo será salvo;  
2.2. Na próxima etapa, informe o tipo de inscrição, fórmulas para remuneração e filtro de usuário;  
2.3. Execute o processo para geração.

Conforme a especificação do governo, o sistema do **Empregador Web** ao qual o arquivo deve ser importado só aceita arquivos na **extensão .csv**. Desta forma, veja abaixo como alterar a extensão do arquivo:

1. Abra o arquivo no bloco de notas, e selecione **Arquivo | Salvar como**;  
2. Na tela que será aberta, selecione no campo **Tipo** a opção **Todos os arquivos (\*.\*)**;  
3. Altere o final do nome do arquivo de **.txt** para **.csv**.

**Importante**  
Os dados relacionados ao cadastro do B.E.M. serão mantidos em históricos e poderão ser acessados pelo anexo **Históricos | Histórico de Adesão ao Benefício Extraordinário Mensal B.E.M.**. É necessário liberar permissão no módulo **Serviços Globais**, menu **Segurança | Perfis** para visualização do histórico.

O cadastro do B.E.M. **não irá alterar os valores de salário e jornada do cadastro do funcionário** pois outros processos do sistema utilizarão o salário cheio para processamento. Os dados da redução serão apresentados **somente no XML e no histórico** do B.E.M..  
  
**Saiba mais**  
Para consultas modelos de fórmulas e outras informações importantes sobre o processo do B.E.M, acesse:  
      • [MP 936 - Benefício Extraordinário Mensal](https://tdn.totvs.com/pages/releaseview.action?pageId=545641381)   
      • [Manual de Leiaute do Arquivo B.E.M](https://sd.mte.gov.br/sdweb/validador/Manual_EmpregadorWeb_BEM.pdf)
