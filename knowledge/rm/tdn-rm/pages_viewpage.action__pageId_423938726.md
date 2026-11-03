---
content_hash: 783a5b9f2a43ba3a708183a91907072109219a092cae668c76c75723e4eeece6
fetched_at: '2026-06-29T00:09:28.625307+00:00'
page_id: '423938726'
product: rm
source: tdn-rm
title: Alterar Indicador da Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938726
version: 2
---

Através desta funcionalidade o usuário poderá vincular um indicador de uso a OS pela data de emissão, data de autorização ou data de saída da OS, além de poder desvincular o identificador e vincular um outro à OS. Para acessar esta funcionalidade basta acessar a ordem de serviço e clicar no menu Processo | Alterar Indicador de Uso..

* **Alterar indicadores de uso (Data Emissão):** Buscará o indicador de uso com a data mais próxima (anterior) à data de emissão
* **Alterar indicadores de uso (Data Autorização):** Buscará o indicador de uso com a data mais próxima (anterior) à data de autorização.
* **Alterar indicadores de uso (Data** **saída****):** Buscará o indicador de uso com a data mais próxima (anterior) à data de saída.
* **Vincular Indicador de uso:** Abrirá uma tela para que o usuário escolha um indicador de uso para que seja associado à OS.

**Desvincular indicador de uso:** Irá desvincular o indicador de uso que se encontra preenchido.  
 Juntamente com esta funcionalidade foi criado o parâmetro parâmetro "Não buscar indicador de uso na O.S. automaticamente" na aba ordem de serviço. Ao marcar esse parâmetro, ao abrir uma nova OS o indicador de uso do objeto não vai ser preenchido automaticamente e o usuário terá de fazê-lo de forma manual utilizando a funcionalidade de alteração de indicador de uso. Desmarcando o parâmetro, toda vez que for aberta uma OS o sistema preencherá o campo indicador de uso automaticamente, porem se o usuário optar por alterar o indicador de uso pode fazê-lo com a funcionalidade "Vincular Indicador de Uso".  
***Observação:***Para que as opções "Alterar indicadores de uso (Data Emissão)", "Alterar indicadores de uso (Data Autorização)" e "Alterar indicadores de uso (Data saida)" fiquem visíveis ao clicar com o botão direito do mouse é necessário parametrizar o tipo de movimento, veja:

1. Etapa do Movimento - Datas (Mov - Datas 1/2) marcar o parâmetro "Exibir data e hora de criação do movimento"
2. Etapa do Movimento - Datas (Mov - Datas 2/2)  o parâmetro Hora de Saída deve ser alterado para Edita.

Também é necessário que os campos de data estejam preenchidos na OS para que se possa alterar os indicadores de uso.  
 Se o parâmetro "Campo Indicador de Uso na OS é obrigatório" estiver marcado, não será possível desvincular um indicador de uso pois ao marcar o parâmetro fica obrigatório existir um indicador de uso na Ordem de Serviço.  
***Atenção!***Se existirem planos de manutenção vinculados a ordem de serviço, ao alterar o indicador de uso, o indicador  contido no plano de manutenção  também será alterado para o mesmo indicador da ordem exceto na opção de "Desvincular indicador de uso", onde será mantido o indicador atual do plano de  manutenção.  
 Para saber mais sobre indicadores de uso [clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=423938474).
