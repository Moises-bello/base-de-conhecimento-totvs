---
content_hash: c378b18e30aeae272ab0ad6a4759f340eccfa5086f99f721ce1cbc5facc26724
fetched_at: '2026-06-29T00:09:21.758215+00:00'
page_id: '422545896'
product: rm
source: tdn-rm
title: Antes de Gerar o Arquivo Texto da ECF
type: documentation
url: https://tdn.totvs.com/display/LRM/Antes+de+Gerar+o+Arquivo+Texto+da+ECF
version: 6
---

#f5f5f5#363636noneAntes de Gerar o Arquivo Texto da ECF

* Para não ter problemas com a geração e validação do arquivo texto os processos abaixo listados devem ser obrigatoriamente executados.  
  A Receita Federal disponibiliza os Planos de Contas paralelos de acordo com os tipos de lucro.   
  Estes Planos de Contas são disponibilizados para importação no subdiretório de objetos gerenciais do diretório de instalação do RM.   
  Deve-se atentar para que seja importado somente o plano de conta relacionado ao regime de apuração do lucro do contribuinte.
* A Tabela Dinâmica da Receita Federal deve ter sido previamente importada.  
  Todas as Contas Contábeis devem estar associadas a uma conta do Plano de Contas Paralelo utilizado nas configurações da ECF.   
  Existe no TOTVS Gestão Contábil um processo que auxilia na conferência dessa associação.  
  Todos os itens do Evento Tributário e os Lançamentos manuais do Evento Tributário deverão possuir associado um código da tabela dinâmica da ECF.   
  Deve-se atentar para não associar os itens do evento aos códigos Títulos dos Grupos. Se isto for feito a linha referente a esta informação não será importada e o validador não emitirá nenhuma mensagem de erro.
* Certifique-se sempre que o layout a ser utilizado na geração da rotina é sempre o mais atual.   
  Para verificar a data do layout inicie a geração da rotina e veja na tela de parâmetros o primeiro deles é a data.   
  Se não estiver atualizado faça o download de uma versão mais atual na Central de Downloads do Suporte ou solicite ajuda ao suporte por telefone.  
  No TOTVS Gestão Fiscal todos os períodos de Apuração do IRPJ e CSLL devem ter sido encerrados.  
  Todas as Contas do Plano de Contas Paralelo e do LALUR parte B devem possuir data inicial de vigência e final.   
  Esta última somente se a vigência já tiver acabado.  
  Quando for feito o uso da Apuração Virtual para a geração das informações o encerramento trimestral no registro K155 deve-se certificar-se que ele é um espelho do molde de Transferência de Grupos Contábeis.

Alteração da Tabela Dinãmica

* Em relação ao campo "Indica qual o Tributo", será possível a alteração caso o campo "Grupo" for igual a "Lalur parte B".
